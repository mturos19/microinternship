import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
df = pd.read_csv('GDP.csv')
df = df.drop(['Country Code', 'Indicator Name', 'Indicator Code'],axis=1)
def graph(countries):
    y = df['Country Name'].isin(countries)
    x = df[y].transpose()[1:].columns
    fil = df.T.loc[:,x]       
    fil.columns = fil.iloc[0]
    data = fil.drop(['Country Name'],axis = 0)   
    fig = px.line(data,labels={'index':'Year','Value':'GDP'})
    fig.show()
    

countries = ['Germany','Italy','United Kingdom','France','Aruba']
graph(countries)













