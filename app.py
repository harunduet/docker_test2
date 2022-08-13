## Hello world app

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
## End of code to test 3rd commit