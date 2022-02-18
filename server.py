from flask import Flask, request, jsonify
from project import *
import json
import pyodbc
from datetime import datetime

def get_connection_info(file_name):

    connections = {}
    with open(file_name) as f:
        lines = f.readlines()
        for line in lines:
            line = ''.join(line.split())
            connection_param, connection_value = line.split(":")
            connections[connection_param] = connection_value
    return connections


app = Flask(__name__)
connection_detail = get_connection_info("connection.config")
ip = connection_detail["ip"]
port = int(connection_detail["port"])
namespace = connection_detail["namespace"]
username = connection_detail["username"]
password = connection_detail["password"]
driver = "{InterSystems IRIS ODBC35}"

# Create connection to InterSystems IRIS
connection_string = 'DRIVER={};SERVER={};PORT={};DATABASE={};UID={};PWD={}'\
    .format(driver, ip, port, namespace, username, password)
connection = pyodbc.connect(connection_string)
connection.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
connection.setencoding(encoding='utf-8')

# 脑出血死亡预测
@app.route('/api', methods=['POST'])
def intra_hemo():
    r = request.json
    r_json = json.loads(r)
    res = cal_pro(r_json["data"])
    response = {
        'probability': str(res)
    }

    data = r_json["data"]
    data = list(data.values())
    try:
        cursor = connection.cursor()

        sql = "INSERT INTO Dhc.Intrahemor (Name, Age, Baselineheartrate, Uricacid, Ddimer, Chlorine, GCS, GFR, Probability, DateTimeUpdated) VALUES (?,?,?,?,?,?,?,?,?,?)"
        current_time = datetime.now()
        cursor.execute(sql, data[0],
                       float(data[1]),
                       float(data[2]),
                       float(data[3]),
                       float(data[4]),
                       float(data[5]),
                       float(data[6]),
                       float(data[7]),
                       float(res), current_time)
        print("Added new line item{}.".format(data[0]))
        connection.commit()
    except Exception as e:
        print(str(e))
    return jsonify(response)

app.run(host="0.0.0.0", port=5001)