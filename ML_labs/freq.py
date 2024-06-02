from itertools import combinations

def find_frequent_itemsets(transactions, min_support):
    itemsets = {}
    num_transactions = len(transactions)

    # Считаем частоту каждого элемента
    for transaction in transactions:
        for item in transaction:
            if item in itemsets:
                itemsets[item] += 1
            else:
                itemsets[item] = 1

    # Фильтруем элементы, у которых поддержка меньше минимальной
    itemsets = {item: support for item, support in itemsets.items() if support >= min_support}

    frequent_itemsets = [{item} for item in itemsets.keys()]
    print(frequent_itemsets)
    # Поиск частых наборов размера k
    k = 2
    while frequent_itemsets:
        new_frequent_itemsets = []
        for itemset1 in frequent_itemsets:
            for itemset2 in frequent_itemsets:
                if len(itemset1.union(itemset2)) == k and itemset1 != itemset2:
                    new_itemset = itemset1.union(itemset2)
                    support = sum(1 for transaction in transactions if new_itemset.issubset(transaction)) / num_transactions
                    if support >= min_support and new_itemset not in new_frequent_itemsets:
                        new_frequent_itemsets.append(new_itemset)
        frequent_itemsets = new_frequent_itemsets
        k += 1

    return itemsets, frequent_itemsets

def generate_rules(itemsets, frequent_itemsets, min_confidence):
    rules = []
    for itemset in frequent_itemsets:
        for i in range(1, len(itemset)):
            for combination in combinations(itemset, i):
                antecedent = set(combination)
                consequent = itemset.difference(antecedent)
                confidence = itemsets[itemset] / itemsets[antecedent]
                if confidence >= min_confidence:
                    rules.append((antecedent, consequent, confidence))
    return rules

# Пример использования
transactions = [
    {'молоко', 'хлеб', 'сыр'},
    {'молоко', 'хлеб', 'яйца'},
    {'молоко', 'хлеб'},
    {'молоко', 'яйца'},
    {'молоко', 'хлеб', 'сыр', 'яйца'},
    {'хлеб', 'сыр'}
]

min_support = 0.3
min_confidence = 0.1

itemsets, frequent_itemsets = find_frequent_itemsets(transactions, min_support)
rules = generate_rules(itemsets, frequent_itemsets, min_confidence)

print(itemsets)
print(frequent_itemsets)

print("Frequent Itemsets:")
for itemset, support in itemsets.items():
    print(f"{itemset}: {support}")

print("\nAssociation Rules:")
for antecedent, consequent, confidence in rules:
    print(f"{antecedent} -> {consequent} (Confidence: {confidence})")
