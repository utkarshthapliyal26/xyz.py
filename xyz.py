# Inventory list to store product records 
inventory = [] 
MAX_PRODUCTS = 100  # Maximum number of products allowed in inventory
# Function to insert a new product 
def insert_product(): 
    if len(inventory) >= MAX_PRODUCTS: 
        print("Inventory is full. Cannot insert more products. current products:", len(inventory)) 
        return
    sku = input("Enter SKU: ") 
 
    # Check for duplicate SKU 
    for item in inventory: 
        if item['sku'] == sku: 
            print("Product with this SKU already exists!") 
            return 
    name = input("Enter Product Name: ")
    if not name.strip():
        print("Invalid input. Product name cannot be empty.")
        return
 
    try:
        quantity = int(input("Enter Quantity: ")) 
    except ValueError: 
        print("Invalid input. Quantity must be a number.") 
        return 
    if quantity < 0: 
        print("Quantity cannot be negative.") 
        return 
 
 # Create product dictionary and add to inventory 
    product = {'sku': sku, 'name': name, 'quantity': quantity} 
    inventory.append(product) 
    print("Product inserted successfully.") 
# Function to display inventory 
def display_inventory(): 
    if not inventory: 
        print("Inventory is empty.") 
        return 
    print("\nCurrent Inventory:") 
    print("SKU\t\tProduct Name\t\tQuantity") 
    print("-----------------------------------------------") 
    for item in inventory: 
        print(f"{item['sku']}\t\t{item['name']}\t\t{item['quantity']}") 
        print()
def insert_Nproducts():
    try:
        count = int(input("How many products do you want to add? "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    for i in range(count):
        print(f"\n--- Product {i+1} ---")
        insert_product()
def Seach_Product_SKU():
    sku = input("Enter SKU to search: ")
    for item in inventory:
        if item['sku'] == sku:
            print(f"Product found: {item['name']} with quantity {item['quantity']}")
            return
    print("Product not found.")
def Search_Product_Name():
    name = input("Enter Product Name to search: ")
    for item in inventory:
        if item['name'].lower() == name.lower():
            print(f"Product found: SKU {item['sku']} with quantity {item['quantity']}")
            return
def Delete_Product():
    sku = input("Enter SKU of the product to delete: ")
    for item in inventory:
        if item['sku'] == sku:
            inventory.remove(item)
            print("Product deleted successfully.")
            return
    print("Product not found.")
def update_quantity():
    sku = input("Enter SKU of the product to update quantity for: ")
    for item in inventory:
        if item['sku'] == sku:
            try:
                new_quantity = int(input("Enter new quantity: "))
                if new_quantity < 0:
                    print("Quantity cannot be negative.")
                    return
                item['quantity'] = new_quantity
                print("Quantity updated successfully.")
                return
            except ValueError:
                print("Invalid input. Quantity must be a number.")
                return
# Main program loop 
def main(): 
    while True: 
        print("\nInventory Stock Manager") 
        print("1. Insert New Product") 
        print("2. Display Inventory") 
        print("3. Insert N Products")
        print("4. Serch Product by SKU")
        print("5. Search Product by Name") 
        print("6. Delete Product")
        print("7. Update Product Quantity")

        print("8. Exit")
         # Get user choice
        choice = input("Enter your choice (1-8): ") 
        if choice == '1': 
            insert_product() 
        elif choice == '2': 
            display_inventory()
        elif choice =='3':
            insert_Nproducts()
        elif choice == '4': 
            Seach_Product_SKU()
        elif choice == '5': 
            Search_Product_Name()
        elif choice == '6': 
            Delete_Product()
        elif choice == '7':
            update_quantity()
        elif choice == '8': 
            print("Exiting Inventory Manager.") 
            break 
        else:
            print("Invalid choice. Please select from 1 to 8.") 
# Start the program 
main()