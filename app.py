from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        principal = int(request.form["principal"])
        rate = int(request.form["percentage"])
        duration = int(request.form["duration"])
        form_intrest = request.form["intrest-type"]
        intrest = int()
        total_payment_due = principal * 1 + rate * duration
        monthly_intrest = principal * rate / 12
        monthly_principal = total_payment_due / rate * duration / 12
        total_principal = principal * 1 + rate * duration
        if form_intrest == "flat rate":
            intrest = principal * rate * duration
        if form_intrest == "reducing balance":
            intrest = total_principal - monthly_principal *rate
        if form_intrest == "compound intrest":
            intrest = principal * (1 + rate ** duration - 1)

        # A = P(1 + rt)
       
        return render_template(
            "index.html",
            intrest=intrest,
            monthly_principal=monthly_principal,
            monthly_intrest=monthly_intrest,
            total_principal=total_principal,
            total_payment_due=total_payment_due,
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
