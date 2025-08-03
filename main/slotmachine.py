import random

ROWS = 3
COLS = 3

symbols = {
    "A": 2,
    "B": 3,
    "C": 4,
}

MIN_LINES = 1
MAX_LINES = 3

MIN_BET = 1
MAX_BET = 10


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    # incorrectly assigned in the tutorial
    current_symbols = all_symbols[:]
    for _ in range(cols):
        column = []
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


def deposit():
    while True:
        amount = input("Please enter the amount to be deposited: ")
        if not amount.isdigit():
            print("Please enter a number.")
            continue

        amount = int(amount)
        if amount <= 0:
            print("Amount must be greater than 0.")
            continue

        break
    return amount


def get_number_of_lines():
    while True:
        lines = input(
            f"Please enter the number of lines to bet on ({str(MIN_LINES)}-{str(MAX_LINES)}) : ")
        if not lines.isdigit():
            print("Please enter a number.")
            continue

        lines = int(lines)
        if not (MIN_LINES <= lines <= MAX_LINES):
            print(
                f"Lines must be between {str(MIN_LINES)} and {str(MAX_LINES)}.")
            continue

        break

    return lines


def get_total_bet(balance, lines):
    while True:
        amount = input("Please enter the bet on each line: ")
        if not amount.isdigit():
            print("Please enter a number.")
            continue

        amount = int(amount)
        total_bet = amount * lines

        if not (MIN_BET <= amount <= MAX_BET):
            print(f"A bet must be between {MIN_BET} and {MAX_BET}.")
            continue

        if total_bet > balance:
            print(
                f"Insufficient deposits. Maximum allowed bet is {balance//lines}")
            continue

        break
    return total_bet


def main():
    balance = deposit()
    lines = get_number_of_lines()
    total_bet = get_total_bet(balance, lines)

    print(
        f"Total deposits: {balance}, Total Lines to bet: {lines}, Total bet amount: {total_bet}.")

    slots = get_slot_machine_spin(ROWS, COLS, symbols)
    print_slot_machine(slots)


main()
