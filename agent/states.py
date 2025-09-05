from pydantic import BaseModel, ConfigDict, Field
from typing import Optional

class File(BaseModel):
    path: str = Field(description="The path of the file to be created")
    purpose: str = Field(description="The purpose of the file to be created")

class Plan(BaseModel):
    name: str = Field(description="The name of the App to be built")
    description: str = Field(description="The oneline description of the App to be built e.g. A simple calculator web app that allows users to add, subtract, multiply and divide numbers")

    features: list[str] = Field(description="List of features of the App to be built e.g. 'user authentication', 'data storage', 'user interface'")
    technologies: list[str] = Field(description="The technologies used in the App to be built e.g. 'React', 'Node.js', 'PostgreSQL', 'python', 'flask")
    files: list[File] = Field(description="A list of files to be created each with a 'path' and 'purpose' e.g. 'index.html', 'style.css', 'script.js'")
    


class ImplementationTask(BaseModel):
    filepath: str = Field(description="The path of file to be modified")
    task_description: str = Field(description="detailed description of the task to be performed on the file e,g. 'add user authentication' ")

class ArchitectOutput(BaseModel):
    implementation_tasks: list[ImplementationTask] = Field(description=" a list of tasks to be taken to implement")
    model_config = ConfigDict(extra="allow")
    

class DeveloperOutput(BaseModel):
    architect_output: ArchitectOutput = Field(description="The plan for the task to be implemented")
    current_step_idx: int = Field(description="The index of the current step in the implementation steps")
    current_file_content: Optional[str] = Field(default=None, description="The content of the current file to be modified")

    