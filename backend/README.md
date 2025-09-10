# AI App Builder

An intelligent application generator that uses a multi-agent system to automatically create web applications based on natural language descriptions. The system employs three specialized AI agents working in sequence to plan, architect, and develop complete applications.

## 🚀 Features

- **Multi-Agent Architecture**: Three specialized AI agents work together to create applications
- **Natural Language Input**: Describe what you want to build in plain English
- **Automated Code Generation**: Complete, production-ready code with proper structure
- **File Management**: Safe file operations with project isolation
- **Modern Web Technologies**: Generates HTML, CSS, and JavaScript applications
- **Structured Planning**: Breaks down complex requirements into manageable tasks

## 🏗️ Architecture

The system uses three specialized agents:

### 1. **Planner Agent**
- Converts user prompts into comprehensive engineering project plans
- Defines app name, description, features, technologies, and file structure
- Creates a structured plan using Pydantic models

### 2. **Architect Agent**
- Breaks down the project plan into specific implementation tasks
- Orders tasks based on dependencies
- Provides detailed task descriptions with integration details
- Ensures each task is self-contained but builds upon previous work

### 3. **Developer Agent**
- Implements each task using a ReAct (Reasoning + Acting) pattern
- Uses tools to read, write, and manage files safely
- Maintains code consistency and integration
- Executes tasks sequentially until completion

## 🛠️ Tools

The developer agent has access to several tools:

- `write_file(path, content)`: Safely writes content to files within the project
- `read_file(path)`: Reads existing file content for context
- `list_files(directory)`: Lists files in a directory
- `get_current_directory()`: Gets the current working directory
- `run_cmd(cmd, cwd, timeout)`: Executes shell commands safely

## 📋 Requirements

- Python 3.11+
- Groq API key (for the LLM)
- Required dependencies (see pyproject.toml)

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ai-app-builder
   ```

2. **Install dependencies**
   ```bash
   pip install -e .
   ```

3. **Set up environment variables**
   Create a `.env` file with your Groq API key:
   ```bash
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

## 📝 Usage

The system is currently configured to generate a landing page for a Mortgage Brokerage company. To customize:

1. Edit the `user_prompt` variable in `agent/graph.py` (line 96)
2. Run the application
3. Check the `generated_project/` directory for the output

### Example Prompts

- "Create a landing page for a Mortgage Brokerage company"
- "Build a simple calculator web app"
- "Generate a portfolio website for a photographer"
- "Create a blog website with contact form"

## 📁 Project Structure

```
ai-app-builder/
├── agent/
│   ├── graph.py          # Main agent orchestration
│   ├── prompts.py        # Agent prompts and instructions
│   ├── states.py         # Pydantic models for data structures
│   ├── tools.py          # File and system operation tools
│   └── test.py           # Test utilities
├── generated_project/    # Output directory for generated apps
│   ├── index.html
│   └── styles/
│       └── style.css
├── main.py              # Entry point
├── pyproject.toml       # Project configuration
└── README.md
```

## 🔧 Configuration

### Dependencies

The project uses several key dependencies:

- **LangChain**: Framework for building LLM applications
- **LangGraph**: For creating multi-agent workflows
- **Groq**: High-performance LLM inference
- **Pydantic**: Data validation and settings management

### Model Configuration

Currently configured to use Groq's `openai/gpt-oss-120b` model. To change:

1. Edit the model name in `agent/graph.py` (line 16)
2. Ensure your Groq API key has access to the selected model

## 🛡️ Security Features

- **Path Safety**: All file operations are restricted to the project directory
- **Input Validation**: Pydantic models ensure data integrity
- **Sandboxed Execution**: Generated code runs in isolated environment

## 🎯 Example Output

The system generates complete web applications with:

- Responsive HTML structure
- Modern CSS styling
- Interactive JavaScript components
- SEO optimization
- Accessibility features
- Cross-browser compatibility

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For issues and questions:

1. Check the existing issues
2. Create a new issue with detailed description
3. Include error messages and system information

## 🔮 Future Enhancements

- Support for additional frameworks (React, Vue, Angular)
- Database integration capabilities
- API generation features
- Deployment automation
- Multi-language support
- Custom template system
