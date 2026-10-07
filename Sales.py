from Database import conn

class Sales:
    def __init__(self, name=None, contact=None):
        pass

    @staticmethod
    def create_table():
        cur = conn.cursor()
        cur.execute(
            """CREATE TABLE IF NOT EXISTS sales(
            id SERIAL PRIMARY KEY,
            customer_id INTEGER NOT NULL,
            date DATE NOT NULL,
            total_amount DECIMAL(10,2) NOT NULL,
            CONSTRAINT fk_sales_customer
            FOREIGN KEY (customer_id)
            REFERENCES customers(id)
            ON DELETE CASCADE
            )"""
        )
        conn.commit()
        cur.close()

    @staticmethod
    def insert_sale(customer_id, date, total_amount):
        cur = conn.cursor()
        cur.execute(
            """INSERT INTO sales (customer_id, date, total_amount)
            VALUES (%s,%s,%s)""",
            (customer_id, date, total_amount),
        )
        print(">>>>>> sale created!")
        conn.commit()
        cur.close()

    @staticmethod
    def update_sale(sale_id, customer_id=None, date=None, total_amount=None):
        cur = conn.cursor()
        cur.execute("SELECT * FROM sales WHERE id = %s", (sale_id,))
        sale = cur.fetchone()

        if not sale:
            print(">>>>> sale not found!")
            cur.close()
            return

        update_fields = []

        if customer_id:
            update_fields.append(f"customer_id = '{customer_id}'")

        if date:
            update_fields.append(f"date = '{date}'")

        if total_amount:
            update_fields.append(f"total_amount = '{total_amount}'")

        update_query = f"UPDATE sales SET {','.join(update_fields)} WHERE id = %s"
        cur.execute(update_query, (sale_id,))
        conn.commit()
        cur.close()

    @staticmethod
    def delete_sale(sale_id):
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM sales WHERE id = %s",
            (sale_id,),
        )
        conn.commit()
        cur.close()

    @staticmethod
    def view_sales():
        cur = conn.cursor()
        cur.execute("SELECT * FROM sales")
        sales = cur.fetchall()
        cur.close()
        return sales

    @staticmethod
    def view_sales_id(sale_id):
        cur = conn.cursor()
        cur.execute("SELECT * FROM sales WHERE id = %s", (sale_id,))
        sales = cur.fetchall()
        cur.close()
        return sales

    @staticmethod
    def generate_bill(sale_id):
        cur = conn.cursor()
        cur.execute("SELECT * FROM sales WHERE id = %s", (sale_id,))
        sale_items = cur.fetchall()
        total_amount = 0
        for item in sale_items:
            total_amount += item[3]

        cur.close()
        return total_amount

    # Analytical query
    @staticmethod
    def total_sale_by_date(start_date, end_date):
        cur = conn.cursor()
        cur.execute(
            "SELECT SUM(total_amount) FROM sales WHERE date BETWEEN %s AND %s",
            (start_date, end_date),
        )
        total_sales = cur.fetchone()
        cur.close()
        return total_sales

    @staticmethod
    def get_top_selling_products():
        cur = conn.cursor()
        cur.execute(
            """SELECT product_id, SUM(quantity) AS total_quantity
             FROM sale_items
             GROUP BY product_id
             ORDER BY total_quantity DESC
             LIMIT 5"""
        )
        total_products = cur.fetchall()
        cur.close()
        return total_products

    @staticmethod
    def get_sales_by_customer(customer_id):
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM sales WHERE customer_id = %s", (customer_id,)
        )
        sales = cur.fetchall()
        cur.close()
        return sales

    @staticmethod
    def sales_menu():
        while True:
            print("1. Create table")
            print("2. Insert Sale")
            print("3. Update Sale")
            print("4. Delete Sale")
            print("5. View Sales")
            print("6. View Sale by ID")
            print("7. Generate Bill")
            print("8. Total Sales by Date")
            print("9. Top 5 Selling Products")
            print("10. Sales by Customer")
            print("0. Exit Sales")

            choice = input("Enter your choice:")

            if choice == "1":
                Sales.create_table()
                print("<<<<<< sales table created!")

            elif choice == "2":
                customer_id = input("Enter Customer ID:")
                date = input("Enter sale Date:")
                total_amount = input("Enter Sales Amount:")
                Sales.insert_sale(customer_id, date, total_amount)
                print("<<<<<< sale inserted!")

            elif choice == "3":
                sale_id = input("Enter sale id:")
                customer_id = input("Enter Customer ID:")
                date = input("Enter sale Date:")
                total_amount = input("Enter Sales Amount:")
                Sales.update_sale(sale_id, customer_id, date, total_amount)

            elif choice == "4":
                sale_id = input("Enter sale id:")
                Sales.delete_sale(sale_id)
                print("<<<<<< Sale deleted!")

            elif choice == "5":
                sale = Sales.view_sales()
                print(sale)

            elif choice == "6":
                sale_id = input("Enter sale id:")
                sale = Sales.view_sales_id(sale_id)
                print(sale)

            elif choice == "7":
                sale_id = input("Enter sale id:")
                bill = Sales.generate_bill(sale_id)
                print(bill)

            elif choice == "8":
                start_date = input("Enter start date:")
                end_date = input("Enter end date:")
                sales = Sales.total_sale_by_date(start_date, end_date)
                print(sales)

            elif choice == "9":
                products = Sales.get_top_selling_products()
                print(products)

            elif choice == "10":
                customer_id = input("Enter Customer ID:")
                sales = Sales.get_sales_by_customer(customer_id)
                print(sales)

            elif choice == "0":
                print("Exiting..")
                break

            else:
                print("Invalid choice! please try again.")


# Sales.sales_menu()