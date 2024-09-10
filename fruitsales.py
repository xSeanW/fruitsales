import pandas as pd

data = {
    "Apples" : [35, 41],
    "Bananas" : [21, 34]
}

df = pd.DataFrame(data, index=['2017 Sales', '2018 Sales'])

df.to_csv('fruit.csv')

print(df)