import pandas as pd
data = {
    'name' : ['Rafy', 'Talha'],
    'Age' : [12, 54],
    'score' : [85, 84]
}
df = pd.DataFrame(data)
df['passed'] = df['score'] > 90
print(df)