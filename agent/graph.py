from langgraph.constants import END
from langchain_groq import ChatGroq
from langchain.globals import set_debug, set_verbose
from dotenv import load_dotenv
from tools import get_current_directory, list_files, read_file, write_file
from prompts import *
from states import *
from langgraph.graph import StateGraph
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import interrupt, Command
from langsmith import traceable
import os
load_dotenv()

set_debug(True)
set_verbose(True)

llm = ChatGroq(model="openai/gpt-oss-120b")

memory = MemorySaver()
config = { 'configurable': {
    'thread_id': '1'
} }

def planner_agent(state: dict) -> dict:
    user_prompt = state["user_prompt"]
    prompt = planner_prompt(user_prompt)
    result = llm.with_structured_output(Plan).invoke(prompt, config=config)
    value = interrupt("Approve the Project Plan: yes/no")
    if value == "yes":
        return {
            "plan": result
        } 
    else:
        raise ValueError("Plan was not approved. Exiting")

@traceable
def architect_agent(state: dict) -> dict:
    plan = state["plan"]
    resp = llm.with_structured_output(ArchitectOutput).invoke( architect_prompt(plan), config=config)
    if resp is None:
        raise ValueError("Architect did not return a valid response")
    resp.plan = plan

    return {
        "architect_output": resp
    }


@traceable
def developer_agent(state: dict) -> dict:
    developer_output: DeveloperOutput = state.get("developer_output")
    if developer_output is None:
        developer_output = DeveloperOutput(architect_output=state["architect_output"],current_step_idx=0)

    steps = developer_output.architect_output.implementation_tasks
    if developer_output.current_step_idx >= len(steps):
        return {
            "developer_output": developer_output,
            "status": "DONE"
        }

    current_task = steps[developer_output.current_step_idx]
    existing_content = read_file.run(current_task.filepath)

    system_prompt = developer_prompt()
    user_prompt = (
        f"Task: { current_task.task_description}\n"
        f"File: { current_task.filepath}\n"
        f"Exising content:{ existing_content}\n"
        f"Use write_file(path, content) to save your changes."
    )
    
    developer_tools= [read_file, write_file, list_files, get_current_directory]
    react_agent = create_react_agent(llm, developer_tools)
    react_agent.invoke({"messages": [{"role":"system", "content": system_prompt                                },
                                     {"role":"user", "content": user_prompt }
                                     ]
                        
                        }, config=config)
    developer_output.current_step_idx += 1
    return {
        "code": developer_output
    }

graph = StateGraph(dict)
graph.add_node("planner", planner_agent)
graph.add_node("architect", architect_agent)
graph.add_node("developer", developer_agent)

graph.add_edge("planner", "architect")
graph.add_edge("architect", "developer")

graph.add_conditional_edges(
    "developer",
    lambda s:"END" if s.get("status") == 'DONE' else 'developer',
    {"END": END, "developer":"developer"}
)

graph.set_entry_point("planner")

agent = graph.compile(checkpointer=memory)

user_prompt = "create a landing page for a Mortgage Brokerage company"

result = agent.invoke({
    "user_prompt": user_prompt
},
config
)
value = input("Approve: yes/no")
agent.invoke(Command(resume=value), config=config)
print(result)


