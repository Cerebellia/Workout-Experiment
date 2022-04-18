import streamlit as st
import pandas as pd
def get_change(current, previous):
    if current == previous:
        return 100.0
    try:
        return ((current - previous) / previous) * -100.0
    except ZeroDivisionError:
        return 0
df = pd.read_csv("./Tremors.csv")
# df["startDate"] = pd.to_datetime(df['startDate'], unit='s')
# df["endDate"] = pd.to_datetime(df['endDate'], unit='s')
beforeWorkout = df[df["startDate"] < 671907360]
afterWorkout = df[df["startDate"] > 671910660]

valuesBefore = []
valuesAfter = []

avgDF = pd.DataFrame()
allCols = {"mild","moderate","none","slight", "strong"}

before = []
after = []
for col in allCols:
  
        with st.beta_expander(label=col):
                
                st.subheader("BEFORE")
                st.text(beforeWorkout[col].mean())
                st.line_chart(beforeWorkout[col])

                before.append(beforeWorkout[col].mean())

                st.subheader("AFTER")
                st.text(afterWorkout[col].mean())
                st.line_chart(afterWorkout[col])

                data = [beforeWorkout[col].mean(), afterWorkout[col].mean()]
                st.header(get_change(beforeWorkout[col].mean(), afterWorkout[col].mean()))
                
# avgDF["before"] = valuesBefore
# avgDF["after"] = valuesAfter
# highestColBefore = max(before)
# highestColAfter = max(after)



# st.subheader("Before: " + str(before))
# st.subheader("After: " + str(after))
st.table(df)

