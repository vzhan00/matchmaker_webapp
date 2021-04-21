import calc
import flask
from main import app

@app.route('/', methods=['GET'])
def display_ranking():
    return calc.ladder_ranking()

@app.route('/', methods=['POST'])
def add_user():
    name = flask.request.json['name']
    calc.add_user(name)
    return flask.jsonify(name)

@app.route('/', methods=['PUT'])
def update_all():
    b_top = flask.request.json['b_top']
    b_jng = flask.request.json['b_jng']
    b_mid = flask.request.json['b_mid']
    b_adc = flask.request.json['b_adc']
    b_sup = flask.request.json['b_sup']
    r_top = flask.request.json['r_top']
    r_jng = flask.request.json['r_jng']
    r_mid = flask.request.json['r_mid']
    r_adc = flask.request.json['r_adc']
    r_sup = flask.request.json['r_sup']
    one_result = flask.request.json['one_result']
    two_result = flask.request.json['two_result']
    calc.update_all(
        b_top,
        b_jng,
        b_mid,
        b_adc,
        b_sup,
        r_top,
        r_jng,
        r_mid,
        r_adc,
        r_sup,
        one_result,
        two_result
        )
    return flask.jsonify(
        b_top,
        b_jng,
        b_mid,
        b_adc,
        b_sup,
        r_top,
        r_jng,
        r_mid,
        r_adc,
        r_sup,
        one_result,
        two_result)

app.run()
