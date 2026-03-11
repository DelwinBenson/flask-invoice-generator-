import os
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# simple invoice counter
invoice_counter = 1


@app.route("/")
def billing_form():
    return render_template("billing_form.html")


@app.route("/receipt", methods=["POST"])
def receipt():

    global invoice_counter

    # generate invoice number
    invoice_number = f"INV-{invoice_counter:03d}"
    invoice_counter += 1

    # generate date
    today = datetime.now().strftime("%d-%m-%Y")

    # get form data
    receiver_name = request.form.get("receiver_name")
    receiver_phone = request.form.get("receiver_phone")
    receiver_email = request.form.get("receiver_email")

    street = request.form.get("street")
    city = request.form.get("city")
    state = request.form.get("state")
    country = request.form.get("country")
    pincode = request.form.get("pincode")

    owner_name = request.form.get("owner_name")
    owner_phone = request.form.get("owner_phone")
    owner_email = request.form.get("owner_email")

    return render_template(
        "receipt.html",

        invoice_number=invoice_number,
        date=today,

        receiver_name=receiver_name,
        receiver_phone=receiver_phone,
        receiver_email=receiver_email,

        street=street,
        city=city,
        state=state,
        country=country,
        pincode=pincode,

        owner_name=owner_name,
        owner_phone=owner_phone,
        owner_email=owner_email
    )



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)