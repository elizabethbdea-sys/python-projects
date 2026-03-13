# income tracker v3 -  List & Loops
print("💰 Monthly Income Tracker")
print("---------------------------")

# A list to store our income streams
income_sources = []
total = 0

# Loop to keep asking until user is done
while True: 
    name = input("Income source name (or 'done' to finish): ")

    if name == "done":
        break

    amount = float(input(f"Amount for {name}: $"))
    income_sources.append((name, amount))
    total += amount

    # Output
    print("--------------------------------")
    print("💰 Income Breackdown:")
    for source, amount in income_sources:
        print(f"{source}: ${amount}")

    print("-------------------------------")
    print(f"TOTAL: ${total}")
    print(f"Savings (20%): ${total * 0.20}")
    print(f"After savings: ${total * 0.80}")