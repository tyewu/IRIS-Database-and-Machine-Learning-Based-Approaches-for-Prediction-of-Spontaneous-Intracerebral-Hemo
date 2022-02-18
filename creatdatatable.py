import pyodbc

def create_intrahemor_table(connection):
    cursor = connection.cursor()
    create_table = "CREATE TABLE Dhc.Intrahemor(Name varchar(50) unique, Age numeric(10,4), Baselineheartrate numeric(10,4), " \
                   "Uricacid numeric(10,4), Ddimer numeric(10,4), Chlorine numeric(10,4), GCS numeric(10,4), GFR numeric(10,4),  " \
                   "Probability numeric(10,4), DateTimeUpdated datetime)"
    try:
        cursor.execute(create_table)
        print("Created Dhc.Intrahemor table successfully.")
        connection.commit()
    except Exception as e:
        print("Error creating portfolio: " + str(e))

def get_connection_info(file_name):

    connections = {}
    with open(file_name) as f:
        lines = f.readlines()
        for line in lines:
            line = ''.join(line.split())
            connection_param, connection_value = line.split(":")
            connections[connection_param] = connection_value
    return connections

def run():
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
    print("Connected to InterSystems IRIS")
    create_intrahemor_table(connection)

if __name__ == '__main__':
    run()
