Bill = (float(input("Total bill amount? ")))
Service = (input("Level of Service? good, fair, bad: "))
good = (float(0.20 * Bill))
fair = (float(0.15 * Bill))
bad = (float(0.10 * Bill))
Good_Bill = (float(Bill + good))
Fair_Bill = (float(Bill + fair))
Bad_Bill = (float(Bill + bad))
if Service == "good":
    print("Tip amount: ", "{:.2f}".format(good))
    print("Total amount: ", "{:.2f}".format(Good_Bill))
elif Service == "fair":
    print("Tip amount: ", "{:.2f}".format(fair))
    print("Total amount: ", "{:.2f}".format(Fair_Bill))
elif Service == "bad":
    print("Tip amount: ", "{:.2f}".format(bad))
    print("Total amount: ", "{:.2f}".format(Bad_Bill))