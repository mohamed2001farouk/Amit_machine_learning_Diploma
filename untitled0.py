import random
import json

class Chatbot:
    def __init__(self, response_file):
        self.responses = self.load_responses(response_file)
    
    def load_responses(self, file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    def get_response(self, user_input):
        for key in self.responses:
            if key in user_input.split():
                return random.choice(self.responses[key])
        return random.choice(self.responses["default"])

    def chat(self):
        print("Chatbot: Hi! How can I assist you today?")
        while True:
            user_input = input("User: ").lower()
            response = self.get_response(user_input)
            print("Chatbot:", response)
            if user_input == "goodbye":
                break

if __name__ == "__main__":
    bot = Chatbot('responses.json')
    bot.chat()
