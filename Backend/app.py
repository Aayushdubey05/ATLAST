from flask import Flask, jsonify, request
from sentence_transformers import SentenceTransformer
import numpy as np

app = Flask(__name__)

# Initialize the SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Sample products data
products = [
    {"id": 1, "name": "Product A", "category": "Electronics", "stock_level": 5, "total_sales": 10000},
    {"id": 2, "name": "Product B", "category": "Groceries", "stock_level": 5, "total_sales": 10075},
    {"id": 3, "name": "Product C", "category": "Clothing", "stock_level": 3, "total_sales": 1000},
    {"id": 4, "name": "Product D", "category": "Grocer", "stock_level": 4, "total_sales": 10075},
    {"id": 5, "name": "Product E", "category": "Cloth", "stock_level": 3, "total_sales": 1000}
]

# Helper function for stock recommendation based on high sales and low stock
def recommend_stock_based_on_sales_and_stock():
    # Calculate a score for each product based on high sales and low stock
    recommendations = sorted(
        products,
        key=lambda product: (product["total_sales"] / (product["stock_level"] + 1)),  # Avoid division by zero
        reverse=True
    )
    # Recommend the top product with the highest score
    return recommendations[0]

@app.route('/api/recommend', methods=['GET'])
def get_stock_recommendation():
    # Get recommendation
    recommended_product = recommend_stock_based_on_sales_and_stock()
    return jsonify({"recommendation": recommended_product})

if __name__ == '__main__':
    app.run(port=5000)
