from flask import Flask, jsonify,request
import getting_information
import json
app = Flask(__name__)
reward_responses={}
@app.route('/get_task', methods=['GET'])
def get_task():
    return ("Hi")

@app.route('/post_task', methods=['POST'])
def create_task():
#    ira_request = request.json["cookie_request"]
    try:

        query_params = ''
        query = "SELECT  keyword from Rewards_logs"
        kv_responses = getting_information.execute_query(query)
    except Exception as e:
        print ("EXCEPTION IN Update star rewards********", str(e))
        return json.dumps({"status": "Failure"})

    return json.dumps({'result':kv_responses[0][0]})


if __name__ == "__main__":
       #create_task() 
       app.run(host='0.0.0.0', port=3020, debug=True)
