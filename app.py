import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect("pet_crm.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/customers")
def customers():
    keyword = request.args.get("keyword", "").strip()

    conn = get_db_connection()
    cursor = conn.cursor()

    if keyword:
        search_keyword = f"%{keyword}%"

        cursor.execute("""
            SELECT id, name, wechat, city, budget, cat_type, status, created_at
            FROM customers
            WHERE name LIKE ?
               OR wechat LIKE ?
               OR city LIKE ?
               OR cat_type LIKE ?
            ORDER BY id DESC
        """, (search_keyword, search_keyword, search_keyword, search_keyword))
    else:
        cursor.execute("""
            SELECT id, name, wechat, city, budget, cat_type, status, created_at
            FROM customers
            ORDER BY id DESC
        """)

    customer_list = cursor.fetchall()
    conn.close()

    return render_template("customers.html", customers=customer_list, keyword=keyword)


@app.route("/customers/new", methods=["GET", "POST"])
def new_customer():
    if request.method == "POST":
        name = request.form.get("name")
        wechat = request.form.get("wechat")
        city = request.form.get("city")
        budget = request.form.get("budget")
        cat_type = request.form.get("cat_type")
        message = request.form.get("message")

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO customers (name, wechat, city, budget, cat_type, message)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, wechat, city, budget, cat_type, message))

        conn.commit()
        conn.close()

        return redirect("/customers")

    return render_template("new_customer.html")


@app.route("/customers/<int:customer_id>/delete")
def delete_customer(customer_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM customers
        WHERE id = ?
    """, (customer_id,))

    conn.commit()
    conn.close()

    return redirect("/customers")

@app.route("/customers/<int:customer_id>/status/<status>")
def update_customer_status(customer_id, status):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE customers
        SET status = ?
        WHERE id = ?
    """, (status, customer_id))

    conn.commit()
    conn.close()

    return redirect("/customers")

@app.route("/customers/<int:customer_id>")
def customer_detail(customer_id):
    
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, wechat, city, budget, cat_type, message, status, created_at
        FROM customers
        WHERE id = ?
    """, (customer_id,))

    customer = cursor.fetchone()

    conn.close()

    return render_template("customer_detail.html", customer=customer)


if __name__ == "__main__":
    app.run(debug=True)