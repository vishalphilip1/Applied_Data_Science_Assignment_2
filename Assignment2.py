# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 20:39:36 2023

@author: acer
"""

import numpy as np
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns

`
def read_data(filename, indicator_code, country_codes):
    df = pd.read_excel(filename, skiprows=3)
    df1 = df.loc[(df['Indicator Code'] == indicator_code) & (df['Country Code'].isin(country_codes))]
    df1.dropna(how='all', axis=1, inplace=True)
    df1.set_index('Country Name', inplace=True)
    # Remove unnecessary columns and transpose
    df1 = df1.drop(columns = ['Country Code', 'Indicator Code', 'Indicator Name'])
    df1_transposed = df1.T
    return df1, df1_transposed
Population, Population_transposed = read_data("API_19_DS2_en_excel_v2_4903056.xls", 'SP.POP.TOTL', ['AUT', 'BEL', 'CHE', 'DEU', 'DNK','FIN','ESP','FRA', 'GBR', 'GRC'])

def read_data1(filename, country_code, indicator_code ):
    dfs = pd.read_excel(filename, skiprows=3)
    df5 = dfs.loc[(dfs['Country Code'] == country_code) & (dfs['Indicator Code'].isin(indicator_code))]
    #df5 = df5[(df5['Year'] >= 1990) & (df5['Year'] <= 2020)]
    df5.dropna(how='all', axis=1, inplace=True)
    df5.set_index('Indicator Name', inplace=True)
    df5 = df5.drop(columns = ['Country Code', 'Indicator Code', 'Country Name'])
    
    return df5

Population, Population_transposed = read_data("API_19_DS2_en_excel_v2_4903056.xls", 'SP.POP.TOTL', ['AUT', 'BEL', 'CHE', 'DEU', 'DNK','FIN','ESP','FRA', 'GBR','GRC'])
Green_House_Gas_Emission, Green_House_Gas_Emission_T  = read_data("API_19_DS2_en_excel_v2_4903056.xls", 'EN.ATM.GHGT.KT.CE', ['AUT', 'BEL', 'CHE', 'DEU', 'DNK','FIN','ESP','FRA', 'GBR', 'GRC'])
CO_Emission, CO_Emission_T  = read_data("API_19_DS2_en_excel_v2_4903056.xls", 'EN.ATM.CO2E.KT', ['AUT', 'BEL', 'CHE', 'DEU', 'DNK','FIN','ESP','FRA', 'GBR', 'GRC'])
NO_Emission, NO_Emission_T  = read_data("API_19_DS2_en_excel_v2_4903056.xls", 'EN.ATM.NOXE.KT.CE', ['AUT', 'BEL', 'CHE', 'DEU', 'DNK','FIN','ESP','FRA', 'GBR','GRC'])
Methane_Emission, Methane_Emission_T  = read_data("API_19_DS2_en_excel_v2_4903056.xls", 'EN.ATM.METH.KT.CE', ['AUT', 'BEL', 'CHE', 'DEU', 'DNK','FIN','ESP','FRA', 'GBR','GRC'])

Germany =read_data1("API_19_DS2_en_excel_v2_4903056.xls", 'DEU',['EN.ATM.GHGT.KT.CE','EN.ATM.CO2E.KT','EN.ATM.NOXE.KT.CE','EN.ATM.METH.KT.CE']).T
Greece =read_data1("API_19_DS2_en_excel_v2_4903056.xls", 'GRC',['EN.ATM.GHGT.KT.CE','EN.ATM.CO2E.KT', 'EN.ATM.GHGT.KT.CE', 'EN.ATM.NOXE.KT.CE','EN.ATM.METH.KT.CE']).T

GS_line_plot = Green_House_Gas_Emission_T.loc[[str(i) for i in range(1990,2020)]].plot()
plt.title("Green House Emission")
#GS_line_plot = Population_line_plot.legend(loc='upper left',fontsize='small', frameon=False)
CO_line_plot = CO_Emission_T.loc[[str(i) for i in range(1990,2020)]].plot()
plt.title("carbon dioxide emission")
#CO_line_plot = Population_line_plot.legend(loc='upper left',fontsize='small', frameon=False)
NO_line_plot = NO_Emission_T.loc[[str(i) for i in range(1990,2020)]].plot()
plt.title("Nitrogen_Oxide Emission")
plt.show()
ME_line_plot = Methane_Emission_T.loc[[str(i) for i in range(1990,2020)]].plot()
plt.title("Methane Emission")

GH_bar_plot = Green_House_Gas_Emission_T.loc[['1990','2000','2005','2010','2015']].plot(kind='bar', figsize=(10, 6), rot=45)
GH_bar_plot.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))
plt.title("Green House Emission")
CO_bar_plot = CO_Emission_T.loc[['1990','2000','2005','2010','2015']].plot(kind='bar', figsize=(10, 6), rot=45)
plt.title("Carbon Dioxide emission")
CO_bar_plot.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))
NO_plot = NO_Emission_T.loc[['1990','2000','2005','2010','2015']].plot(kind='bar', figsize=(10, 6), rot=45)
NO_plot.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))
plt.title("Nitrogen Oxide Emission")
ME_plot = Methane_Emission_T.loc[['1990','2000','2005','2010','2015']].plot(kind='bar', figsize=(10, 6), rot=45)
ME_plot.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))
plt.title("Methane Emission")
plt.show()

std = np.std(Green_House_Gas_Emission_T["Austria"])
print("Std. deviation:", std)
print("Skew:", stats.skew(Green_House_Gas_Emission_T["Austria"]))
print("Kurtosis", stats.kurtosis(Green_House_Gas_Emission_T["Austria"]))

Germany_cor = Germany.corr()
fig, ax = plt.subplots(figsize=(12, 10))
sns.heatmap(Germany_cor, cmap='YlGnBu')
# Split the indicator names into two lines
ticklabels = [name.get_text().split(' ') for name in ax.get_xticklabels()]
new_ticklabels = []
for names in ticklabels:
    new_ticklabels.append('\n'.join(names))
    
# Set the modified ticklabels on the x-axis
ax.set_xticklabels(new_ticklabels)

Greece_cor = Greece.corr()
sns.heatmap(Greece_cor, cmap='YlGnBu')
