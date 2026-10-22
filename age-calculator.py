
from datetime import date

print("===== Age Calculator =====")

while True:
    try:
        birth_year = int(input("Enter your birth year: "))
        current_year = date.today().year

        if birth_year > current_year:
            print("Invalid year! You cannot be born in the future.")

        elif birth_year < 1900:
            print("Please enter a valid birth year.")

        else:
            age = current_year - birth_year

            print("\n===== Your Age Details =====")
            print("Birth Year:", birth_year)
            print("Current Year:", current_year)
            print("Your Age:", age, "years")

            print("Approximate Age in Months:", age * 12)
            print("Approximate Age in Days:", age * 365)

        again = input("\nCalculate again? (yes/no): ").lower()

        if again != "yes":
            print("Thank you for using Age Calculator!")
            break

    except ValueError:
        print("Invalid input! Please enter a number.")
