from datetime import datetime

HISTORY_FILE = "history.txt"

def save_history(operation, result):
    with open(HISTORY_FILE, "a") as file:
# Will open history.py as a file.

        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{time}] {operation} = {result}\n")
# will show the date and time of usage of the calculator.

def show_history():
# It will display the history of the calculator.

    try:
        with open(HISTORY_FILE, "r") as file:
            history = file.read()

            if history:
                print("\n========== CALCULATION HISTORY ==========")
                print(history)
            else:
                print("\nNo calculation history found.")

    except FileNotFoundError:
# it is error handling.
         print("\nNo calculation history found.")

def clear_history():
# it will clear the history.

    with open(HISTORY_FILE, "w") as file:
        file.write("")

    print("\nCalculation history cleared.")