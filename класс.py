import pandas as pd
import re



class Person:

    @staticmethod
    def calculate_age():
        excel_file = ".\Книга1.xlsx"
        df = pd.read_excel(excel_file)
        df['dob']=pd.to_datetime(df['dob']).astype("datetime64[ns]")
        df['dod']=pd.to_datetime(df['dod']).astype("datetime64[ns]")
        now=pd.Timestamp('now')
        mask=df['age'].isna()
        df.loc[mask,'age']=(df.loc[mask,'dod'].fillna(now)-df.loc[mask,'dob']).astype("<m8[Y]")
        print(df['age'])




    @staticmethod
    def load_from_file():
        a=pd.read_excel(".\Книга1.xlsx")
        print(a)





    @staticmethod
    def search():
        excel_file=".\Книга1.xlsx"
        df = pd.read_excel(excel_file)
        b = input("Search: ")
        k=0
        rows = []
        df['dob'] = pd.to_datetime(df['dob']).astype("datetime64[ns]")
        df['dod'] = pd.to_datetime(df['dod']).astype("datetime64[ns]")
        now = pd.Timestamp('now')
        mask = df['age'].isna()
        df.loc[mask, 'age'] = (df.loc[mask, 'dod'].fillna(now) - df.loc[mask, 'dob']).astype("<m8[Y]")
        for item in df["name"]:
            if re.search(b,item):
                rows.append(k)
            k = k + 1
        print(df.iloc[rows])

    def enter_data(self):
        row=[]
        k=0
        a=input()
        for item in df[".\Книга1.xlsx"]:
            if re.search(item):
                row.append(k)
            k=k+1

