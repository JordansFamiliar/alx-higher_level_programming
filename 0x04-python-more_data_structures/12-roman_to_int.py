def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                    'M': 1000}
    decimal = 0
    prev = 0

    for symbol in reversed(roman_string):
        value = roman_values[symbol]
        if value < prev:
            decimal -= value
        else:
            decimal += value
        prev = value
    return (decimal)
