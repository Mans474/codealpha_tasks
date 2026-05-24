# Function for chatbot replies
def chatbot():

    print("Simple Chatbot")
    print("Type 'bye' to exit.\n")

    while True:

        # user input
        user_input = input("You: ").lower()

        # Rule-based replies
        if user_input == "hello":
            print("Bot: Hi!")

        elif user_input == "how are you":
            print("Bot: I'm fine!")

        elif user_input == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand.")

# Calling the function chatbot()
chatbot()
