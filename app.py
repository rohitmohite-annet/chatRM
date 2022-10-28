from flask import Flask, request, render_template,url_for,redirect,jsonify,make_response
import json
import pandas as pd
import pyodbc
app = Flask(__name__)
@app.route("/")
def index():
    return "<h1>Hello World!</h1>"
#
# def results():
# 	# build a request object
# 	req = request.get_json(force=True)
#
# 	# fetch action from json
# 	action = req.get('queryResult').get('action')
#
# 	# return a fulfillment response
# 	return {'fulfillmentText': 'This is a response from webhook ROHIT.'}


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
    # return make_response(jsonify(results()))

    req = request.get_json(force=True)
    queryResult = req.get('queryResult')
    queryText = queryResult.get('queryText')
    session = req.get('session')

    return {
            "fulfillmentText": str(queryText) ,
            "source": 'webhook'
        }


if __name__ == "__main__":
    app.run()
