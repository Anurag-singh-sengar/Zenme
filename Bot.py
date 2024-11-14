class ChatBot:
    def __init__(self):
        self.intro = "Hello! I'm Anurag's Chatbot. How can I assist you today?"

    def respond(self, user_input):
        if "hello" in user_input.lower():
            return "Hi there! How can I help you?"
        elif "technology" in user_input.lower():
            return "I love technology! What specific area are you interested in?"
        elif "finance" in user_input.lower():
            return "Finance is fascinating! Are you looking for investment tips?"
        else:
            return "I'm sorry, I didn't understand that."

if __name__ == "__main__":
    bot = ChatBot()
    print(bot.intro)
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        response = bot.respond(user_input)
        print("Chatbot:", response)
