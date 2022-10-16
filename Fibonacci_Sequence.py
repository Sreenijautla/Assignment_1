# Write a Python program to get the Fibonacci series between 0 to 50
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34


num=int(input())
first_number=0
second_number=1
while num>second_number:
    print(second_number,end=" ")
    first_number,second_number = second_number,first_number+second_number