from flask import Flask, request, render_template,url_for,redirect,jsonify,make_response
import json
import pandas as pd
import pyodbc
app = Flask(__name__)
@app.route("/")
def index():
    return "<h1>Hello World!</h1>"

@app.route('/webhook', methods=['GET','POST'])
def testwebhook():
    # server = 'sql-4see.database.windows.net'
    # database = 'dev-4see'
    # username = 'db_admin'
    # password = 'Innovation!2022'
    # cnxn = pyodbc.connect(
    #     'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    # cursor = cnxn.cursor()
    # data = pd.read_sql("select Question from DialogFlowSampleQNA", cnxn)
    # first = data.iloc[0, 0]

    req = request.get_json(force=True)
    session = req.get('session')

    return {
            "fulfillmentText": str(req),
            "source": 'webhook'
        }


if __name__ == "__main__":
    app.run()
