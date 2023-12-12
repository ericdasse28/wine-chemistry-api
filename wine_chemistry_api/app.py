from flask import Flask, request

app = Flask(__name__)


@app.route("/wine_quality/estimate", methods=["POST"])
def predict_wine_quality():
    """Endpoint that predicts wine quality."""

    wine_features = request.json

    # Code here


if __name__ == "__main__":
    app.run()
