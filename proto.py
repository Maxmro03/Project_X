from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database Connection
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="123456789",
    database="inventory_prototype_X"
)
cursor = db.cursor()

# Home Route - Display AWB Records
@app.route('/')
def index():
    cursor.execute("SELECT * FROM awb_details ORDER BY AWB")
    awb_records = cursor.fetchall()
    return render_template("dashboard.html", awb_records=awb_records)

# Add AWB Record Route
@app.route('/add_awb', methods=['POST'])
def add_awb():
    awb = request.form['AWB']
    mawb = request.form['MAWB']
    awb_date = request.form['AWB_date']
    freight_fordwarder = request.form['freight_fordwarder']
    amount = request.form['Amount']
    currency = request.form['Currency']
    supplier = request.form['Supplier']
    goods_types = request.form['Goods_types']
    clearance = request.form['Clearance']
    number_of_boxes = request.form['Number_of_boxes']
    weight = request.form['Weight']
    unit_of_measure = request.form['Unit_of_measure']
    volumetric_weight = request.form['Volumetric_weight']

    cursor.execute("""
        INSERT INTO awb_details 
        (AWB,MAWB, AWB_date, freight_fordwarder, Amount, Currency, Supplier, Goods_types, Clearance, Number_of_boxes, weight, unit_of_measure, volumetric_weight) 
        VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (awb,mawb, awb_date, freight_fordwarder, amount, currency, supplier, goods_types, clearance, number_of_boxes, weight, unit_of_measure, volumetric_weight))
    
    db.commit()
    return redirect(url_for('index'))

# Search AWB Route
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    cursor.execute("SELECT * FROM awb_details WHERE AWB = %s", (query,))
    search_results = cursor.fetchall()
    return render_template("dashboard.html", awb_records=search_results)

if __name__ == "__main__":
    app.run(debug=True)