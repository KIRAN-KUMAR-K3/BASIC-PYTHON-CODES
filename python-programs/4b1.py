roman_numbers = {
    "I": 1,
    "V": 5,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
int_value = 0

user_input = input("Enter Roman Numbers:").upper()

for i in range(len(user_input)):
    if user_input[i] in roman_numbers:
        if i + 1 < len(user_input) and roman_numbers[user_input[i]] < roman_numbers[user_input[i + 1]]:
            int_value -= roman_numbers[user_input[i]]
        else:
            int_value += roman_numbers[user_input[i]]
    else:
        print("Invalid input")
        quit()

print("The integer value is:", int_value)
