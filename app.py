from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/PROJECT-ROUTE')
def home():
     raise Exception("This is a test error for generating a 500 Internal Server Error.")
    # return jsonify(message="Hello level 400 FET, Quality Assurance!")


if __name__ == '__main__':
    app.run(debug=True)
