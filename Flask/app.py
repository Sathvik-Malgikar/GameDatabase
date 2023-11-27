from flask import Flask, jsonify,request,url_for
import mysql.connector
from flask_cors import CORS  # Import the CORS extension

app = Flask(__name__)
CORS(app)

def connectHandler():
    return mysql.connector.connect(
         host= 'localhost',
  user= 'root',
  password= 'Sathvik22',
  database= 'gamedb'
    )
print(url_for("efgnwog",fw3ion="fwuiwfu"))
def authenticate(username,password,deleteMode=False):
    
    if deleteMode:
            
        gameDB = connectHandler()
        cursor = gameDB.cursor()
        # print(username,password)
        cursor.execute(f"DELETE FROM users where username = '{username}' and password = '{password}' ")
        print(f"DELETE FROM users where username = '{username}' and password = '{password}' ")
        print(f"deleted {username} successfully ")
        # print(temp,"TEMP")
        gameDB.commit()
        gameDB.close()
        

        
        return
    
    gameDB = connectHandler()
    cursor = gameDB.cursor()
    # print(username,password)
    cursor.execute(f"SELECT * FROM users where username = '{username}' and password = '{password}' ")
    
    temp = cursor.fetchall()
    # print(temp,"TEMP")
    gameDB.close()
    
    return temp!=[]
    
    
@app.route('/auth', methods=['GET'])
def auth():
    uname = request.args.get('uname')
    passw = request.args.get('pass')
    
    return str(authenticate(uname,passw))

@app.route('/del', methods=['GET'])
def dele():
    uname = request.args.get('uname')
    passw = request.args.get('pass')
    
    return str(authenticate(uname,passw,True))


@app.route('/data', methods=['GET'])
def get_data():
    tabname = request.args.get('tabname')
    gameDB = connectHandler()
    cursor = gameDB.cursor()
    print("getdata")
    cursor.execute(f"select * from {tabname}")
    data = cursor.fetchall()
    gameDB.close()
    # print("returning " + data)
    return data
    pass

@app.route('/data2', methods=['GET'])
def get_data2():
    tabname = request.args.get('tabname')
    gameDB = connectHandler()
    cursor = gameDB.cursor()
    print("getdata")
    cursor.execute(f"select * from {tabname}")
    data = cursor.fetchall()
    gameDB.close()
    # print("returning " + data)
    return data
    pass


    
@app.route('/data', methods=['POST'])
def post_data():
    try:
        tabname = request.args.get('tabname')
        data_to_insert = request.get_json()

        print(data_to_insert)
        gameDB = connectHandler()
        cursor = gameDB.cursor()

        # Assuming data_to_insert is a dictionary with keys matching the database columns
        columns = ', '.join(data_to_insert.keys())
        values = ', '.join(['%s' for _ in range(len(data_to_insert))])

        # Use parameterized query to avoid SQL injection
        print(f"INSERT INTO {tabname} ({columns}) VALUES ({values})", tuple(data_to_insert.values()))
        cursor.execute(f"INSERT INTO {tabname} ({columns}) VALUES ({values})", tuple(data_to_insert.values()))

        gameDB.commit()
        gameDB.close()

        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


@app.route('/NP', methods=['POST'])
def receive_data1():
    data = request.get_json()
    print("Received data:", data)
    gameDB = connectHandler()
    cursor = gameDB.cursor()
    
    cursor.execute("INSERT INTO profiles (name, points, level,player_id, display_name, password,email) VALUES (%s, %s, %s,%s,%s,%s,%s)", (data["name"], data["points"], data["level"], data["player_id"], data["display_name"], data["password"], data["email"]))  
 
    gameDB.commit()
    gameDB.close()
    return jsonify({"message": "Data received successfully!"})

@app.route('/NC', methods=['POST'])
def receive_data2():
    data = request.get_json()
    print("Received data:", data)
    gameDB = connectHandler()
    cursor = gameDB.cursor()
    cursor.execute("INSERT INTO cars (carID, maxspeed, brandname,modelname, colour, ownerplayerid) VALUES (%s, %s, %s,%s,%s,%s)", (data["carID"], data["maxSpeed"], data["brandName"], data["modelName"], data["colour"], data["ownerPlayerID"], ))  
 
    gameDB.commit()
    gameDB.close()
    # cursor.close()
    return jsonify({"message": "Data received successfully!"})

