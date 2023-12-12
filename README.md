# wine-chemistry-api

API that gives some chemical information about wine

## Context

You are working for a company that performs physicochemical analyses on
wine. They collected a lot of data about different wines and built a machine
learning model that predicts the quality of wine on a scale of 0 to 10 given
some wine features, namely:

- fixed acidity
- volatile acidity
- citric acid
- chlorides
- free sulfur dioxide
- total sulfur dioxide
- density
- pH
- sulphates
- alcohol

The company decided to make their model available to the outside world through an API
Your mission, if you accepted it, is to implement the POST API endpoint `/wine/estimate_quality`
that will a take json containing the above mentioned wine features as input, and return
the quality of the described wine as output.

### Example

#### Request

```bash
curl --header "Content-Type: application/json"
    --request POST \
    --data '{"fixed acidity": 7.8, "volatile acidity": 0.59, "citric acid": 0.18, "chlorides": 0.076, "free sulfur dioxide": 17.0, "total sulfur dioxide": 54.0, "density": 0.9975, "pH": 3.43, "sulphates": 0.59, "alcohol": 10.0}' \
    http://localhost:8080/wine/estimate_quality
```

#### Response

```
{"quality": 5}
```

## Iteration 1

The model was made available to you in the directory `ml_model/`

Fill in the code in the view `predict_wine_quality` of app.py so that it:

1. Loads the model using [joblib](https://pypi.org/project/joblib/)
2. Predicts the quality of wine described by the variable `wine_features`
3. And returns the quality as described by the example
