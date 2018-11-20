string = input("Enter text: ").upper()

for text in string:
    if text == "A":
        string = string.replace("A", "4")
    elif text == "E":
        string = string.replace("E", "3")
    elif text == "G":
        string = string.replace("G", "6")
    elif text == "L":
        string = string.replace("L", "1")
    elif text == "O":
        string = string.replace("O", "0")
    elif text == "S":
        string = string.replace("S", "5")
    elif text == "T":
        string = string.replace("T", "7")


print(string)

