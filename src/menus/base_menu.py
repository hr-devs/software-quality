# base_menu.py

from input_handler import get_choice

class BaseMenu:
    def __init__(self, title, options):
        self.title = title
        self.options = options  # Dict: { "1": ("Description", function_to_call), ... }

    def display(self):
        while True:
            print(f"\n==== {self.title} ====")
            for key, (desc, _) in self.options.items():
                print(f"{key}. {desc}")
            choice = get_choice(self.options.keys())
            _, action = self.options[choice]
            if action:
                result = action()
                if result == "back":
                    break
                elif result == "exit":
                    exit()
