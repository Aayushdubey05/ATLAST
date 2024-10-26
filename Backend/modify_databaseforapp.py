import csv

def update_data():
    # Load existing data
    with open('products.csv', mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        products = list(reader)

    # Update data logic
    for product in products:
        # Example: Increase stock level by 10 for each product
        product['stock_level'] = int(product['stock_level']) + 10

    # Write updated data back to CSV
    with open('products.csv', mode='w', newline='') as csvfile:
        fieldnames = ['id', 'name', 'category', 'stock_level', 'total_sales']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for product in products:
            writer.writerow(product)

if __name__ == "__main__":
    update_data()
    print("Data updated successfully.")
