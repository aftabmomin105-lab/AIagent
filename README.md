# AIagent
# 🤖 Basic AI Agent

## 📌 Project Overview

This project is a basic **AI Agent** developed using **Python** and the **OpenAI API**.

The agent accepts questions or instructions from the user and sends them to an AI model through the OpenAI API. The generated response is then displayed to the user.

This project is developed as part of the **AI-Augmented Workflow** course to understand how artificial intelligence can be integrated into a Python application and how AI-assisted coding tools can support software development.

---

## 🎯 Objectives

The main objectives of this project are:

* To understand the basic concept of an AI Agent.
* To develop a simple AI Agent using Python.
* To connect a Python application with an AI model using an API.
* To understand API-based communication.
* To use AI-assisted coding tools during development.
* To practice testing and debugging AI-generated code.
* To document the development process using an Architecture Decision Record (ADR).

---

## 🛠️ Technologies Used

| Technology     | Purpose                |
| -------------- | ---------------------- |
| Python         | Programming language   |
| OpenAI API     | AI model communication |
| VS Code        | Code editor            |
| Git            | Version control        |
| GitHub         | Code repository        |
| GitHub Copilot | AI-assisted coding     |
| Markdown       | Project documentation  |

---

## 🏗️ System Architecture

The basic architecture of the AI Agent is:

```text
              ┌──────────────┐
              │     User     │
              └──────┬───────┘
                     │
                     │ Question / Prompt
                     ▼
              ┌──────────────┐
              │ Python Agent │
              └──────┬───────┘
                     │
                     │ API Request
                     ▼
              ┌──────────────┐
              │  OpenAI API  │
              └──────┬───────┘
                     │
                     │ AI Response
                     ▼
              ┌──────────────┐
              │ Python Agent │
              └──────┬───────┘
                     │
                     ▼
              ┌──────────────┐
              │     User     │
              └──────────────┘
```

---

## 📂 Project Structure

```text
AI-Agent-Project/
│
├── README.md
├── ADR.md
├── CONTRIBUTION_LOG.md
├── requirements.txt
├── .gitignore
│
├── src/
│   └── agent.py
│
└── screenshots/
    ├── project-structure.png
    ├── agent-running.png
    ├── copilot.png
    └── github.png
```

---

## ⚙️ Installation

### Step 1: Install Python

Make sure Python is installed on your computer.

Check the installed version:

```bash
python --version
```

---

### Step 2: Create a Virtual Environment

Open the terminal in the project directory:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

---

### Step 3: Install Required Package

Install the OpenAI Python library:

```bash
pip install openai
```

Save the dependencies:

```bash
pip freeze > requirements.txt
```

---

## 🔑 API Key Configuration

The OpenAI API requires an API key.

The API key should **not** be written directly inside the Python source code.

Set the API key as an environment variable.

### Windows

```cmd
setx OPENAI_API_KEY "your_api_key_here"
```

After setting the variable, restart VS Code or the terminal.

### Security

Never upload your API key to GitHub.

The `.gitignore` file should contain:

```text
.env
venv/
__pycache__/
```

---

## 💻 Running the AI Agent

Run the following command from the project directory:

```bash
python src/agent.py
```

The program will display:

```text
===== Basic AI Agent =====
Type 'exit' to stop the agent.

You:
```

Enter a question, for example:

```text
You: What is Artificial Intelligence?
```

The AI Agent will generate a response:

```text
Agent: Artificial Intelligence is a field of computer science...
```

To stop the program:

```text
You: exit
```

---

## 🧠 Basic Agent Workflow

The working process of the project is:

```text
User Input
    ↓
Python Program
    ↓
OpenAI API
    ↓
AI Model
    ↓
Generated Response
    ↓
Python Program
    ↓
User
```

---

## 🤖 AI-Assisted Development

AI tools are used during the development of this project to support:

* Python code generation
* Code explanation
* Debugging
* Error identification
* Documentation
* Project structure planning

The AI-generated code is reviewed and tested by the student before being used in the final project.

The development workflow is:

```text
AI Suggestion
      ↓
Human Review
      ↓
Code Modification
      ↓
Testing
      ↓
Final Implementation
```

---

## 📝 Architecture Decision Record

The project's main technical decision is documented in:

```text
ADR.md
```

### Selected Technology Stack

**Python + OpenAI API + VS Code + GitHub Copilot + Git/GitHub**

The ADR explains:

* Why Python was selected.
* Why the OpenAI API was selected.
* Alternative options such as Ollama.
* Advantages and disadvantages.
* AI-assisted coding compatibility.
* Security considerations.

---

## 📊 Testing

The AI Agent can be tested using different questions.

| Test No. | Input                         | Expected Result      | Status |
| -------- | ----------------------------- | -------------------- | ------ |
| 1        | What is AI?                   | AI explanation       | Pass   |
| 2        | Explain Python                | Python explanation   | Pass   |
| 3        | What is an AI Agent?          | AI Agent explanation | Pass   |
| 4        | Give three applications of AI | Three applications   | Pass   |
| 5        | exit                          | Program terminates   | Pass   |

---

## 📸 Project Evidence

Screenshots of the project can be stored in the `screenshots` folder.

Recommended screenshots:

1. Project folder structure
2. Python code in VS Code
3. AI Agent running in the terminal
4. AI-assisted coding using GitHub Copilot
5. GitHub repository
6. Testing results

---

## 📋 AI Contribution Log

AI-assisted contributions are recorded in:

```text
CONTRIBUTION_LOG.md
```

The contribution log records:

* Date
* File or section
* AI tool used
* AI-generated suggestion
* Student's modifications
* Testing performed

---

## 🔐 Security Considerations

The API key is treated as a secret credential.

The following practices are followed:

* API keys are not hard-coded.
* API keys are not uploaded to GitHub.
* Sensitive files are added to `.gitignore`.
* AI-generated code is reviewed before use.

---

## 🚀 Future Improvements

The basic AI Agent can be extended with:

* Voice input
* Voice output
* Chat history
* Web search
* File/document processing
* User interface
* Memory
* Multiple AI tools
* Local AI models using Ollama
* Task planning and execution

---

## 📚 Learning Outcomes

After completing this project, the following concepts are understood:

* Basic AI Agent architecture
* Python programming
* API communication
* AI model interaction
* Environment variables
* Git and GitHub
* AI-assisted programming
* Code testing and debugging
* Technical documentation
* Architecture Decision Records

---

## ✅ Conclusion

The **Basic AI Agent** demonstrates how a Python application can communicate with an AI model through an API and provide responses to user queries.

The project also demonstrates an **AI-Augmented Workflow**, where AI tools are used to assist with coding, debugging, documentation, and development while the student remains responsible for reviewing, testing, and understanding the final implementation.

This project provides a foundation for developing more advanced AI Agents with additional tools, memory, planning, and automation capabilities.

---

## 👨‍🎓 Project Information

**Project:** Basic AI Agent
**Course:** AI-Augmented Workflow
**Programming Language:** Python
**AI Platform:** OpenAI API
**Development Tool:** Visual Studio Code
**Version Control:** Git/GitHub
**Documentation:** Markdown
