shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

"""
def compute_bill(shopping_list):
    total = 0
    for item in shopping_list:
        total = total + prices[key]
    print(total)
"""
for price in prices:
    print(price)
