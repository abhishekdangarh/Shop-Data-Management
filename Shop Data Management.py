items = []
def calculate_grade(price):
    if price <= 1000:
        return "0"
    grades = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    grade_number = int((price - 1001) // 200)
    if grade_number < len(grades):
        return grades[grade_number]
    return "Z+"

def add_item():
    item_id = input("Enter Item ID: ")
    name = input("Enter Item Name: ")
    price = float(input("Enter Price: ₹"))
    quantity = int(input("Enter Stock Quantity: "))
    grade = calculate_grade(price)
    item = {
        "id": item_id,
        "name": name,
        "price": price,
        "quantity": quantity,
        "grade": grade
    }
    items.append(item)
    print("\nItem added successfully!")
    print("Grade:", grade)

def display_items():
    print("\n========== AVAILABLE ITEMS ==========")
    available = False
    for item in items:
        if item["quantity"] > 0:
            available = True
            print("------------------------------------------")
            print("Item ID   :", item["id"])
            print("Item Name :", item["name"])
            print("Price     : ₹", item["price"])
            print("Stock     :", item["quantity"])
            print("Grade     :", item["grade"])
    if available == False:
        print("No items available in stock.")

def add_stock():
    item_id = input("Enter Item ID: ")
    quantity = int(input("Enter quantity to add: "))
    for item in items:
        if item["id"] == item_id:
            item["quantity"] += quantity
            print("\nStock added successfully!")
            print("Current Stock:", item["quantity"])
            return
    print("Item not found.")

def sell_item():
    item_id = input("Enter Item ID: ")
    quantity = int(input("Enter quantity to sell: "))
    for item in items:
        if item["id"] == item_id:
            if item["quantity"] >= quantity:
                item["quantity"] -= quantity
                print("\nSale successful!")
                print("Remaining Stock:", item["quantity"])
            else:
                print("Not enough stock available.")
            return
    print("Item not found.")

def search_by_grade():
    grade = input("Enter Grade: ").upper()
    found = False
    print("\n========== ITEMS OF GRADE", grade, "==========")
    for item in items:
        if item["grade"] == grade and item["quantity"] > 0:
            print("------------------------------------------")
            print("ID       :", item["id"])
            print("Name     :", item["name"])
            print("Price    : ₹", item["price"])
            print("Stock    :", item["quantity"])
            found = True
    if found == False:
        print("No available items found.")

def stock_details():
    print("\n========== COMPLETE STOCK DETAILS ==========")
    if len(items) == 0:
        print("No stock available.")
        return
    total_items = 0
    total_value = 0
    for item in items:
        value = item["price"] * item["quantity"]
        print("------------------------------------------")
        print("Item ID   :", item["id"])
        print("Item Name :", item["name"])
        print("Price     : ₹", item["price"])
        print("Quantity  :", item["quantity"])
        print("Grade     :", item["grade"])
        print("Stock Value: ₹", value)
        total_items += item["quantity"]
        total_value += value
    print("------------------------------------------")
    print("Total Quantity :", total_items)
    print("Total Stock Value: ₹", total_value)
while True:
    print("\n==========================================")
    print("       SHOP STOCK MANAGEMENT SYSTEM")
    print("==========================================")
    print("1. Add New Item")
    print("2. List Available Items")
    print("3. Add Stock")
    print("4. Sell Item")
    print("5. Search by Grade")
    print("6. Complete Stock Details")
    print("7. Exit")
    choice = input("\nEnter your choice: ")
    if choice == "1":
        add_item()
    elif choice == "2":
        display_items()
    elif choice == "3":
        add_stock()
    elif choice == "4":
        sell_item()
    elif choice == "5":
        search_by_grade()
    elif choice == "6":
        stock_details()
    elif choice == "7":
        print("\nThank you for using Shop Stock Management System!")
        break
    else:
        print("\nInvalid choice! Please enter 1-7.")