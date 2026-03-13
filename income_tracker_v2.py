# income Tracker V2 - Interactive
print("💰 Wellcome to Your Monthly Income Tracker")
print("-------------------------------------------")

# Ask the user for input
tempered_ai = float(input("Tempered AI income: $"))
builders_tech = float(input("Builders Tech income: $"))
shopify = float(input("Shopifyincome: $"))
etsy = float(input("Etsy income: $"))

# Calculate
total = tempered_ai + builders_tech + shopify + etsy
savings = total *0.20

# Output
print("-------------------------------------------")
print("TOTAL:", total)
print("Savings (20%):", savings)
print("After savings:", total - savings)