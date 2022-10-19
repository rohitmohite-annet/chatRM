from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World!</h1>"

@app.route('/webhook', methods=['POST'])
def testwebhook():
  return {
        "fulfillmentText": 'This is from the replit webhook',
        "source": 'webhook'
    }


if __name__ == "__main__":
    app.run()

