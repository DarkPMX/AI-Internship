greetings = {"hello", "hi", "hey", "sup", "howdy", "morning", "namaste"}

goodbye = {"asta lavista", "sayonara", "bye", "tata", "goodbye"}

responses = {
    "thanks": "You're welcome!",
    "who are you?": "I am a chatbot. How may I help you?",
    "what is your name?": "My name is The Bot.",
    "python": "Python is a high-level programming language used to create software programs.",
    "what is your favourite food?": "My favourite food is pizza.",
    "variables": "Variables are used to store data in a program.",
    "functions": "Functions are used to perform specific tasks in a program.",
    "data types": "Data types are used to specify the type of data stored in a variable.",
    "loops": "Loops are used to repeat a block of code a specified number of times.",
    "arrays": "Arrays are used to store multiple values in a single variable.",
    "dictionaries": "Dictionaries are used to store key-value pairs of data.",
    "hello": "Hi there! How can I assist you today?",
    "hi": "Hello! What can I do for you?",
    "hey": "Hey! How can I help you?",
    "sup": "Not much, just here to chat! How about you?",
    "howdy": "Howdy! What can I do for you?",
    "morning": "Good morning! How can I assist you today?",
    "namaste": "Namaste! How can I help you today?",
    "asta lavista": "Asta lavista! Take care!",
    "sayonara": "Sayonara! See you later!",
    "bye": "Goodbye! Have a great day!",
    "tata": "Tata! Take care!",
    "goodbye": "Goodbye! See you soon!"
    
}

print("Hi, welcome to your Python dictionary!!")
print("Chat with me and learn Python... it's that easy!!!")

user = input("You:")
if user in responses:
    print("Bot: " + responses[user])
else:
    print("Bot: Sorry, I don't understand")