import streamlit as st
from time import sleep
import requests

flask_api_url2 = 'http://localhost:5000/NP'
flask_api_url3 = 'http://localhost:5000/NC'

def send_flask_data(data,URI):
     # Send data to Flask backend
    response = requests.post(URI, json= data)

    # Check the response from the Flask server
    if response.status_code == 200:
        st.success("Data sent successfully!")
    else:
        st.error(f"Failed to send data. Status Code: {response.status_code}")

        
curpage = 1      
name=None
points=None
level=None
player_id=None
displayName=None
password=None
email=None
description=None
def np():
    def page1():
        global name,points,level,player_id,displayName,password,email,description
        global curpage
        name = st.text_input("Name")
        points = st.number_input("points",disabled=True)
        level = st.number_input("level",disabled=True)
        player_id = st.text_input("player_id" )
        displayName = st.text_input("displayName" )
        password = st.text_input("password" ,type="password")
        email = st.text_input("email" )
        description = st.text_area("description" )
        
        next_clicked = st.form_submit_button("next")
        if next_clicked:
            curpage=2
    def page2():
        global curpage
        # Sample list of options
        options = ["Combat", "Archery", "Tactical", "Stealth" ,"Accuracy/Aim" ]

        # Multiselect widget
        selected_options = st.multiselect("Select skills :", options)

        # Display the selected options
        st.write("Your skills :", selected_options)
        
        # Slider widget for selecting a single value
        age_value = st.slider("Select age:", min_value=0.0, max_value=100.0, value=20.0)
       
        res=  st.form_submit_button() 
        
        if res:
            data = {
                "name" : name,
                "password" : password,
                "email" : email,
                "points" : 0,
                "age" : age_value,
                "combatSkills" : selected_options,
                "level" : level,
                "display_name" : displayName,
                "description" : description,
                "player_id" : player_id
                
            }
            send_flask_data(data, flask_api_url2)
            st.balloons()
            
            sleep(3)
            curpage=1
            return True
    
    
    with st.form("NP"):
        
        if curpage==1:
            page1()
        else:
            return page2()
        
        
    
    

def nc():
    # st.image( "f1.jpg", width=200)
    with st.form("NC"):
        
        ownerPlayerID = st.text_input("ownerPlayerID")
        carID = st.text_input("car ID")
        st.divider()
        modelName = st.text_input("model name")
        speed = st.slider("Select car max speed:", min_value=0.0, max_value=300.0, value=20.0)
        brandOptions=  ["Toyota" , "Ford" , "Chevrolet" , "Honda" , "Audi" , "Nissan" , "Maruti" , "BMW"]
        brand = st.radio("Select one option:", brandOptions)
        
        color = st.color_picker("Car colour")
         
       
        res=  st.form_submit_button() 
    if res:
        data = {
        "carID" : carID,
        "maxSpeed" : speed,
        "brandName" : brand,
        "colour" : color,
        "modelName" : modelName,
        "ownerPlayerID" : ownerPlayerID
        
            
       
        }
        send_flask_data(data, flask_api_url3)
        st.balloons()
        
        sleep(3)
        
        return True
          
        