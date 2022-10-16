# Write a Python program that accepts a word from the user and reverse it.
# Sample Test Case
# Input : Edyoda
# output: adoydE


word=input("Input : ")
empty_string=''
for i in word:
  empty_string=i+empty_string
print("output:",empty_string)