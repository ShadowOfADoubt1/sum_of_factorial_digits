FROM python:3.8

ADD sum_of_factorial_digits.py .

RUN pip install numpy

ENTRYPOINT ["python3", "./sum_of_factorial_digits.py"]