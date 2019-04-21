from flask import Flask, redirect, render_template, request, url_for,flash
from test import sys, order1
from system import System
app = Flask(__name__)
#app.config["SECRET_KEY"] = "Highly secret key"


@app.route("/")
def home():
    return "Home page"


@app.route("/inventory", methods=["GET", "POST"])
def maintain_inventory():
    inventory = sys.stock
    messages = []
    if request.method == "POST":
        quantity1 = int(request.form["quantity"])
        name1 = request.form["name"]
        delete = request.form["delete"]
        if quantity1 <= 0:
            message1 = "error: number should be greater than 0"
            messages.append(message1)

        if isinstance(name1, str):
            message2 = "error: name should be a string"
            messages.append(message2)

        if not sys.checkname(name1):
            message3 = "error: name is not in the inventory list"
            messages.append(message3)

        if quantity1 is not None and name1 is not None:
            sys.refillStock(name1, quantity1)

        if sys.checkname(delete):
            sys.deleteStock(delete) 

        #if quantity2 is not None and name2 is not None:
        return render_template("inventory.html", inventory=inventory, messages=messages)
    sys.reduce()
    return render_template("inventory.html", inventory=inventory, messages=messages)


@app.route("/customer/<int:Id>")
def customer_page(Id):

    order = sys.getorder(Id)
    return render_template("customer.html", order=order)


@app.route("/staff")
def staff_page():
    orders = sys.orders
    sys.removeorder()
    return render_template("staff.html", orders=orders)


if __name__ == '__main__':
    app.run(debug=True)
  #app.run(host="192.168.17.70", port=5000)


#@app.route("/delete", methods=["GET", "POST"])
#def delete_stock():

