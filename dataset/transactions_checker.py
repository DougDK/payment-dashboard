import json

with open('transactions.json', 'r', encoding='utf-8') as f:
    transactions = json.load(f)
    print(f"Amount of transactions: {len(transactions)}")