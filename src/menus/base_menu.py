from input_handler import UserInput

class BaseMenu:
    def __init__(self, title, get_options):
        self.title = title
        self.get_options = get_options # Dict: { "1": ("Description", function_to_call), ... }

    def display(self):
        while True:
            options = self.get_options() 
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

