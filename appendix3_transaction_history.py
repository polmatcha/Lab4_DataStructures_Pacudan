# Student-specific inputs
LAST_NAME = "Pacudan"
STUDENT_ID = "TUPM-26-1859"
FAVORITE_ARTIST = "The 1975"
SEED_NUM = int(STUDENT_ID[-1])  # 9

# Use alphabet positions from the artist's letters (A=1, ..., Z=26).
ARTIST_POSITIONS = [
    ord(char.upper()) - ord("A") + 1
    for char in FAVORITE_ARTIST
    if char.isalpha()
]

from collections import Counter, defaultdict

CUSTOMERS = [f"{LAST_NAME}-C{i}" for i in range(1, 6)]
PRODUCT_PRICES = {
    "NOTEBOOK": 35,
    "PEN": 15,
    "USB": 250,
    "HEADPHONES": 450,
    "CALCULATOR": 300
}
PRODUCTS = list(PRODUCT_PRICES.keys())

transactions = []
for i in range(10):
    customer = CUSTOMERS[i % len(CUSTOMERS)]
    product = PRODUCTS[(i * 2) % len(PRODUCTS)]
    artist_value = ARTIST_POSITIONS[i % len(ARTIST_POSITIONS)]
    quantity = 1 + ((SEED_NUM + artist_value + i) % 5)
    transactions.append({
        "customer": customer,
        "product": product,
        "quantity": quantity,
        "price_each": PRODUCT_PRICES[product]
    })

# Include a repeated customer-product transaction.
transactions.append(transactions[0].copy())

for transaction in transactions:
    transaction["total"] = transaction["quantity"] * transaction["price_each"]

print("=== APPENDIX 3: TRANSACTION HISTORY ANALYZER ===")
print("\n1. GENERATED TRANSACTION RECORDS")
for transaction in transactions:
    print(transaction)

organized = defaultdict(list)
for transaction in transactions:
    organized[(transaction["customer"], transaction["product"])].append(transaction)

print("\n2. ORGANIZED TRANSACTION DATA")
for (customer, product), items in sorted(organized.items()):
    print(f"{customer} | {product}: {len(items)} transaction(s), "
          f"quantities={[x['quantity'] for x in items]}, "
          f"total value=PHP {sum(x['total'] for x in items)}")

purchase_keys = [(t["customer"], t["product"]) for t in transactions]
purchase_counts = Counter(purchase_keys)
repeated = {key: count for key, count in purchase_counts.items() if count > 1}

print("\n3. REPEATED / DISTINCT PURCHASES")
print(f"Repeated customer-product pairs: {repeated}")
print(f"Distinct customers: {len(set(t['customer'] for t in transactions))}")
print(f"Distinct products purchased: {len(set(t['product'] for t in transactions))}")

print("\n4. TRANSACTION VALUES")
for transaction in transactions:
    print(f"{transaction['customer']} bought {transaction['quantity']} "
          f"{transaction['product']}(s): PHP {transaction['total']}")

print("\n5. CUSTOMER SUMMARIES")
for customer in CUSTOMERS:
    items = [t for t in transactions if t["customer"] == customer]
    print(f"{customer}: {len(items)} transaction(s), "
          f"total spent=PHP {sum(t['total'] for t in items)}")

print("\n6. PRODUCT SUMMARIES")
for product in PRODUCTS:
    items = [t for t in transactions if t["product"] == product]
    print(f"{product}: {sum(t['quantity'] for t in items)} item(s), "
          f"revenue=PHP {sum(t['total'] for t in items)}")

print("\n7. ORDERED RESULTS (CUSTOMER, PRODUCT)")
for transaction in sorted(transactions, key=lambda t: (t["customer"], t["product"])):
    print(transaction)

grand_total = sum(t["total"] for t in transactions)
total_items = sum(t["quantity"] for t in transactions)
print("\n8. OVERALL TRANSACTION SUMMARY")
print(f"Total transaction records: {len(transactions)}")
print(f"Total items sold: {total_items}")
print(f"Grand total sales: PHP {grand_total}")
print(f"Repeated customer-product pairs: {len(repeated)}")



# FINAL OUTPUT: FINAL CONSOLIDATED TRANSACTION REPORT

from collections import defaultdict, Counter

print("\n" + "=" * 65)
print("FINAL CONSOLIDATED TRANSACTION REPORT")
print("=" * 65)

# 1. Consolidate transactions by customer and product
consolidated = defaultdict(lambda: {
    "quantity": 0,
    "transaction_count": 0,
    "total_value": 0
})

for transaction in transactions:
    key = (transaction["customer"], transaction["product"])
    consolidated[key]["quantity"] += transaction["quantity"]
    consolidated[key]["transaction_count"] += 1
    consolidated[key]["total_value"] += transaction["total"]

print("\n1. CONSOLIDATED CUSTOMER-PRODUCT DATA")
for (customer, product), data in sorted(consolidated.items()):
    print(f"Customer: {customer} | Product: {product}")
    print(f"  Transactions: {data['transaction_count']}")
    print(f"  Total Quantity: {data['quantity']}")
    print(f"  Total Value: PHP {data['total_value']}")

# 2. Total sales by customer
print("\n2. TOTAL SALES BY CUSTOMER")
for customer in CUSTOMERS:
    customer_total = sum(
        t["total"] for t in transactions
        if t["customer"] == customer
    )
    print(f"{customer}: PHP {customer_total}")

# 3. Total sales by product
print("\n3. TOTAL SALES BY PRODUCT")
for product in PRODUCTS:
    product_total = sum(
        t["total"] for t in transactions
        if t["product"] == product
    )
    quantity_sold = sum(
        t["quantity"] for t in transactions
        if t["product"] == product
    )
    print(
        f"{product}: {quantity_sold} item(s), "
        f"PHP {product_total}"
    )

# 4. Identify repeated customer-product purchases
purchase_counts = Counter(
    (t["customer"], t["product"]) for t in transactions
)
repeated_purchases = {
    key: count
    for key, count in purchase_counts.items()
    if count > 1
}

print("\n4. REPEATED CUSTOMER-PRODUCT PURCHASES")
if repeated_purchases:
    for (customer, product), count in sorted(repeated_purchases.items()):
        print(
            f"{customer} purchased {product} "
            f"{count} times"
        )
else:
    print("No repeated customer-product purchases found.")

# 5. Overall consolidated summary
grand_total = sum(t["total"] for t in transactions)
total_quantity = sum(t["quantity"] for t in transactions)

print("\n5. OVERALL TRANSACTION SUMMARY")
print(f"Student: {LAST_NAME}")
print(f"Student ID: {STUDENT_ID}")
print(f"Total Transaction Records: {len(transactions)}")
print(f"Distinct Customers: {len(set(t['customer'] for t in transactions))}")
print(f"Distinct Products: {len(set(t['product'] for t in transactions))}")
print(f"Total Items Sold: {total_quantity}")
print(f"Repeated Customer-Product Pairs: {len(repeated_purchases)}")
print(f"Grand Total Sales: PHP {grand_total}")
print("=" * 65)
print("END OF FINAL CONSOLIDATED TRANSACTION REPORT")
print("=" * 65)
