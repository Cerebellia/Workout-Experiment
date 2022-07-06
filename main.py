import streamlit as st
import pandas as pd
def get_change(current, previous):
    if current == previous:
        return 100.0
    try:
        return ((current - previous) / previous) * -100.0
    except ZeroDivisionError:
        return 0
df = pd.read_json("./Tremor.json")
df["startDate"] = pd.to_datetime(df['startDate'], unit='s')
df["endDate"] = pd.to_datetime(df['endDate'], unit='s')

dfBefore = df[df["startDate"].dt.hour > 12]
dfAfter = df[df["startDate"].dt.hour < 12]


valuesBefore = []
valuesAfter = []

avgDF = pd.DataFrame()
allCols = {"mild","moderate","none","slight", "strong"}

before = []
after = []
for col in allCols:
        
        with st.expander(label=col):
                
                st.subheader("BEFORE")
                st.text(dfBefore[col].mean())
            
                st.line_chart(dfBefore[col])

                before.append(dfBefore[col].mean())

                st.subheader("AFTER")
                st.text(dfAfter[col].mean())
            
                st.line_chart(dfAfter[col])

                after.append(dfAfter[col].mean())

        
                


dfValues = pd.DataFrame()
dfValues["strong"] =  df["strong"]
dfValues["mild"]  = df["mild"]
dfValues["none"]  = df["none"]
dfValues["slight"]  = df["slight"]

df["Dominate_Value"] = dfValues.idxmax(axis = 1)
st.subheader("Before: " + str(before))
st.subheader("After: " + str(after))
st.table(df)