def populate():
    print("POPULATING ...")
    gameDB = connectHandler()
    cursor = gameDB.cursor()
    cursor.execute("drop table if exists profiles")
    cursor.execute("drop table if exists cars")
    cursor.execute("drop table if exists leaderboard")
    cursor.execute("drop table if exists users")
    cursor.execute("drop table if exists playerStatus")
    cursor.execute("create table profiles(name varchar(30) primary key , points int , level int, player_id varchar(20) , display_name varchar(16) ,password varchar(10) ,email varchar(50)  )")
    cursor.execute('''INSERT INTO profiles  
VALUES
("User1", 1200, 5, "I love gaming!", "Gamer1", "password1", "user1@example.com"),
("User2", 800, 3, "Gamer for life!", "Gamer2", "password2", "user2@example.com"),
("User3", 1500, 8, "Achievement hunter", "Gamer3", "password3", "user3@example.com"),
("User4", 600, 2, "Casual gamer", "Gamer4", "password4", "user4@example.com"),
("User5", 2000, 10, "Pro gamer", "Gamer5", "password5", "user5@example.com"),
("User6", 950, 4, "Team player", "Gamer6", "password6", "user6@example.com"),
("User7", 1700, 7, "Strategy master", "Gamer7", "password7", "user7@example.com"),
("User8", 700, 3, "High score chaser", "Gamer8", "password8", "user8@example.com"),
("User9", 1400, 6, "RPG enthusiast", "Gamer9", "password9", "user9@example.com"),
("User10", 1100, 5, "Puzzle solver", 'Gamer10', "password10", "user10@example.com")''')
    
    
    cursor.execute("create table cars(carID varchar(30) primary key , maxSpeed float , brandName varchar(30)  , modelName varchar(20) , colour varchar(16) ,ownerPlayerID varchar(20)  )")
    cursor.execute('''INSERT INTO cars (carID, maxSpeed, brandName, modelName, colour, ownerPlayerID)
VALUES
("vbUVYuyvuo67", 120.3, "Toyota", "Supra-mk4", "Crimson-red", "Gamer8"),
("4iLko3aWz6X", 140.2, "Ford", "Mustang", "Silver", "Gamer2"),
("Y5HtLjC9kZs", 110.8, "Chevrolet", "Camaro", "Blue", "Gamer4"),
("2gPjA1FvMws", 130.5, "Nissan", "GT-R", "Black", "Gamer6"),
("8ZqKu0LmRQn", 112.7, "Honda", "Civic", "White", "Gamer1"),
("fNvp9PjRxYd", 125.0, "BMW", "M3", "Silver", "Gamer7"),
("D3mW2bGqJzo", 138.4, "Audi", "A4", "Red", "Gamer3"),
("rKlFfO0zEj1", 118.9, "Mazda", "RX-7", "Yellow", "Gamer9"),
("1nCv5SxO2Jp", 132.1, "Porsche", "911", "Black", "Gamer5"),
("OaRyNwBh2Vp", 115.6, "Subaru", "Impreza", "Blue", "Gamer10")
''')
    
    cursor.execute("create table leaderBoard(pname varchar(30) primary key , score int default 0 , level int default 1 )")
    cursor.execute('''INSERT INTO leaderBoard  
VALUES
("Jaganna" , 400, 5),
("Sathvik", 0, 1)''')
    
    cursor.execute("create table users(username varchar(30) primary key , password varchar(30) not null , admin_role boolean default false )")
    cursor.execute('''INSERT INTO users  
VALUES 
("Sathvik", "gg", True)''')
    
    cursor.execute("create table playerStatus(pname varchar(30) primary key , gameover boolean default false)")
    cursor.execute('''INSERT INTO playerStatus  
VALUES
("Jaganna" ,false),
("Sathvik",  false)''')
    
    
    
    
    cursor.execute('''
            CREATE TRIGGER set_gameover_to_true
AFTER UPDATE ON leaderBoard
FOR EACH ROW
BEGIN
    IF NEW.level =5
    THEN
    UPDATE playerStatus
    SET gameover = TRUE
    WHERE pname = NEW.pname;
    END IF;
END;
               ''')
    
    gameDB.commit()
    
    gameDB.close()


    
if __name__ == '__main__':
    populate()
    app.run(debug=True)
