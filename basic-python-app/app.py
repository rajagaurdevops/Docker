from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Flask App deployed successfully via GitHub Actions!  Auther - Raja kumar Gaur and aman and nishant"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
