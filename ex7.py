total_bill = float(input("Total bill amount? "))
service = input("Level of service? ").lower()
good = float(0.20 * total_bill)
fair = float(0.15 * total_bill)
bad = float(0.10 * total_bill)
good_bill = float(good + total_bill)
fair_bill = float(fair + total_bill)
bad_bill = float(bad + total_bill)
if service == "good":
    print("Tip amount: {:0.2f}".format(good))
    print("Total amount: {:0.2f}".format(good_bill))
if service == "fair":
    print("Tip amount: {:0.2f}".format(fair))
    print("Total amount: {:0.2f}".format(fair_bill))
if service == "bad":
    print("Tip amount: {:0.2f}".format(bad))
    print("Total amount: {:0.2f}".format(bad_bill))
