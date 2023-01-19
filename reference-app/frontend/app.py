from flask import Flask, render_template, request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route("/")
def homepage():
    return render_template("main.html")


if __name__ == "__main__":
    app.run()
