from Database import conn

class Customers:
    def __init__(self, name=None, contact=None):
        pass
        # self.name = name
        # self.contact = contact
    
    @staticmethod
    def create_table():
        cur = conn.cursor()
        cur.execute(
            """CREATE TABLE IF NOT EXISTS customers(
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            contact VARCHAR(15) NOT NULL
            )"""
        )
        conn.commit()
        cur.close()

    @staticmethod
    def insert_customer(name, contact):
        cur = conn.cursor()
        cur.execute(
            """INSERT INTO customers(name,contact)
            VALUES (%s,%s)
            """,
            (name, contact),
        )
        conn.commit()
        cur.close()

    @staticmethod
    def update_customer(customer_id, name=None, contact=None):
        cur = conn.cursor()
        cur.execute("SELECT * FROM customers WHERE id = %s", (customer_id,))
        customer = cur.fetchone()

        if not customer:
            print(">>>>> Customer not found!")
            cur.close()
            return

        update_fields = []
        values = []

        if name:
            update_fields.append("name = %s")
            values.append(name)

        if contact:
            update_fields.append("contact = %s")
            values.append(contact)

        if not update_fields:
            cur.close()
            return

        values.append(customer_id)

        update_query = f"UPDATE customers SET {','.join(update_fields)} WHERE id = %s"
        cur.execute(update_query, values)

        conn.commit()
        cur.close()
    
    @staticmethod
    def delete_customer(customer_id):
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM customers WHERE id = %s",
            (customer_id,),
        )
        conn.commit()
        cur.close()

    @staticmethod
    def get_all_customers():
        cur = conn.cursor()
        cur.execute("SELECT * FROM customers")
        customers = cur.fetchall()
        cur.close()
        return customers

    @staticmethod
    def customer_menu():
        while True:
            print("1. Create table")
            print("2. Insert Customer")
            print("3. update Customer")
            print("4. Delete Customer")
            print("5. View Customer")
            print("0. Exit Customers")

            choice = input("Enter your choice:")

            if choice == "1":
                Customers().create_table()
                print("<<<<<< customer Table created!")

            elif choice == "2":
                name = input("Enter customer name:")
                contact = input("Enter customer contact:")
                Customers().insert_customer(name, contact)
                print("<<<<<< customer inserted!")

            elif choice == "3":
                customer_id = int(input("Enter customer id:"))
                name = input("Enter new customer name:")
                contact = input("Enter new customer contact:")
                Customers().update_customer(customer_id, name, contact)
                print("<<<<<< customer updated!")

            elif choice == "4":
                customer_id = int(input("Enter customer id:"))
                Customers().delete_customer(customer_id)
                print("<<<<<< customer deleted!")

            elif choice == "5":
                customers = Customers().get_all_customers()
                print(customers)
                print("<<<<<< customer fetched!")

            elif choice == "0":
                print("Exiting..")
                break

            else:
                print("Invalid choice! please try again.")

# Customers().customer_menu()
            


    

   
