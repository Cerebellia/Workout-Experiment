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
  
        #with st.beta_expander(label=col):
                
                print("BEFORE")
                print(beforeWorkout[col].mean())
                

                before.append(beforeWorkout[col].mean())

                print("AFTER")
                print(afterWorkout[col].mean())
                print(afterWorkout[col])

                data = [beforeWorkout[col].mean(), afterWorkout[col].mean()]
                print(get_change(beforeWorkout[col].mean(), afterWorkout[col].mean()))
                


