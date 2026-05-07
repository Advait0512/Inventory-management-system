import mysql.connector

# DB CONNECTION
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Enter_your_Password",# its generally 12345678 or admin123
    database="inventory_db"
)

cursor = conn.cursor()

# ---------------------------
# ADD PRODUCT
# ---------------------------
def add_product():
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    threshold = int(input("Enter minimum threshold: "))

    query = "INSERT INTO products (name, quantity, price, threshold) VALUES (%s, %s, %s, %s)"
    values = (name, quantity, price, threshold)

    cursor.execute(query, values)
    conn.commit()
    print("✅ Product added successfully!\n")


# ---------------------------
# VIEW PRODUCTS
# ---------------------------
def view_products():
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()

    print("\n📦 Inventory:")
    for row in rows:
        print(row)
    print()


# ---------------------------
# UPDATE STOCK
# ---------------------------
def update_stock():
    product_id = int(input("Enter product ID: "))
    new_quantity = int(input("Enter new quantity: "))

    query = "UPDATE products SET quantity = %s WHERE product_id = %s"
    cursor.execute(query, (new_quantity, product_id))
    conn.commit()

    print("🔄 Stock updated!\n")


# ---------------------------
# DELETE PRODUCT
# ---------------------------
def delete_product():
    product_id = int(input("Enter product ID to delete: "))

    cursor.execute("DELETE FROM products WHERE product_id = %s", (product_id,))
    conn.commit()

    print("🗑️ Product deleted!\n")


# ---------------------------
# LOW STOCK ALERT
# ---------------------------
def check_low_stock():
    cursor.execute("SELECT name, quantity, threshold FROM products WHERE quantity < threshold")
    rows = cursor.fetchall()

    if rows:
        print("\n⚠️ Low Stock Alert:")
        for row in rows:
            print(f"{row[0]} is low! Quantity: {row[1]}")
    else:
        print("\n✅ All stocks are sufficient.\n")


# ---------------------------
# MENU
# ---------------------------
def menu():
    while True:
        print("\n===== INVENTORY SYSTEM =====")
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Stock")
        print("4. Delete Product")
        print("5. Check Low Stock")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_product()
        elif choice == '2':
            view_products()
        elif choice == '3':
            update_stock()
        elif choice == '4':
            delete_product()
        elif choice == '5':
            check_low_stock()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

# RUN
menu()
