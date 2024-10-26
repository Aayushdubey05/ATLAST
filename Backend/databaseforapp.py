import mysql.connector
import random

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aayush@05",
    database="Retail"
)
cursor = conn.cursor()

# Define categories and names for random selection
categories = ["Electronics", "Groceries", "Clothing", "Furniture", "Toys","Foods","Buildings","Houses"]
names = ["Product A", "Product B", "Product C", "Product D", "Product E"]

# Insert random product data
for i in range(1, 600):
    name = random.choice(names)
    category = random.choice(categories)
    stock_level = random.randint(1, 100)
    total_sales = random.randint(1000, 10000)
    
    cursor.execute("""
        INSERT INTO products (id, name, category, stock_level, total_sales)
        VALUES (%s, %s, %s, %s, %s)
    """, (i, name, category, stock_level, total_sales))

conn.commit()
cursor.close()
conn.close()

print("MySQL database 'product_db' populated with 500 entries.")
