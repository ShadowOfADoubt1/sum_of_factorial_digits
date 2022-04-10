# Sum of Factorial Digits

**Program output:**
The program takes a whole number, calculates its factorial and sums the digits of that factorial. 

**Functions:**
1. SumOfDigits(str_input): calculates the factorial of the given whole number and returns the sum of the digits
    
2. StringToInt(str_input): converts a string to an integer without casting
    
3. IntToString(int_input): converts a integer to string without casting
    
4. SeperateDigits(str_input): seperates the given string into an array of its characters and converts them to integers without casting

**How it works:**
The sum_of_factorial_digits.py is the python script that takes a given whole number and calculates the sum of its factorial's digits with SumOfDigits. It takes it's input from the commandline and use StringToInt to convert it to an integer. Then it uses numpy to calculate the factorial of the whole number. Once it has the factorial it uses IntToString to convert it into a string. Then with SeperateDigits the string is converted into an array of characters and then convers that array to an array of integers. Then using numpy the program sums all thge elements of the array of integers and returns it as the output. For non-whole number arguments the program catches the error and returns **Argument must be a whole number***.

Dockerfile is used to create the Docker container. It establishes the version of python that should be used and adds the given python script. After that it installs the neccesary dependencies and runs **python3 ./sum_of_factorial_digits.py whole_number_argument**. This will return the expected outcome.

