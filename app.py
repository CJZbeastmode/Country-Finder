from flask import Flask, render_template, url_for


# Configure application
app = Flask(__name__)

@app.route("/")
def cityfinder():
    return render_template("cityfinder.html")

@app.route("/generator")
def generator():
    return render_template("generator.html")

@app.route("/about")
def about():
    return render_template("about.html")



if __name__ == "__main__":
    app.run(debug=True)