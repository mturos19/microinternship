import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('gdp_csv.csv')
def plot_gdp(countries):
    #Slice and create the dataframes
    filtered_df = df[df['Country Name'].isin(countries)]
    pivot_df = filtered_df.pivot(index='Year', columns='Country Name', values='Value')
    pivot_df.plot()

    plt.xlabel('Year')
    plt.ylabel('GDP')
    plt.title('GDP Comparison')

    plt.legend()
    plt.show()


countries_list=['United Kingdom', 'Italy', 'France', 'Germany']
plot_gdp(countries_list)


import plotly.express as px

df_map=df 

fig = px.choropleth(df_map, locations="Country Name",
                    color="Value", 
                    locationmode='country names',
                    color_continuous_scale=px.colors.sequential.Plasma,
                    animation_frame="Year",
                    range_color=(0, 3.5E12))
fig.show()
