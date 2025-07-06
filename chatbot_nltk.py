responses = {
    "hello": "Hi there!",
    "how are you": "I'm a bot, but I'm doing great!",
    "name": "I'm your friendly chatbot!",
    "bye": "Goodbye! See you soon."
}

print("Hi! I'm your rule-based chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()
    if user_input == 'bye':
        print("Chatbot: Goodbye!")
        break
    response = responses.get(user_input, "Sorry, I don't understand that.")
    print("Chatbot:", response)
