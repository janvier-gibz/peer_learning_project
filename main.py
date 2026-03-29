from db import connect_db, create_tables
from shop import Shop


def main():
    conn = connect_db()

    if not conn:
        return

    create_tables(conn)

    shop = Shop(conn)

    while True:
        print("\n====== SHOP MENU ======")
        print("1. Add Product")
        print("2. View Products")
        print("3. Sell Product")
        print("4. View Sales")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            shop.add_product()
        elif choice == "2":
            shop.view_products()
        elif choice == "3":
            shop.sell_product()
        elif choice == "4":
            shop.view_sales()
        elif choice == "5":
            print("Goodbye!")
            conn.close()
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()