print("Hi! I'm your chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Bye! Have a great day!")
        break
    else:
        print("Chatbot: I'm still learning, but you said:", user_input)
