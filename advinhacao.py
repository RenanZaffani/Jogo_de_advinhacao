import random


def guessing():
    print("Welcome to the Guessing Game!")

    secret_number = random.randrange(1, 101)
    total_attempts = 0
    points = 1000

    print("What level do you want?")
    print("1 - Easy")
    print("2 - Average")
    print("3 - Hard")
    level = int(input("Answer: "))

    if level == 1:
        total_attempts = 20
    elif level == 2:
        total_attempts = 10
    elif level == 3:
        total_attempts = 5
    else:
        print("Wrong answer.")

    for round in range(1, total_attempts + 1):
        print(" ")

        print(f"Attempt {round} out of {total_attempts}.")
        user_number_str = input("Type your number between 1 and 100: ")
        print(f"You was type {user_number_str}.")
        user_number = int(user_number_str)

        if user_number < 1 or user_number > 100:
            print("You need type a number between 1 and 100.")
            continue

        right = user_number == secret_number
        bigger = user_number > secret_number
        smaller = user_number < secret_number

        if right:
            print("You're right.")
            print(f"You did {points} points.")
            break
        else:
            if bigger:
                print("You're wrong. Your number is bigger than the secret number.")
            elif smaller:
                print("You're wrong. The secret number is bigger than your number.")
            lost_points = abs(secret_number - user_number)
            points = points - lost_points

    print("End Game.")


if __name__ == "__main__":
    guessing()
