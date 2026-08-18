import datetime
import math


# -------------------------
# Agent Memory
# -------------------------

memory = []


# -------------------------
# Tools
# -------------------------

def get_time():
    return datetime.datetime.now().strftime("%H:%M:%S")


def get_date():
    return datetime.datetime.now().strftime("%d-%m-%Y")


def calculator(expression):
    try:
        result = eval(expression, {"__builtins__": None}, {})
        return f"The answer is {result}"
    except:
        return "Sorry, I could not calculate that."


def remember(text):
    memory.append(text)
    return "I will remember that."


def show_memory():
    if not memory:
        return "I don't remember anything yet."

    return "I remember: " + ", ".join(memory)


# -------------------------
# AI Agent
# -------------------------

def agent(user_input):

    text = user_input.lower()

    # Greeting
    if "hello" in text or "hi" in text:
        return "Hello! I am your AI agent. How can I help you?"

    # Time
    elif "time" in text:
        return "The current time is " + get_time()

    # Date
    elif "date" in text:
        return "Today's date is " + get_date()

    # Memory
    elif text.startswith("remember"):
        information = user_input[8:].strip()

        if information:
            return remember(information)

        return "What should I remember?"

    # Show memory
    elif "what do you remember" in text:
        return show_memory()

    # Calculator
    elif "calculate" in text:
        expression = user_input.lower().replace("calculate", "").strip()
        return calculator(expression)

    # Exit
    elif text == "bye":
        return "Goodbye! 👋"

    # Unknown command
    else:
        return (
            "I don't understand that yet.\n"
            "Try: hello, time, date, calculate 10+20,\n"
            "remember my favorite color is blue, or what do you remember?"
        )


# -------------------------
# Start Agent
# -------------------------

print("=" * 40)
print("🤖 ADVANCED PYTHON AI AGENT")
print("=" * 40)

print("Type 'bye' to stop.\n")


while True:

    user = input("You: ")

    response = agent(user)

    print("Agent:", response)

    if user.lower() == "bye":
        break
