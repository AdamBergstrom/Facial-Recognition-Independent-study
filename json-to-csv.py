import json
import pandas as pd
from pandas.io.json import json_normalize

#load json object
with open('./test.json') as f:
    d = json.load(f)

results = json_normalize(d['FaceDetails'])
df = results
landmarks=d['FaceDetails'][0]['Landmarks']

# loop over all landmark types
for type in landmarks:
    # create a column with 'X' appended and the corresponding x value
    df['{}X'.format(type['Type'])] = type['X']
    # create a column with 'Y' appended and the corresponding y value
    df['{}Y'.format(type['Type'])] = type['Y']

# removes the nested duplicate data
df = df.drop(columns=['Landmarks'])

# send to csv
df.to_csv('test.csv')
