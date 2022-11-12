# evaluate an ridge regression model on the dataset
from numpy import mean
from numpy import std
from numpy import absolute
import numpy as np
import matplotlib.pyplot as plt
import seaborn
import tensorflow as tf
import pandas as pd
import streamlit as st
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedKFold
from sklearn.linear_model import Ridge




st.title("Happiness Rank Prediction")

df = pd.read_csv(r"C:\Users\DevenShah\Desktop\test\SunHacks2022\main_model\2015_modified2.csv")

df.head()

new_df = df.drop(['Standard Error','Dystopia Residual'],axis = 'columns')

new_df.head()

x = new_df.iloc[:,3:]
y = new_df.iloc[:,2]


from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)
regressor.fit(x, y)

gdb = st.number_input("Enter GDP per capita:",min_value=0.0,max_value=5.0,step=1e-6,format="%.5f")
hlth = st.number_input("Enter Health (Life Expectancy):",min_value=0.0,max_value=5.0,step=1e-6,format="%.5f")
fdom = st.number_input("Enter Freedom:",min_value=0.0,max_value=5.0,step=1e-6,format="%.5f")
ss = st.number_input("Enter Social Support:",min_value=0.0,max_value=5.0,step=1e-6,format="%.5f")
cp = st.number_input("Enter Corruption Perception:",min_value=0.0,max_value=5.0,step=1e-6,format="%.5f")
gn = st.number_input("Enter Generosity:",min_value=0.0,max_value=5.0,step=1e-6,format="%.5f")
music1 = st.number_input("Enter Music value(0 - Energetic,1 - Relaxing,2 - Happy,3 - Sad,4 - Aggressive):",min_value=0.0,max_value=5.0,step=1e-6,format="%.5f")
model1 = regressor.predict([[gdb,hlth,fdom,ss,cp,gn,music1]])
st.button("Predict")
#list_data = [model1]
st.write("Happiness Rank is",model1)

standard_dev_gdp = new_df['Economy (GDP per Capita)'].mean()*100
std_dev_health = new_df['Health (Life Expectancy)'].mean()*100
std_freedom = new_df['Freedom'].mean()*100
std_family = new_df['Family'].mean()*100
std_gov_corruption = new_df['Trust (Government Corruption)'].mean()*100
std_generosity = new_df['Generosity'].mean()*100

import pandas as pd
df=pd.read_csv(r'C:\Users\DevenShah\Desktop\test\SunHacks2022\main_model\happyindex.csv')
df.rename( columns={'Unnamed: 0':'Attributes'}, inplace=True )
#gdb = st.number_input("Enter GDP per capita:")
#hlth = st.number_input("Enter Health (Life Expectancy):")
#fdom = st.number_input("Enter Freedom:")
#ss = st.number_input("Enter Social Support:")
#cp = st.number_input("Enter Corruption Perception:")
#gn = st.number_input("Enter Generosity:")
arr_gdb=[]
arr_hlth=[]
arr_fdom=[]
arr_ss=[]
arr_cp=[]
arr_gn=[]

if(gdb<standard_dev_gdp):

    for i in df["GDP"]:
        if(df.iat[0,i]==1):
            
            arr_gdb.append("yes")
            
        else:
            arr_gdb.append("no")

if(hlth<std_dev_health):
    for i in df["Health"]:
        if(df.iat[0,i]==1):
            arr_hlth.append("yes")
            
        else:
            arr_hlth.append("no")
        
   

if(fdom<std_freedom):
    for i in df["Freedom"]:
        if(df.iat[0,i]==1):
            arr_fdom.append("yes")
            
        else:
            arr_fdom.append("no")
         
               
if(ss<std_family):
    for i in df["Social Support"]:
        if(df.iat[0,i]==1):
            arr_ss.append("yes")
            
        else:
            arr_ss.append("no")
            

if(cp<std_gov_corruption):
    for i in df["Corruption"]:
        if(df.iat[0,i]==1):
            arr_cp.append("yes")
        else:
            arr_cp.append("no")   


if(gn<std_generosity):
    for i in df["Generosity"]:
        if(df.iat[0,i]==1):
            arr_gn.append("yes")
        
        else:
            arr_gn.append("no")
               
  
st.markdown("<h3 style='text-align: center; color: white;'>-----Recommendations-----</h3>", unsafe_allow_html=True)

st.markdown("<h5 color: white;'>Gross Domestic Product</h5>", unsafe_allow_html=True)
print("These are the recommendation:-")
if(gdb<3):
    if arr_gn[0]=="yes":
        st.write("----Listen to Music")
    if arr_gn[1]=="yes":
        st.write("----Colour therapy recommended")
    if arr_gn[2]=="yes":
        st.write("----Regular Exercise")
    if arr_gn[3]=="yes":
        st.write("----Solving puzzles(sudoku,crosswords,mazes etc)")
    if arr_gn[4]=="yes":
        st.write("----Have a healthy diet")
    if arr_gn[5]=="yes":
        st.write("----Practice self affirmations")
    if arr_gn[6]=="yes":
        st.write("----Communicate with friends and family")
    if arr_gn[7]=="yes":
        st.write("----Explore your hobbies/interests")
    if arr_gn[8]=="yes":
        st.write("----Smile:)")


