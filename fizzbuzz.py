import os 


def clear_terminal_screen():
    return os.system("clear || cls")


def menu():
    clear_terminal_screen()

    user_options = {
        'fizz_option': [number for number in range(0, 51) if number % 3 == 0],
        'buzz_option': [number for number in range(0, 51) if number % 5 == 0],
        'fizzbuzz_option': [number for number in range(0, 51) if number % 5 == 0 and number % 3 == 0]
    }

    while True:
        user_input = input(
            "\n- Enter 'fizz' to print numbers divisible by 3"
            "\n- Enter 'buzz' to print numbers divisible by 5"
            "\n- Enter 'fizzbuzz' to print numbers divisible by 3 AND 5"
            "\n- Enter 'all' to print every number"
            "\n- Enter 'clear' to clear the terminal screen"
            "\n- Enter 'quit' to exit the program: "
        ).lower()

        if user_input == 'fizzbuzz':
            clear_terminal_screen()
            print(f"\nPrinting numbers divisible by 3 and 5:\n{user_options['fizzbuzz_option']}")
        elif user_input == 'fizz':
            clear_terminal_screen()
            print(f"\nPrinting numbers divisible by 3:\n{user_options['fizz_option']}")
        elif user_input == 'buzz':
            clear_terminal_screen()
            print(f"\nPrinting numbers divisible by 5:\n{user_options['buzz_option']}")
        elif user_input == 'all':
            for number in range(0, 51):
                if number % 5 == 0 and number % 3 == 0:
                    print(f"{number} - FizzBuzz")
                elif number % 3 == 0:
                    print(f"{number} - Fizz")
                elif number % 5 == 0:
                    print(f"{number} - Buzz")
                else:
                    print(number)
        elif user_input == 'clear':
            clear_terminal_screen()
        elif user_input == 'quit':
            clear_terminal_screen()
            print("\nThank you for using FizzBuzz. Have a great day.\n")
            break
        else:
            clear_terminal_screen()
            print("Unknown command. Enter valid options only.")


menu()