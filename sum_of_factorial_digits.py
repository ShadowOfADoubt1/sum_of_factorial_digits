import sys
import numpy


def SumOfDigits(
                str_input):
    """Sums the digits of a factorial"""
    int_number = StringToInt(str_input) # Convert string input to an integer
    int_factorial = numpy.math.factorial(int_number) # Calculates factorial of given integer
    str_factorial = IntToString(int_factorial) # Converts factorial to a string
    ary_digits = SeperateDigits(str_factorial) # Seperates a string into an array of its characters and converts them to integers
    int_digits_sum = numpy.sum(ary_digits) # Sums the the contents of an array of integers
    return int_digits_sum


def StringToInt(
                str_input):
    """Takes a string and converts it to an integer without type casting"""
    ary_int = numpy.array(str_input, dtype=int)
    return ary_int


def IntToString(
                int_input):
    """Takes a integer and converts it to a string without type casting"""
    ary_string = numpy.array([int_input], dtype=str)
    return ary_string[0]


def SeperateDigits(
                    str_input):
    """Returns an array of a string's characters converted to integers"""
    ary_digits = numpy.array(list(str_input), dtype=int)
    return ary_digits


if __name__ == '__main__':
    try:
        str_cmd_argument = sys.argv[1] # Takes commandline argument
        int_sum_of_digits = SumOfDigits(str_cmd_argument) # Calculates the sum of the digits of given number's factorial
        print(int_sum_of_digits) # Prints result
    except ValueError: # Catches invalid parameters
        print("Argument must be a whole number") # Prints reason for error
