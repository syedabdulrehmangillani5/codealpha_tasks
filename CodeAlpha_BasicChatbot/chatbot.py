"""
CodeAlpha Python Internship - Task 4: Basic Chatbot
Author: Your Name
Description: A simple rule-based chatbot that replies to predefined
             messages such as "hello", "how are you" and "bye".
"""


def get_response(user_input):
    """Return the chatbot's reply for the given user message."""
    message = user_input.strip().lower()

    if message in ("hello", "hi", "hey"):
        return "Hi!"
    elif message == "how are you":
        return "I'm fine, thanks!"
    elif message == "what is your name":
        return "I'm CodeAlpha Bot."
    elif message == "help":
        return "Try saying: hello, how are you, what is your name, or bye."
    elif message in ("bye", "goodbye"):
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that. Type 'help' to see what I can do."


def main():
    print("=== CodeAlpha Chatbot === (type 'bye' to exit)")
    while True:
        user_input = input("You: ")
        reply = get_response(user_input)
        print("Bot:", reply)
        if user_input.strip().lower() in ("bye", "goodbye"):
            break


if __name__ == "__main__":
    main()
