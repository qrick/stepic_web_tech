import flask


app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def root():
    res = ""
    for k, v in flask.request.args.items():
        res += "{}={}\n".format(k, v)    
    return res, 200

if __name__ == "__main__":
    app.run(debug=True)
