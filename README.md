# Sum of Factorial Digits

**Program output:**
The program takes a whole number, calculates its factorial and sums the digits of that factorial. 

**Functions**
1. SumOfDigits(str_input): calculates the factorial of the given whole number and returns the sum of the digits
    
2. StringToInt(str_input): converts a string to an integer without casting
    
3. IntToString(int_input): converts a integer to string without casting
    
4. SeperateDigits(str_input): seperates the given string into an array of its characters and converts them to integers without casting

**How it works**
1. sum_of_factorial_digits.py is the python script that takes a given whole number and calculates the sum of its factorial's digits with SumOfDigits. It takes it's input from the commandline and use StringToInt to convert it to an integer. Then it uses numpy to calculate the factorial of the whole number. Once it has the factorial it uses IntToString to convert it into a string. Then with SeperateDigits the string is converted into an array of characters and then convers that array to an array of integers. Then using numpy the program sums all thge elements of the array of integers and returns it as the output. For non-whole number arguments the program catches the error and returns **Argument must be a whole number**.

2. Dockerfile is used to create the Docker container. It establishes the version of python that should be used and adds the given python script. After that it installs the neccesary dependencies and runs **python3 ./sum_of_factorial_digits.py whole_number_argument**. This will return the expected outcome.

**How to run it**
1. From tarball:
    a) Extract tarball into a work directory
    b) Build Docker container by running **sudo docker build -t factorial-digits work_directory**
    c) Then run **sudo docker run --rm factorial-digits whole_number_argument** to get a result
3. From git:
    a) Clone or download git repo
    b) Extract repo if you downloaded it as a zip file into a work directory
    c) Build Docker container by running **sudo docker build -t factorial-digits work_directory**
    d) Then run **sudo docker run --rm factorial-digits whole_number_argument** to get a result

