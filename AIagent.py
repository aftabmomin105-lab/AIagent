from openai import OpenAI

client = OpenAI()

print("===== Basic AI Agent =====")
print("Type 'exit' to stop the agent.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Agent: Goodbye!")
        break

    response = client.responses.create(
        model="gpt-5",
        input=user_input
    )

    print("Agent:", response.output_text)