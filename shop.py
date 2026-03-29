class Shop:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

    def add_product(self):
        try:
            name = input("Enter product name: ")
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))

            query = "INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)"
            self.cursor.execute(query, (name, price, quantity))
            self.conn.commit()

            print("Product added successfully!")

        except Exception as e:
            print("Error adding product:", e)

    def view_products(self):
        try:
            self.cursor.execute("SELECT * FROM products")
            products = self.cursor.fetchall()

            if not products:
                print("No products found.")
                return

            print("\n--- Product List ---")
            for p in products:
                print(f"ID: {p[0]} | Name: {p[1]} | Price: {p[2]} | Qty: {p[3]}")

        except Exception as e:
            print("Error fetching products:", e)

    def sell_product(self):
        try:
            name = input("Enter product name: ")
            qty = int(input("Enter quantity: "))

            self.cursor.execute(
                "SELECT quantity, price FROM products WHERE name=%s",
                (name,)
            )
            result = self.cursor.fetchone()

            if result:
                stock, price = result

                if qty <= stock:
                    new_qty = stock - qty
                    total = qty * price

                    # Update stock
                    self.cursor.execute(
                        "UPDATE products SET quantity=%s WHERE name=%s",
                        (new_qty, name)
                    )

                    # 🔥 Insert with phone + location
                    self.cursor.execute(
                        """INSERT INTO sales 
                        (product_name, quantity, total_price) 
                        VALUES (%s, %s, %s, %s, %s)""",
                        (name, qty, total)
                    )

                    self.conn.commit()
                    print("Sale successful!")
                else:
                    print("Not enough stock!")
            else:
                print("Product not found!")

        except Exception as e:
            print("Error during sale:", e)

    def view_sales(self):
        try:
            self.cursor.execute("SELECT * FROM sales")
            sales = self.cursor.fetchall()

            if not sales:
                print("No sales recorded.")
                return

            print("\n--- Sales Records ---")
            for s in sales:
                print(f"""
ID: {s[0]}
Product: {s[1]}
Quantity: {s[2]}
Total: {s[3]}
------------------------
""")

        except Exception as e:
            print("Error fetching sales:", e)
