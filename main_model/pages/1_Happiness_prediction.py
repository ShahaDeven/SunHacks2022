import numpy as np
import matplotlib.pyplot as plt
import seaborn
import tensorflow as tf
import pandas as pd
import streamlit as st



st.title("Happiness Rank Prediction")

df = pd.read_csv(r"C:\Users\DevenShah\Desktop\test\SunHacks2022\main_model\2015_modified2.csv")

df.head()

new_df = df.drop(['Country','Region','Standard Error','Dystopia Residual'],axis = 'columns')

new_df.head()

x = new_df.iloc[:,3:]
y = new_df.iloc[:,1]
print(x)

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)
regressor.fit(x, y)

model1 = regressor.predict([[1.37561,1.40223,0.93284,0.63376,0.90444,0.99005,0]])
print(model1)
#list_data = [model1]
st.write("Happiness Rank is",model1)
gdb = 1.37561
hlth = 1.40223
fdom = 0.93284
ss = 0.63376
cp = 0.90444
gn = 0.99005

standard_dev_gdp = new_df['Economy (GDP per Capita)'].mean()*100
std_dev_health = new_df['Health (Life Expectancy)'].mean()*100
std_freedom = new_df['Freedom'].mean()*100
std_family = new_df['Family'].mean()*100
std_gov_corruption = new_df['Trust (Government Corruption)'].mean()*100
std_generosity = new_df['Generosity'].mean()*100

import pandas as pd
df=pd.read_csv(r'C:\Users\DevenShah\Desktop\test\SunHacks2022\main_model\happyindex.csv')
df.rename( columns={'Unnamed: 0':'Attributes'}, inplace=True )
gdb = 1.37561
hlth = 1.40223
fdom = 0.93284
ss = 0.63376
cp = 0.90444
gn = 0.99005
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