import sys

class Chatbot:
    def __init__(self,patterns):
            self.patterns=dict(sorted(patterns.items(), key=lambda x: -len(x[0])))

    def get_response(self,user_input):

        if user_input=='exit':
            print('The program is finished now.')
            sys.exit()

        for key in self.patterns:
            if key in user_input:
                 return self.patterns[key]
        return 'I don`t get it.'

    def chat(self):
             while True:
                user_input=input('You: ').strip().lower()
                response=self.get_response(user_input)
                print('Bot:',response)

def main():
    patterns = {
        "hello": "Hi!",
        "hi": "Hello!",
        "hey": "Hey there!",
        "good morning": "Good morning!",
        "good evening": "Good evening!",
        "your name": "I'm a simple chatbot.",
        "who are you": "I'm just a program, nothing fancy.",
        "what are you": "A rule-based chatbot.",
        "sad": "Why are you feeling sad?",
        "happy": "Nice, what's making you happy?",
        "angry": "What happened?",
        "tired": "You should get some rest.",
        "bored": "Try doing something new.",
        "how are you": "I'm fine. What about you?",
        "what's up": "Not much. You?",
        "what are you doing": "Talking to you.",
        "python": "Python is great for beginners.",
        "programming": "It takes practice, not talent.",
        "code": "Debugging is where you really learn.",
        "error": "Read the error message carefully.",
        "bug": "Bugs are normal.",
        "math": "Math builds your thinking.",
        "logic": "Logic is everything in programming.",
        "problem": "Break it into smaller parts.",
        "time": "Use it wisely.",
        "sleep": "Sleep matters more than you think.",
        "work": "Consistency beats intensity.",
        "success": "It takes time.",
        "joke": "I would, but I'm not that funny yet.",
        "funny": "Glad you think so.",
        "music": "Music helps focus.",
        "game": "Games are fun, but don't overdo it.",
        "yes": "Alright.",
        "no": "Why not?",
        "thanks": "No problem.",
        "thank you": "You're welcome.",
        "bye": "Goodbye!",
        "see you": "See you later!",
        "exit": "Exiting..."
    }

    bot=Chatbot(patterns)
    bot.chat()

if __name__=='__main__':
     main()
     