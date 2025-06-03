# input_handler.py

def get_choice(valid_choices):
    while True:
        choice = input("\nSelect an option: ").strip()
        if choice in valid_choices:
            return choice
        print("Invalid choice. Try again.")
