def mimic(my_words:str, index:int) ->str:
    """Given a string my_words, returns the same string"""
    if len(my_words) < index + 1:
        return "Too high of an index"
    elif index < 0:
        return "Please enter a valid index"
    return my_words[index]

while True:
    mimic(input("Enter a word: "), int(input("Enter an index: ")))

print(mimic("hello"))