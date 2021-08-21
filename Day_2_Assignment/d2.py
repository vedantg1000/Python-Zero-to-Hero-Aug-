# Day 2 Assignment: Take a string input and print the number of occurrences of each character.

string = input("Enter any String: ")
for x in string:
    print(x, "Ocurred", string.count(x), "times")
