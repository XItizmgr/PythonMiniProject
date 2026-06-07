history_file = "history.txt"


def show_history():
    with open(history_file, "r") as file:
        lines = file.readlines()

        if len(lines) != 0:
            for line in reversed(lines):
                print(line.strip())


def clear_history():
    file = open(history_file, "w")
    print("History clear")
    file.close()


def append_history(equestion, result):
    file = open(history_file, "a")
    file.write(f"{equestion} = {result} \n")
    file.close()


def calculator(user_input):
    parts = user_input.split()
    num1 = int(parts[0])
    oprator = parts[1]
    num2 = int(parts[2])
    if oprator == "+":
        result = num1 + num2
    elif oprator == "-":
        result = num1 - num2
    elif oprator == "*":
        result = num1 * num2
    elif oprator == "/":
        if num2 == 0:
            print("cannot divide by zero")
            return
        result = num1 / num2
    elif oprator == "%":
        result = num1 % num2
    else:
        print(
            "calculation can be done using only  (+, -, *, /, %) : Enter a valid oprator  "
        )
        return
    print("Result =", result)
    append_history(user_input, result)


while True:
    user_input = input(
        "Enter a calculation (+, -, *, /, %) or type 'history', 'clear history', or 'exit': "
    ).strip()
    if user_input == "history":
        show_history()
    elif user_input == "clear history":
        clear_history()
    elif user_input == "exit":
        print("goodbyee see u later")
        break
    else:
        calculator(user_input)
