Coins = 0
print("You have {} coins.".format(Coins))
Offer = input("Do you want another? yes or no: ")
while Offer == "yes":
    Coins = Coins + 1
    print("You have {} coins.".format(Coins))
    Offer = input("Do you want another? yes or no: ")
print("Bye")