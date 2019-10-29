import random
import math


class CowsAndBullNoRepeat:
    def __init__(self):
        self.num = self.generate_random_number_list()
        self.cows = 0
        self.bulls = 0

    def generate_random_number_list(self):
        random_list = [random.randint(1, 9)]
        for i in range(3):
            current_digit = random.randint(0, 9)
            while current_digit in random_list:
                current_digit = random.randint(0, 9)
            random_list.append(current_digit)
        return random_list

    def generate_digits_list(self, number_to_divide):
        if number_to_divide < 1000:
            raise ValueError("The number is too small")
        elif number_to_divide > 9999:
            raise ValueError("The number is too large")
        first_digit = math.floor(number_to_divide/1000)
        second_digit = math.floor(number_to_divide / 100) - first_digit * 10
        third_digit = math.floor(number_to_divide / 10) - second_digit * 10 - first_digit * 100
        fourth_digit = number_to_divide - third_digit*10 - second_digit * 100 - first_digit * 1000
        four_digit_list = [first_digit, second_digit, third_digit, fourth_digit]
        return four_digit_list

    def check_num(self, number, position):
        if number == self.num[position]:
            self.cows += 1
        elif number in self.num:
            self.bulls += self.num.count(number)

    def print_headers(self):
        print("Welcome to the Cows and Bulls Game!")
        print("Enter a number:")

    def reset_cows_and_bulls(self):
        self.cows = 0
        self.bulls = 0

    def game_loop(self):
        try:
            guessed_number = input(">>>")
            if len(set(guessed_number)) != 4:
                raise ValueError("You cannot enter a number with duplicate digits")
            if guessed_number.isdigit():
                guessed_number = int(guessed_number)
                guessed_number_list = self.generate_digits_list(guessed_number)
                self.reset_cows_and_bulls()
                for i in range(len(guessed_number_list)):
                    self.check_num(guessed_number_list[i], i)
                print(str(self.cows) + " cows, " + str(self.bulls) + " bulls")
            else:
                raise ValueError("The value entered was not an integer.")

        except ValueError as err:
            print("Incorrect input, please enter a positive 4 digit integer.")
            print(str(err))

    def start_game(self):
        self.print_headers()
        while self.cows < 4:
            self.game_loop()


if __name__ == "__main__":
    newGame = CowsAndBullNoRepeat()
    newGame.start_game()
