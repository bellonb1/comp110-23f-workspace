"""Hit web game Wordle with one try."""

__author__:str = "730656976"

secret:str = "python"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

guess = input("What is your " + str(len(secret)) + "-letter guess? ")
while len(guess) != 6:
    guess = input("That was not " + str(len(guess))+ " letters! Try again: ")

index:int = 0
box_string:str = ""

while index < len(secret):
    nested_index:int = 0
    if guess[index] == secret[index]:
        box_string += GREEN_BOX
    else:
        is_guessed:bool = False
        while not is_guessed and nested_index < len(secret):
            if guess[index] == secret[nested_index]:
                is_guessed = True
            else:
                nested_index+=1
        if is_guessed:
            box_string += YELLOW_BOX
        else:
            box_string += WHITE_BOX
    index+=1

print(box_string)

if guess == secret:   
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")