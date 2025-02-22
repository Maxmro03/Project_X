from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database Connection
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="123456789",
    database="inventory_management"
)
cursor = db.cursor()

@app.route('/')
def index():
    cursor.execute("SELECT * FROM products ORDER BY sales_count DESC LIMIT 5")
    fast_moving = cursor.fetchall()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    return render_template("index.html", fast_moving=fast_moving, products=products)

@app.route('/add_product', methods=['POST'])
def add_product():
    name = request.form['name']
    category = request.form['category']
    stock = request.form['stock']  # Stock comes before price
    price = request.form['price']  # Price comes after stock

    cursor.execute(
        "INSERT INTO products (product_name, category, stock_quantity, price, sales_count) VALUES (%s, %s, %s, %s, 0)",
        (name, category, stock, price)  # Ensure correct order
    )
    db.commit()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
