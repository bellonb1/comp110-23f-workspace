"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730656976"

five_input = input("Enter a 5-character word: ")
if len(five_input) != 5:
    print("Error: Word must contain 5 characters")
    exit()

char_input = input("Enter a single character: ")
if len(char_input) != 1:
    print("Error: Characer must be a single character.")
    exit()


print("Searching for " + char_input + " in " + five_input)
count = 0
for i in range(len(five_input)):
    if char_input == five_input[i]:
        count += 1
        print(char_input + " found at index " + str(i))
if count > 1:
    print(str(count) + " instances of " + char_input + " found in " + five_input)
elif count > 0:
    print("1 instance of " + char_input + " found in " + five_input)
else:
    print("No instances of " + char_input + " found in " + five_input)