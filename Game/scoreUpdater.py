import mysql.connector
import json


def connectHandler():
    return mysql.connector.connect(
         host= 'localhost',
  user= 'root',
  password= 'Sathvik22',
  database= 'gamedb'
    ) 
    

def pushScore(pname,score,level):
    
    gameDB = connectHandler()

    cursor = gameDB.cursor()

    cursor.execute(f"UPDATE leaderboard set score = {score}, level ={level} where pname = '{pname}' ")

    gameDB.commit()
    
    gameDB.close()





# gameDB.close()

