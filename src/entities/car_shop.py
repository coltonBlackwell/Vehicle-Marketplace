import mysql.connector
import os


class CarShop:

    def __init__(self):

        self.mydb = mysql.connector.connect(
            host=os.environ.get("MYSQL_HOST", "localhost"),
            user="colton",
            password="good4Colton!",
            database="car_shop"
        )

        self.mycursor = self.mydb.cursor()

        # self.mycursor.execute("CREATE DATABASE car_shop")

        self.mycursor.execute("CREATE TABLE IF NOT EXISTS cars (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), price INT)")

    def add_car(self, car): #Takes in Car object

        sql = "INSERT INTO cars (name, price) VALUES (%s, %s)"
        val = (car.name, car.price)
  
        self.mycursor.execute(sql, val) #Use execute if only one record

        self.mydb.commit()

        car.id = self.mycursor.lastrowid
    
    def remove_car(self, car_id):

        sql = "DELETE FROM cars WHERE id = %s"

        val = (car_id,)

        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print(self.mycursor.rowcount, "car deleted.")

    def shut_down_store(self):

        print("\n--- Dropping all tables in 'mydatabase' ---")
        self.mycursor.execute("SHOW TABLES")
        for (table_name,) in self.mycursor.fetchall():
            self.mycursor.execute(f"DROP TABLE {table_name}")
            print(f"Dropped: {table_name}")

    def get_all_cars(self):
        self.mycursor.execute("SELECT * FROM cars")
        return self.mycursor.fetchall()  # Each row is (id, name, price)