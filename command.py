from abc import ABC, abstractmethod
import json 
import time 
import re
import random
import os

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass 

class Clear_Screen(Command):
    def execute(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system("clear")

class Greet_User(Command):
    def __init__(self, description: str, message: str, delay: int) -> None:
        self.description = description
        self.message = message
        self.delay = delay

    def execute(self):
        print(self.description)
        time.sleep(self.delay)
        print(self.message)
 
class Search_Symbols(Command):
    def __init__(self, text: str) -> None:
        self.text = text
        self.q_mark = r"\?"
        self.e_mark = r"\!"

    def execute(self):
        pass 

class Open_File(Command):
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def execute(self):
        with open(self.file_path, "r") as file:
            return json.load(file)

class Process_Output(Command):
    def __init__(self, text: str, basis_data: dict) -> None:
        self.words = text.split()
        self.text = text.lower()
        self.basis_data = basis_data
        self.frequency = {}
    
    def execute(self):
        for category, content in self.basis_data.items():
            sorted_words = sorted(content['words'], key=len, reverse=True)
            for phrase in sorted_words:
                weight = len(phrase.split())
                pattern = r'\b' + re.escape(phrase.lower()) + r'\b'
                matches = re.findall(pattern, self.text)
                if matches:
                    self.frequency[category] = self.frequency.get(category, 0) + weight
                    index = content['words'].index(phrase)
        
        if not self.frequency:
            print(f"--> Hmm, I'm not sure how to respond to that, but I'm listening!")
            return True
        
        max_category = max(self.frequency, key=self.frequency.get)
        if max_category == "exit":
            responses = self.basis_data[max_category]['response']
            print(f"--> {random.choice(responses)}")
            return False
        elif max_category == "interogative":
            responses = self.basis_data[max_category]['response'][index]
            print(f"--> {responses}")
            return True
        else:
            responses = self.basis_data[max_category]['response']
            print(f"--> {random.choice(responses)}")
            return True

        # for word in self.words:
        #     if word.lower() in self.basis_data['exit']['words']:
        #         if "exit" not in self.frequency:
        #             self.frequency["exit"] = 1
        #         else:
        #             self.frequency["exit"] += 1
        #     elif word.lower() in self.basis_data['greetings']['words']:
        #         if "greetings" not in self.frequency:
        #             self.frequency["greetings"] = 1
        #         else:
        #             self.frequency["greetings"] += 1
        #     elif word.lower() in self.basis_data['affirmation']['words']:
        #         if "gen z" not in self.frequency:
        #             self.frequency["affirmation"] = 1
        #         else:
        #             self.frequency["affirmation"] += 1
        #     elif word.lower() in self.basis_data['negation']['words']:
        #         if "gen z" not in self.frequency:
        #             self.frequency["negation"] = 1
        #         else:
        #             self.frequency["negation"] += 1
        #     else:
        #         if "unknown" not in self.frequency:
        #             self.frequency["unknown"] = 1
        #         else:
        #             self.frequency["unknown"] += 1

        # max_key = max(self.frequency, key=self.frequency.get)
        
        # if max_key == 'unknown':
        #     print("-- I can't process that!")
        # else:
        #     print(random.choice(self.basis_data[max_key]['response']))

class Conversation(Command):
    def __init__(self, file) -> None:
        self.running = True
        self.file = file
    
    def execute(self):
        while self.running:
            user_input = input(">> ")
            self.running = Process_Output(user_input, self.file).execute()