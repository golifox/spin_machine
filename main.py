import random


# import all constants from file
from config import *


def check_winnings(columns, lines, bet, values):
    """
    Function that find the same values in a row in random matrix
    and return how much money user wins, and list on winning lines
    Example return: 100, [1,2]

    """

    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    """
    Function that generate random matrix of spin
    and return matrix like list.
    
    """
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)

    return columns


def print_slot_machine(columns):
    """
    Function for representation spin matrix.

    """
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ") 
            else:
                print(column[row])  


def deposit():
    """
    Function to take input first user deposit. 

    """
    while True: 
        amount = input("What do you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number!")

    return amount


def get_number_of_lines():
    """
    Function to take user input how much lines he predict to win.

    """
    while True: 
        lines = input(f"Enter the number of lines to bet on (1-{str(MAX_LINES)})? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines!")
        else:
            print("Please enter a number!")

    return lines


def get_bet():
    """
    Function to get user input bet in $.
    
    """
    while True: 
        amount = input(f"Amount must be between ${MIN_BET} - ${MAX_BET}: ")
        if amount.isdigit():
            amount = int(amount)
            if 1 <= amount <= MAX_BET:
                break
            else:
                print("Enter a valid bet!")
        else:
            print("Please enter a number!")

    return amount


def spin(balance):
    """
    A main loop of the game.
    
    """
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print("You do not have enough to bet that amount, "
                  f"your current balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines}."
          f"Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, SYMBOLS)

    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, SYMBOL_VALUE)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)

    return winnings - total_bet


def main():
    """
    Main entry point.
    
    """
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to spin (q to exit)")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


if __name__ == "__main__":
    main()