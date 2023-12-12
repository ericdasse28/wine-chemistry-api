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

## Iteration 2

We want to make sure the data provided by the user as input is really about wine before performing a prediction. Our rule of thumb is that a wine has a pH comprised between 2.5 and 4.5. If the input pH does not fall into that umbrella, we want to return an error message "Error: A wine should normally have a pH comprised between 2.5 and 3.5" and HTTP error code 400 (Bad Request)

Add that verification to the endpoint you just implemented.

## Iteration 3

The company decided to focus only on red wines and therefore with 3.5 \< pH \< 4.5. A wine whose pH does not fall into that umbrella is most likely a white wine. Therefore, if the input corresponds to a white wine, we want to return the error message "Error: As of now, we only deal with red wine. Your input is most likely a white wine" and HTTP error code 400

Add this verification as well

## Iteration 4

Now, the company wants to present the quality of wine in a more concise manner, using words in another endpoint. Essentially, the expected output is:

- BAD (for wine quality between 0 and 3)
- AVERAGE (4 \<= quality \<= 6>)
- NOT BAD (from 7 to 9)
- PERFECTION (10)

Implement a second endpoint, with path `/wine_quality/estimate/summary` that outputs wine quality in that fashion.
