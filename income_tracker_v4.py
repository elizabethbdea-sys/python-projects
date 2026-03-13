# Income Tracket V4 - Functions

def get_income():
    """Collects income source from user"""
    sources = []
    total = 0

    while True:
        name = input("income source (or 'done' to finish): ")
        if name == "done":
            break
        amount = float(input(f"Amount for {name}: $"))
        sources.append((name, amount))
        total += amount

    return sources, total
    
def show_report(sources, total):
    """Prints the income report"""
    print("\n💰 Income Breakdown:")
    print("--------------------")
    for name, amount in sources:
        print(f" {name}: ${amount}")
    print("----------------------")
    print(f"TOTAL:         ${total}")
    print(f"savings (20%): ${total * 0.20}")
    print(f"After savings: ${total * 0.80}")

# --- Run the program ---
print("💰 Monthly Income Tracker v4")
print("----------------------------")
sources, total = get_income()
show_report(sources, total)