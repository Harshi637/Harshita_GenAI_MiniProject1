def add_item(item, cart=[]):
    cart.append(item)
    return cart

print("Given add_item Output:")
print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", cart=["bread"]))
print(add_item("eggs"))

def add_item_fixed(item, cart=None):
    if cart is None:
        cart = []

    cart.append(item)
    return cart

print("\nFixed add_item Output:")
print(add_item_fixed("apple"))
print(add_item_fixed("banana"))
print(add_item_fixed("eggs"))

def create_cart(owner, discount=0):
    return {"owner": owner,"items": [],"discount": discount}

def add_to_cart(cart, name, price, qty=1):
    item = {"name": name,"price": price,"qty": qty}

    cart["items"].append(item)


def update_price(price_tuple, new_price):

    try:
        price_tuple[0] = new_price

    except TypeError as e:
        print("\nTuple Modification Error:")
        print(e)

def calculate_total(cart):
    total = 0
    for item in cart["items"]:
        total += item["price"] * item["qty"]

    discount_amount = (cart["discount"] / 100) * total
    final_total = total - discount_amount

    return final_total

cart1 = create_cart("Aarav", discount=10)
cart2 = create_cart("Diya", discount=5)
add_to_cart(cart1, "Laptop", 50000, 1)
add_to_cart(cart1, "Mouse", 1000, 2)
add_to_cart(cart2, "Book", 500, 3)
add_to_cart(cart2, "Pen", 20, 5)

print("\nCustomer 1 Cart:")
print(cart1)
print("\nCustomer 2 Cart:")
print(cart2)

print("\nFinal Total for Aarav:", calculate_total(cart1))
print("Final Total for Diya:", calculate_total(cart2))

price_data = (500, "Book")
update_price(price_data, 700)
# price_data remains unchanged because tuples are immutable

# ---------------------------
# Discussion Points

# 1. Why is discount=0 safe but cart=[] dangerous?
# discount=0 is safe because integers are immutable.
# The value cannot be changed accidentally across function calls.
# cart=[] is dangerous because lists are mutable.
# The same list object gets reused in every function call.

# 2. What is the difference between rebinding and mutating?
# Rebinding:
# Assigning a variable to a completely new object.
# Mutating:
# Changing the contents of the SAME object.

# 3. Which of these are mutable?
# Mutable:
# list, dict, set
# Immutable:
# tuple, str, int


# 4. When you pass a list into a function and modify it,do changes reflect outside? Why?
# Yes.
# Lists are mutable and Python passes references to objects.
# So modifying the list inside the function changes the
# original list outside the function as well.