from input_handler import UserInput

class BaseMenu:
    def __init__(self, title, options):
        self.title = title
        self.options = options  # Dict: { "1": ("Description", function_to_call), ... }

    def display(self):
        while True:
            print(f"\n==== {self.title} ====")
            for key, (desc, _) in self.options.items():
                print(f"{key}. {desc}")
            choice = UserInput.get_menu_choice(self.options.keys())
            _, action = self.options[choice]
            if action:
                result = action()
                if result == "back":
                    break
                elif result == "exit":
                    exit()

    def display(self, options):
        while True:
            print(f"\n==== {self.title} ====")
            for key, (desc, _) in options.items():
                print(f"{key}. {desc}")
            choice = UserInput.get_menu_choice(options.keys())
            _, action = options[choice]
            if action:
                result = action()
                if result == "back":
                    break
                elif result == "exit":
                    exit()