elif(hlth<3):
    st.markdown("<h5 color: white;'>Health</h5>", unsafe_allow_html=True)
    st.write("These are the recommendation:-")
    if arr_hlth[0]=="yes":
        st.write("----Listen to Music")
    if arr_hlth[1]=="yes":
        st.write("----Colour therapy recommended")
    if arr_hlth[2]=="yes":
        st.write("----Regular Exercise")
    if arr_hlth[3]=="yes":
        st.write("----Solving puzzles(sudoku,crosswords,mazes etc)")
    if arr_hlth[4]=="yes":
        st.write("----Have a healthy diet")
    if arr_hlth[5]=="yes":
        st.write("----Practice self affirmations")
    if arr_hlth[6]=="yes":
        st.write("----Communicate with friends and family")
    if arr_hlth[7]=="yes":
        st.write("----Explore your hobbies/interests")
    if arr_hlth[8]=="yes":
        st.write("----Smile:)")


elif(fdom<3):
    st.markdown("<h5 color: white;'>Freedom</h5>", unsafe_allow_html=True)
    st.write("These are the recommendation:-")  
    if arr_fdom[0]=="yes":
        st.write("----Listen to Music")
    if arr_fdom[1]=="yes":
        st.write("----Colour therapy recommended")
    if arr_fdom[2]=="yes":
        st.write("----Regular Exercise")
    if arr_fdom[3]=="yes":
        st.write("----Solving puzzles(sudoku,crosswords,mazes etc)")
    if arr_fdom[4]=="yes":
        st.write("----Have a healthy diet")
    if arr_fdom[5]=="yes":
        st.write("----Practice self affirmations")
    if arr_fdom[6]=="yes":
        st.write("----Communicate with friends and family")
    if arr_fdom[7]=="yes":
        st.write("----Explore your hobbies/interests")
    if arr_fdom[8]=="yes":
        st.write("----Smile:)")


elif(ss<3):
    st.markdown("<h5 color: white;'>Soical Support</h5>", unsafe_allow_html=True)
    st.write("These are the recommendation:-")
    if arr_ss[0]=="yes":
        st.write("----Listen to Music")
    if arr_ss[1]=="yes":
        st.write("----Colour therapy recommended")
    if arr_ss[2]=="yes":
        st.write("----Regular Exercise")
    if arr_ss[3]=="yes":
        st.write("----Solving puzzles(sudoku,crosswords,mazes etc)")
    if arr_ss[4]=="yes":
        st.write("----Have a healthy diet")
    if arr_ss[5]=="yes":
        st.write("----Practice self affirmations")
    if arr_ss[6]=="yes":
        st.write("----Communicate with friends and family")
    if arr_ss[7]=="yes":
        st.write("----Explore your hobbies/interests")
    if arr_ss[8]=="yes":
        st.write("----Smile:)")


elif(cp<3):
    st.markdown("<h5 color: white;'>Corruption</h5>", unsafe_allow_html=True)
    st.write("These are the recommendation:-")
    if arr_cp[0]=="yes":
        st.write("----Listen to Music")
    if arr_cp[1]=="yes":
        st.write("----Colour therapy recommended")
    if arr_cp[2]=="yes":
        st.write("----Regular Exercise")
    if arr_cp[3]=="yes":
        st.write("----Solving puzzles(sudoku,crosswords,mazes etc)")
    if arr_cp[4]=="yes":
        st.write("----Have a healthy diet")
    if arr_cp[5]=="yes":
        st.write("----Practice self affirmations")
    if arr_cp[6]=="yes":
        st.write("----Communicate with friends and family")
    if arr_cp[7]=="yes":
        st.write("----Explore your hobbies/interests")
    if arr_cp[8]=="yes":
        st.write("----Smile:)")


elif(gn<3):
    st.markdown("<h5 color: white;'>Generosity</h5>", unsafe_allow_html=True)
    st.write("These are the recommendation:-")
    if arr_gn[0]=="yes":
        st.write("----Listen to Music")
    if arr_gn[1]=="yes":
        st.write("----Colour therapy recommended")
    if arr_gn[2]=="yes":
        st.write("----Regular Exercise")
    if arr_gn[3]=="yes":
        st.write("----Solving puzzles(sudoku,crosswords,mazes etc)")
    if arr_gn[4]=="yes":
        st.write("----Have a healthy diet")
    if arr_gn[5]=="yes":
        st.write("----Practice self affirmations")
    if arr_gn[6]=="yes":
        st.write("----Communicate with friends and family")
    if arr_gn[7]=="yes":
        st.write("----Explore your hobbies/interests")
    if arr_gn[8]=="yes":
        st.write("----Smile:)")
else:
    print("")