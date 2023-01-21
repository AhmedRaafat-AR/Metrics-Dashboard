import logging
from flask import Flask, render_template, request, jsonify
from flask_opentracing import FlaskTracing
from prometheus_flask_exporter import PrometheusMetrics
from jaeger_client import Config
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor


import pymongo
from flask_pymongo import PyMongo


app = Flask(__name__)
metrics = PrometheusMetrics(app)
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()


app.config["MONGO_DBNAME"] = "example-mongodb"
app.config[
    "MONGO_URI"
] = "mongodb://example-mongodb-svc.default.svc.cluster.local:27017/example-mongodb"

mongo = PyMongo(app)


def init_tracer(service):
    logging.getLogger("").handlers = []
    logging.basicConfig(format="%(message)s", level=logging.DEBUG)

    config = Config(
        config={"sampler": {"type": "const", "param": 1,}, "logging": True,},
        service_name=service,
    )

    # this call also sets opentracing.tracer
    return config.initialize_tracer()

tracer = init_tracer('backend')
tracing = FlaskTracing(tracer, True, app)

@app.route("/")
def homepage():
    return "Hello World"


@app.route("/api")
def my_api():
    answer = "something"
    return jsonify(repsonse=answer)


@app.route("/star", methods=["POST"])
def add_star():
    star = mongo.db.stars
    name = request.json["name"]
    distance = request.json["distance"]
    star_id = star.insert({"name": name, "distance": distance})
    new_star = star.find_one({"_id": star_id})
    output = {"name": new_star["name"], "distance": new_star["distance"]}
    return jsonify({"result": output})


if __name__ == "__main__":
    app.run()
