# Imperative
# here, we define the product names and prices
products = {
    "coca cola": 150,
    "pepsi": 100,
    "sprite": 75,
    "prime" : 35,
    "cobra" : 50
}

# this is the function to display available products and their costs
def display_products():
    print("Available Products:")
    for product, price in products.items():
        print(f"{product.capitalize()}: ₱{price:.2f}")

# Function to simulate/start the vending machine
def vending_machine():
    #this loop keeps running til the customer chooses to stop
    while True:
        print("\nSODA Vending Machine")
        print("1. Select product")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1": #if the customer chooses to select a product, this will be prompted
            display_products()
            product_choice = input("Enter the product name: ").lower() #the user will be asked to input the name of the product they want to buy
            if product_choice in products:
                customer_money = float(input("Please insert your money: ")) # if the product is present in the list, the system would ask for the user to input the money or amount
                if customer_money >= products[product_choice]: #if the money is greater than the cost of the product, this will be prompted
                    print(f"Dispensing {product_choice}...")
                    change = customer_money - products[product_choice]
                    print(f"Thank you! Please take your change: ₱{change:.2f}")
                    customer_money = 0.0
                else:
                    print("Insufficient Amount!") #if not, this will be prompted
            else:
                print("Product Unavailable") # if the product is not in the list, this will be prompted
        elif choice == "2": # if the user chose to stop the transaction, this will be prompted
            print("Exiting...")
            break
        else:
            print("Invalid choice!") # if the user have input the wrong number (neither 1 or 2) this will be prompted

# Run the vending machine by calling the function
vending_machine()
