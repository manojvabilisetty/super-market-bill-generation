from datetime import datetime

# Product Database
products = {
    1: ("Rice", 50),
    2: ("Sugar", 45),
    3: ("Milk", 30),
    4: ("Bread", 25),
    5: ("Oil", 120),
    6: ("Soap", 35),
    7: ("Biscuits", 20),
    8: ("Tea Powder", 80)
}

cart = []
total = 0

# Customer Details
print("===================================")
print("   SUPER MARKET BILLING SYSTEM")
print("===================================")

customer_name = input("Enter Customer Name : ")
mobile = input("Enter Mobile Number : ")

# Current Date and Time
now = datetime.now()
date_time = now.strftime("%d-%m-%Y %H:%M:%S")

# Display Products
print("\nAvailable Products")
print("-----------------------------------")
print("ID\tProduct\t\tPrice")
print("-----------------------------------")

for pid, data in products.items():
    print(f"{pid}\t{data[0]}\t\t₹{data[1]}")

# Add Products
while True:
    choice = int(input("\nEnter Product ID (0 to Finish): "))

    if choice == 0:
        break

    if choice in products:
        qty = int(input("Enter Quantity: "))

        name, price = products[choice]
        amount = price * qty

        cart.append([name, price, qty, amount])
        total += amount

        print("Product Added Successfully!")
    else:
        print("Invalid Product ID!")

# GST Calculation
gst = total * 0.05
grand_total = total + gst

# Print Bill
print("\n")
print("=" * 50)
print("            SUPER MARKET BILL")
print("=" * 50)

print("Customer Name :", customer_name)
print("Mobile Number :", mobile)
print("Date & Time   :", date_time)

print("-" * 50)
print("Product\tPrice\tQty\tAmount")
print("-" * 50)

for item in cart:
    print(
        f"{item[0]}\t₹{item[1]}\t{item[2]}\t₹{item[3]}"
    )

print("-" * 50)
print(f"Subtotal      : ₹{total}")
print(f"GST (5%)      : ₹{gst:.2f}")
print(f"Grand Total   : ₹{grand_total:.2f}")
print("=" * 50)
print("       THANK YOU! VISIT AGAIN")
print("=" * 50)