import pandas as pd
import plotly.express as px

file=pd.read_csv('data.csv')
fig=px.scatter(file,x='Population',y='Per capita',size='Percentage',color='Country',size_max=60)
fig.show()