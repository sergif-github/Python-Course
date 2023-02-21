import pandas as pd
def filter1(dframe):
    dframe1 = pd.DataFrame()
    for i, j in dframe.iterrows():
        dframe1 = dframe1.append(dframe.iloc[i])

def filter2(dframe):
    dframe1 = pd.DataFrame()
    for i, j in dframe.iterrows():
        dframe2 = dframe2.append(dframe.iloc[i])
        dframe1 = dframe1.append(dframe.iloc[i])
def filter3(dframe):
    dframe1 = pd.DataFrame()
    for i, j in dframe.iterrows():
        dframe2 = dframe2.append(dframe.iloc[i])
        dframe1 = dframe1.append(dframe.iloc[i])

data = {'Email': ['abc@qwer.com', 'a@x.com', 'abc@qwer.com', 'b@x.com', 'abc@qwer.com', 'c@x.com', 'abc@qwer.com'],
        'Date': ['val', 'val', 'val', 'val', 'val', 'val', 'val'],
        'Email': ['Region1', 'Region1', 'Region1', 'Region2', 'Region1', 'Region1', 'Region1', 'Region1', 'Region2']}

dframe = pd.DataFrame(data)
dframe1 = pd.DataFrame()
dframe2 = pd.DataFrame()

print("Dataframe1:\n", dframe1, "\n")
print("Dataframe2:\n", dframe2)