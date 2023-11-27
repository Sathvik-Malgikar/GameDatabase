import altair as alt
import streamlit as st
from streamlit_modal import Modal
import requests
from time import sleep
# from bghandle import set_png_as_page_bg
from modal import np,nc
import base64

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


bgimg = get_img_as_base64("download.jpeg")
abstract1 = get_img_as_base64("abstract1.jpg")

# Flask API endpoint
flask_api_url1 = 'http://localhost:5000/data'
flask_api_url2 = 'http://localhost:5000/auth'
flask_api_url3 = 'http://localhost:5000/del'

# print(st.__version__)
# Function to make a GET request to the Flask route

def auth(u,p):
    response = requests.get(flask_api_url2,params={"uname" : u, "pass" : p})
    if response.status_code == 200:
        # print(response.text,"in auth")
        
        return response.text
    else:
        print("no response in auth")
        return None

def get_flask_data(selected_option):
    response = requests.get(flask_api_url1,params={"tabname" : selected_option})
    if response.status_code == 200:
        return response.json()
    else:
        return None
import json
def post_flask_data(selected_option, data_to_post):
    # flask_api_url2 = "your_flask_api_url_for_post_request"

    # Assuming data_to_post is a dictionary containing the JSON data
    headers = {'Content-Type': 'application/json'}
    
    # Convert the dictionary to a JSON string
    json_data = json.dumps(data_to_post)

    # Make the POST request
    response = requests.post(flask_api_url1, params={"tabname": selected_option}, data=json_data, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return None

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url("data:image/png;base64,{bgimg}");
background-size: 100%; 
background-position: center;
background-repeat: no-repeat;
background-attachment: local;
}}
 
</style>
"""
st.markdown(page_bg_img , unsafe_allow_html=True)

st.title(":red[Game Database]")

c1,c2,c3 = st.columns(3)

if "loggedIn" not in st.session_state:
    
    st.session_state["loggedIn"]=False

st.write()

def makeNewUser(s1,s2,deleteMode=False):
    
    if deleteMode:
        response = requests.get(flask_api_url3,params={"uname" : s1 , "pass" : s2})
        return
    
    post_flask_data("users",{"username" : s1, "password": s2})

with st.container():
    
    with st.form("auth"):
            
        
        uname = c1.text_input("Username" ,placeholder="Username" )

        passw    = c2.text_input("Password" , type="password",placeholder="Password")
        
        nclicked = c3.button("Create new user")
        if nclicked:
            makeNewUser(uname,passw)
        
        
        
        ndclicked = c3.button("Delete user !",type="primary")
        if ndclicked:
            makeNewUser(uname,passw,True)
        
        # Add some text
        if st.form_submit_button("Login",use_container_width=True ):
            if (auth(uname,passw))=="True" :
                st.session_state["loggedIn"]=True 
                st.write(" <h1 style='color: green;' >Login success !</h1>  ",unsafe_allow_html=True)
            else:
                st.session_state["loggedIn"]=False
                st.write("<h1 style='color: red;' >Invalid credentials !</h1> ",unsafe_allow_html=True)
                


if "loggedIn" not in st.session_state or not st.session_state["loggedIn"]:
    exit()
        
if st.button("Logout" ):
    st.write(":red[Logout success ] ")
    st.session_state["loggedIn"]=False
    st.rerun()

# newProfile = st.button("Make a new profile")
# if newProfile:
#     npmodal.open()
    

NPmodal = Modal("Make a new profile" , key="NP",max_width=2000 )
NCmodal = Modal("Add a new car" , key="NC",max_width=1200)

newProfile = st.button("Make a new profile")
newCar = st.button("Make a new car")
if newProfile:
  
    NPmodal.open()
if newCar:
    NCmodal.open()



if NPmodal.is_open():
    with NPmodal.container():
        
        if np():
            st.toast("Successfully Added!")
            NPmodal.close()

 
            

# custom_div_html = """
#         <div style="background-color: lightblue; padding: 10px;">
#             <h1>This is a custom div with text.</h1>
#         </div>
#         """

# st.markdown(custom_div_html, unsafe_allow_html=True)
  
if NCmodal.is_open():
    
    with NCmodal.container():
        
        
        
        if nc():
            st.toast("Successfully Added!")
            NCmodal.close()

       



options = ["cars", "profiles","leaderboard" ]
selected_option = st.selectbox("Select table :", options) 

import time
def getScore(sst):

    while True:
        # print(sst)
        # print("fetching")
        sst["fetchedData"] = get_flask_data("leaderboard")
        # print(sst["fetchedData"])
        st.rerun()
        time.sleep(0.3)

import threading
from streamlit.runtime.scriptrunner import add_script_run_ctx
gs = threading.Thread(target=getScore,args=(st.session_state,))
add_script_run_ctx(gs)


if st.button("Get data" ):
    if selected_option == "leaderboard":
        gs.start()
    else:
        st.write("getting from backend please wait ...")
        data =get_flask_data(selected_option)
        print((data))
        st.dataframe(data)


def drawChart():
    if "fetchedData" not in st.session_state:return
    import pandas as pd
    import numpy as nump

     

    chart_data = pd.DataFrame(
    {"names":  [x[0] for x in st.session_state["fetchedData"]], "score": [x[1] for x in st.session_state["fetchedData"]]
        
    } , 
    )
    # st.bar_chart(
        
    # chart_data, x="names", y=["score"  ], color=["#0000ff" ] )
    
    # st.bar_chart(chart_data)

    # Convert wide-form data to long-form
    # See: https://altair-viz.github.io/user_guide/data.html#long-form-vs-wide-form-data
    data = pd.melt(chart_data.reset_index(), id_vars=["index"])

    # Horizontal stacked bar chart
    chart = (
        alt.Chart(data)
        .mark_bar()
        .encode(
            x=alt.X("value", type="quantitative", title="Score"),
            y=alt.Y("index", type="nominal", title="Players"),
            color=alt.Color("variable", type="nominal", title=""),
            order=alt.Order("variable", sort="descending"),
        )
    )

    st.altair_chart(chart, use_container_width=True)
    
    
    import json
    st.write( "<h4 style='color: white;' >" +"Levels :" + json.dumps({x[0] : x[2] for x in st.session_state["fetchedData"]}) +"</h4>",unsafe_allow_html=True )


    
drawChart()
time.sleep(1)
st.rerun()




