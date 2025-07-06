import cohere

# Replace with your actual Cohere API key
co = cohere.Client("epolonJB0B1s6x1pKUNgANlAklla0iELvdqI9l78")

print("Hi! I'm your Cohere-powered AI Chatbot. Type 'bye' to exit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye! 👋")
        break

    response = co.generate(
        model='command-light',
        prompt=f"You are a helpful assistant. User: {user_input}\nAssistant:",
        max_tokens=100
    )

    print("Chatbot:", response.generations[0].text.strip())
