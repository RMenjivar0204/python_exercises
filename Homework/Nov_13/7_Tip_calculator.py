Bill = float(input("Total bill amount? "))
Service = input("Level of service? good, fair, or bad:  ")
good = float(0.20 * Bill)
fair = float(0.15 * Bill)
bad = float(0.10 * Bill)
good_Tip = float(good + Bill)
fair_Tip = float(fair + Bill)
bad_Tip = float(bad + Bill)
if Service == "good":
    print("Tip amount: {:0.2f}".format(good))
    print("Total amount: {:0.2f}".format(good_Tip))
elif Service == "fair":
    print("Tip amount: {:0.2f}".format(fair))
    print("Total amount: {:0.2f}".format(fair_Tip))
elif Service == "bad":
    print("Tip amount: {:0.2f}".format(bad))
    print("Total amount: {:0.2f}".format(bad_Tip))