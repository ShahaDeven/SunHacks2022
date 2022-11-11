df=pd.read_csv('happyindex.csv')
df.rename( columns={'Unnamed: 0':'Attributes'}, inplace=True )
gdb=int(input())
hlth=int(input())
fdom=int(input())
ss=int(input())
cp=int(input())
gn=int(input())
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

elif(hlth<std_dev_health):
    for i in df["Health"]:
        if(df.iat[0,i]==1):
            arr_hlth.append("yes")
            
        else:
            arr_hlth.append("no")
        
   

elif(fdom<std_freedom):
    for i in df["Freedom"]:
        if(df.iat[0,i]==1):
            arr_fdom.append("yes")
            
        else:
            arr_fdom.append("no")
         
               
elif(ss<std_family):
    for i in df["Social Support"]:
        if(df.iat[0,i]==1):
            arr_ss.append("yes")
            
        else:
            arr_ss.append("no")
            

elif(cp<std_gov_corruption):
    for i in df["Corruption"]:
        if(df.iat[0,i]==1):
            arr_cp.append("yes")
        else:
            arr_cp.append("no")   


elif(gn<std_generosity):
    for i in df["Generosity"]:
        if(df.iat[0,i]==1):
            arr_gn.append("yes")
        
        else:
            arr_gn.append("no")
               
  
print("-----Recommendations-----")
print("Gross Domestic Product")
print("These are the recommendation:-")
if(gdb<standard_dev_gdp):
    if arr_gn[0]=="yes":
         print("Listen to Music")
    if arr_gn[1]=="yes":
        print("Colour therapy recommended")
    if arr_gn[2]=="yes":
        print("Regular Exercise")
    if arr_gn[3]=="yes":
        print("Solving puzzles(sudoku,crosswords,mazes etc)")
    if arr_gn[4]=="yes":
        print("Have a healthy diet")
    if arr_gn[5]=="yes":
        print("Practice self affirmations")
    if arr_gn[6]=="yes":
        print("Communicate with friends and family")
    if arr_gn[7]=="yes":
        print("Explore your hobbies/interests")
    if arr_gn[8]=="yes":
        print("Smile:)")

print("\nHealth")
print("These are the recommendation:-")
if(hlth<std_dev_health):
    if arr_hlth[0]=="yes":
         print("Listen to Music")
    if arr_hlth[1]=="yes":
        print("Colour therapy recommended")
    if arr_hlth[2]=="yes":
        print("Regular Exercise")
    if arr_hlth[3]=="yes":
        print("Solving puzzles(sudoku,crosswords,mazes etc)")
    if arr_hlth[4]=="yes":
        print("Have a healthy diet")
    if arr_hlth[5]=="yes":
        print("Practice self affirmations")
    if arr_hlth[6]=="yes":
        print("Communicate with friends and family")
    if arr_hlth[7]=="yes":
        print("Explore your hobbies/interests")
    if arr_hlth[8]=="yes":
        print("Smile:)")

print("\nFreedom")
print("These are the recommendation:-")
if(fdom<std_freedom):
    if arr_fdom[0]=="yes":
         print("Listen to Music")
    if arr_fdom[1]=="yes":
        print("Colour therapy recommended")
    if arr_fdom[2]=="yes":
        print("Regular Exercise")
    if arr_fdom[3]=="yes":
        print("Solving puzzles(sudoku,crosswords,mazes etc)")
    if arr_fdom[4]=="yes":
        print("Have a healthy diet")
    if arr_fdom[5]=="yes":
        print("Practice self affirmations")
    if arr_fdom[6]=="yes":
        print("Communicate with friends and family")
    if arr_fdom[7]=="yes":
        print("Explore your hobbies/interests")
    if arr_fdom[8]=="yes":
        print("Smile:)")

print("\nSocial Support")
print("These are the recommendation:-")
if(ss<std_family):
    if arr_ss[0]=="yes":
         print("Listen to Music")
    if arr_ss[1]=="yes":
        print("Colour therapy recommended")
    if arr_ss[2]=="yes":
        print("Regular Exercise")
    if arr_ss[3]=="yes":
        print("Solving puzzles(sudoku,crosswords,mazes etc)")
    if arr_ss[4]=="yes":
        print("Have a healthy diet")
    if arr_ss[5]=="yes":
        print("Practice self affirmations")
    if arr_ss[6]=="yes":
        print("Communicate with friends and family")
    if arr_ss[7]=="yes":
        print("Explore your hobbies/interests")
    if arr_ss[8]=="yes":
        print("Smile:)")

print("\nCorruption")
print("These are the recommendation:-")
if(cp<std_gov_corruption):
    if arr_cp[0]=="yes":
         print("Listen to Music")
    if arr_cp[1]=="yes":
        print("Colour therapy recommended")
    if arr_cp[2]=="yes":
        print("Regular Exercise")
    if arr_cp[3]=="yes":
        print("Solving puzzles(sudoku,crosswords,mazes etc)")
    if arr_cp[4]=="yes":
        print("Have a healthy diet")
    if arr_cp[5]=="yes":
        print("Practice self affirmations")
    if arr_cp[6]=="yes":
        print("Communicate with friends and family")
    if arr_cp[7]=="yes":
        print("Explore your hobbies/interests")
    if arr_cp[8]=="yes":
        print("Smile:)")

print("\nGenerosity")
print("These are the recommendation:-")
if(gn<std_generosity):
    if arr_gn[0]=="yes":
         print("Listen to Music")
    if arr_gn[1]=="yes":
        print("Colour therapy recommended")
    if arr_gn[2]=="yes":
        print("Regular Exercise")
    if arr_gn[3]=="yes":
        print("Solving puzzles(sudoku,crosswords,mazes etc)")
    if arr_gn[4]=="yes":
        print("Have a healthy diet")
    if arr_gn[5]=="yes":
        print("Practice self affirmations")
    if arr_gn[6]=="yes":
        print("Communicate with friends and family")
    if arr_gn[7]=="yes":
        print("Explore your hobbies/interests")
    if arr_gn[8]=="yes":
        print("Smile:)")