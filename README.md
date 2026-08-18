# 🤖 Advanced Python AI Agent

A simple **rule-based AI Agent built using Python**.
This project demonstrates how an AI agent can interact with users, perform basic tasks, and maintain simple memory during program execution.

---

## 📌 Project Overview

This Python AI Agent can:

* 👋 Respond to greetings
* 🕐 Display the current time
* 📅 Display the current date
* 🧮 Perform basic calculations
* 🧠 Remember information provided by the user
* 💭 Display previously remembered information
* 👋 Exit the program when the user types `bye`

The project is designed for beginners to understand the basic structure and working of an AI agent.

---

## 🛠️ Technologies Used

* **Python 3**
* `datetime` module
* `math` module
* Python functions
* Lists
* Conditional statements
* User input/output
* Basic expression evaluation

---

## 📂 Project Structure

```text
AI-Agent/
│
├── ai_agent.py
└── README.md
```

### Files

| File          | Description                                 |
| ------------- | ------------------------------------------- |
| `ai_agent.py` | Main Python program containing the AI Agent |
| `README.md`   | Documentation for the project               |

---

## ⚙️ Features

### 1. Greeting

The agent recognizes simple greetings such as:

```text
hello
hi
```

Example:

```text
You: hello
Agent: Hello! I am your AI agent. How can I help you?
```

---

### 2. Current Time

The agent can display the current system time.

Example:

```text
You: time
Agent: The current time is 16:30:25
```

The time is obtained using Python's `datetime` module.

---

### 3. Current Date

The agent can display today's date.

Example:

```text
You: date
Agent: Today's date is 18-08-2026
```

---

### 4. Calculator

The agent can perform basic mathematical calculations.

Example:

```text
You: calculate 10+20
Agent: The answer is 30
```

Other examples:

```text
calculate 50-20
calculate 5*10
calculate 100/4
calculate 2**5
```

---

### 5. Agent Memory

The agent has a simple memory system using a Python list.

The user can tell the agent to remember something.

Example:

```text
You: remember my favorite color is blue
Agent: I will remember that.
```

The information is stored in the `memory` list.

---

### 6. Show Memory

The user can ask:

```text
You: what do you remember?
```

Example response:

```text
Agent: I remember: my favorite color is blue
```

Multiple pieces of information can also be stored.

Example:

```text
You: remember my favorite color is blue
You: remember I like football
You: what do you remember?

Agent: I remember: my favorite color is blue, I like football
```

> **Note:** This memory exists only while the Python program is running. It is not permanently saved to a file or database.

---

### 7. Exit the Agent

To stop the program, type:

```text
bye
```

Example:

```text
You: bye
Agent: Goodbye! 👋
```

---

## 🧠 How the AI Agent Works

The agent follows a simple decision-making process:

```text
User Input
    ↓
Convert Input to Lowercase
    ↓
Analyze User Command
    ↓
Identify Required Action
    ↓
Call Appropriate Function
    ↓
Generate Response
    ↓
Display Response
```

For example:

```text
User: What time is it?
        ↓
Agent detects "time"
        ↓
get_time()
        ↓
Current time is returned
        ↓
Agent displays the result
```

---

## 🔧 Main Functions

### `get_time()`

Returns the current system time.

```python
def get_time():
    return datetime.datetime.now().strftime("%H:%M:%S")
```

---

### `get_date()`

Returns the current date.

```python
def get_date():
    return datetime.datetime.now().strftime("%d-%m-%Y")
```

---

### `calculator(expression)`

Evaluates a mathematical expression and returns the result.

```python
def calculator(expression):
    try:
        result = eval(expression, {"__builtins__": None}, {})
        return f"The answer is {result}"
    except:
        return "Sorry, I could not calculate that."
```

---

### `remember(text)`

Stores information in the agent's memory.

```python
def remember(text):
    memory.append(text)
    return "I will remember that."
```

---

### `show_memory()`

Displays information stored in memory.

```python
def show_memory():
    if not memory:
        return "I don't remember anything yet."

    return "I remember: " + ", ".join(memory)
```

---

### `agent(user_input)`

This is the main decision-making function.

It analyzes the user's input and decides which action should be performed.

For example:

```python
if "time" in text:
    return "The current time is " + get_time()
```

---

## ▶️ How to Run the Project

### Step 1: Install Python

Make sure **Python 3** is installed on your computer.

Check the installation using:

```bash
python --version
```

or:

```bash
py --version
```

---

### Step 2: Open the Project

Open the project folder in **VS Code**.

Make sure your Python file is saved as:

```text
ai_agent.py
```

---

### Step 3: Run the Program

Open the VS Code terminal and run:

```bash
python ai_agent.py
```

If that does not work on Windows, try:

```bash
py ai_agent.py
```

---

## 💻 Example Execution

```text
========================================
🤖 ADVANCED PYTHON AI AGENT
========================================
Type 'bye' to stop.

You: hello
Agent: Hello! I am your AI agent. How can I help you?

You: time
Agent: The current time is 16:30:25

You: date
Agent: Today's date is 18-08-2026

You: calculate 25+75
Agent: The answer is 100

You: remember my favorite color is blue
Agent: I will remember that.

You: what do you remember?
Agent: I remember: my favorite color is blue

You: bye
Agent: Goodbye! 👋
```

---

## 📋 Supported Commands

| Command                 | Function                 |
| ----------------------- | ------------------------ |
| `hello`                 | Greets the user          |
| `hi`                    | Greets the user          |
| `time`                  | Shows current time       |
| `date`                  | Shows current date       |
| `remember ...`          | Stores information       |
| `what do you remember?` | Shows stored information |
| `calculate 10+20`       | Performs calculation     |
| `bye`                   | Stops the agent          |

---

## 🔒 Limitations

This is a **basic rule-based AI agent**, so it has some limitations:

1. It does not use a real Large Language Model (LLM).
2. It understands only predefined commands.
3. Memory is temporary.
4. Memory is lost when the program is closed.
5. The calculator supports expressions that Python's `eval()` accepts.
6. It does not understand natural language as flexibly as modern AI assistants.

---

## 🚀 Future Improvements

The project can be extended with:

* 🧠 Permanent memory using files or databases
* 🤖 Integration with an actual LLM/API
* 🎤 Voice input
* 🔊 Voice output
* 🌐 Web search capability
* 📁 File handling
* 🖥️ Graphical User Interface (GUI)
* 🔐 Better input validation
* 📊 Logging of agent activities
* 🧩 Multiple specialized tools
* 💬 Better natural-language understanding

---

## 🎯 Learning Objectives

This project helps demonstrate:

* Python programming fundamentals
* Functions
* Conditional statements
* Lists
* Exception handling
* User input and output
* Modular programming
* Tool-based agent design
* Basic memory implementation
* Decision-making logic

---

## 👨‍💻 Project Type

**Project:** Basic AI Agent
**Language:** Python
**Level:** Beginner
**Purpose:** Educational / College Project
**Course:** AI-Augmented Workflow

---

## 📜 License

This project is created for **educational and academic purposes**.

---

## ⭐ Conclusion

This project demonstrates the basic concept of an **AI Agent** using Python. The agent receives user input, identifies the requested task, calls an appropriate function, and returns a response.

Although it is a simple rule-based implementation, it provides a foundation for developing more advanced AI agents with **LLMs, external tools, databases, APIs, and permanent memory**.
