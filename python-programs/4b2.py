def roman_to_int(roman):
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    int_value = 0
    prev_value = 0
    for numeral in reversed(roman):
        current_value = roman_dict.get(numeral, 0)
        if current_value < prev_value:
            int_value -= current_value
        else:
            int_value += current_value
        
        prev_value = current_value
    return int_value
user_input = input("Enter Roman Numerals: ").upper()
try:
    integer_value = roman_to_int(user_input)
    print(f"The integer value of {user_input} is {integer_value}")
except ValueError:
    print("Invalid input. Please enter a valid Roman numeral.")
