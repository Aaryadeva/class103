import pandas as pd
import plotly.express as px

file=pd.read_csv('data.csv')
fig=px.bar(file,x='Country',y='InternetUsers')
fig.show()