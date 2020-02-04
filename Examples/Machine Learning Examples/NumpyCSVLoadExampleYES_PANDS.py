
#========================================================================================
#=====              METHOD 1 TO LOAD DATA FROM A CSV FILE WITH PANDAS           =========
#========================================================================================

#STEP 1 - IMPORT NUMPY AND PANDAS
import numpy as np
import pandas as pd

#STEP 2 - WE WILL READ THE CSV FILE USING PANDAS READ_CSV() METHOD

#Usualy pandas will read the header row whch contains columns names, so in this case since we dont have a header line
#       we will choose header = None
X =pd.read_csv('C:/Users/chen/PycharmProjects/PythonProjects/NumpyUdemy/linear_regression_class/data_2d.csv',
                    header=None)


#PLEASE DENOTE THE PANDAS RETURNS A DATA FRAME TYPE NOT NDARRAY, so in order to do numpy function a casting is required
#print(type(X))

#INFO METHOD IN PANADS - GIVES INFORMATION ON AN OBJECT
#print(X.info())

#HEAD METHOD IN PANDAS - GIVES THE FIRST 5 ROWS OF THE OBJECT
#print(X.head())
#TO WATCH MORE THAN 5 ROWS OF THE FILE WE WILL PUT THE NUMBER OF ROWS REQUESTED IN THE HEAD METHOd, IN THIS EXAMPLE 10
#print(X.head(10))

#================================================================================================
#==         REMEMBER PANDAS DONT WORK LIKE NUMPY, A CASTING IS REQUIRED FOR CALCULATIONS      ===
#==                                                                                           ===
#==         PLEASE NOTE:                                                                      ===
#==                       ON NUMPY X[0] = VALUES OF FIRST ROW (NDARRAY OBJECT)                ===
#==                       ON PANDAS X[0] =  VALUES OF THE FIRST COLUMN (SERIES OBJECTS        ===
#==                                                                                           ===
#================================================================================================

#ILOC = WILL GIVE THE INFORMATION ON THE FIRST ROW IN PANDAS
#print(X.iloc[0])
#print(X.loc[0])

#SYNTAX HOW TO VIEW MORE THEN ONE COL
#print(X[[0,2]])

#FILTERING ROWS BASED ON CRITERIA, IN THIS EXAMPLE ALL THE ROWS WHERE X[0]< 5
#print(X[X[0] < 5])

#IF WE WONT USE BRACTES WE WILL GET BOOLIAN RETURN IF THE VALUE IS TRUE OR FALSE BASED ON THE CRITERIA GIVER
#print(X[0] < 5)

#STEP 3 - AFTER LOADING THE DATA WE WILL CAST THE INFORMATION FROM PANADS DATA FRAME TO NUMPY ARRAY
#M =X.values
#print(type(M))
#print(M)

#===========================================================================================
#==         HOW TO CHANGE HEADER IN PANDAS TO CREATE COL NAMES?                         ====
#===========================================================================================

#STEP 1 - READ THE FILE IN PANDAS -
#           in this case we dont skip the header, but yes skip last 3 lines since there are not relevant
#           in order to skip footer we must put engine as python otherwise the defult is C, which we dont want
df =pd.read_csv('C:/Users/chen/PycharmProjects/PythonProjects/NumpyUdemy/airline/international-airline-passengers.csv',
                    engine="python", skipfooter=3)

#CHEKING THE COLUMNS NAMES
#print(df.columns)

#CHANGING COLUMNS NAMES
df.columns = ['month', 'passengers']
#print(df.columns)

#WATCH SPECIFIC COLUMN
#print(df['passengers'])
#WHEN COL NAMES ARE STRINGS WE CAN USE: df.passengers , THIS WONT WORK IF THE COL NAME HAS SPACES IN IT
#print(df.passengers)

#HOW TO ADD COL WITH FIXED VALUE, note this will by defult add the col from the right
#df['ones'] = 1
#HOW TO ADD COL WITH FIXED VALUE IN SPECIFIC COL PLACE :
#                                   df.insert(loc=location, column=name of col, value=the value to insert in the col)
df.insert(0, 'ones', 1)
#print(df.head())

#HOW TO INSERT COL TO DATA FRAME WITH DIFFERENT VALUES?
# WE WILL HAVE TO USE APPLY FUNCTION

#IN THIS EXAMPLE WE WILL TAKE THE MONTH VALUES AND ADD A NEW COL THAT WILL INSERT THE DAYTIME FOR A NEW COL
#First we need daytime
from datetime import datetime

#we check using strptime() to check it does what we want
#print(datetime.strptime("1949-05", "%Y-%m"))
#lets apply to the new col date
#df['date'] = df.apply(lambda row: datetime.strptime(row['month'], "%Y-%m"), axis=1)
df.insert(1, 'date', df.apply(lambda row: datetime.strptime(row['month'], "%Y-%m"), axis=1))
#print(df.head())


#===========================================================================================
#==                             JOINS METHOD                                            ====
#===========================================================================================

#HERE WE WILL LEARN TO JOIN DATA FROM TWO SEPRATE CSV FILE TO A USABLE MATRIX

#STEP 1 - OPEN THE TWO CSV FILES

t1 = df =pd.read_csv('C:/Users/chen/PycharmProjects/PythonProjects/NumpyUdemy/numpy_class/table1.csv',
                    engine="python")
t2 = df =pd.read_csv('C:/Users/chen/PycharmProjects/PythonProjects/NumpyUdemy/numpy_class/table2.csv',
                    engine="python")

#print(t1, t2)

#IN THIS EXAMPLE WE WANT TO JOIN ON THE USER_ID COL
#THE FUNCTION IN PANDAS THAT DOES THAT IS CALLED MERGE, ON ARG SPECIFY WHICH COL TO MERGE ON THE FILES
#IF WE DONT PUT ON, IT WILL JOIN THE ROW INDEX
#m = pd.merge(t1, t2, on='user_id')
#print(m)

#ALTTERNATIVE WAY TO MERGE
m =t1.merge(t2, on='user_id')
#print(m)
#print(type(m))

#NOW WE WILL CONVERT m(DATA FRAME) to a numpy.array
m = m.values
print(m)
print(type(m))