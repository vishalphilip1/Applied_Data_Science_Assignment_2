# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 20:39:36 2023

@author: acer
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 20:39:36 2023

@author: acer
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns

def read_data(filename, indicator_code, country_codes):
    df = pd.read_excel(filename, skiprows=3)
    df1 = df.loc[(df['Indicator Code'] == indicator_code) & (df['Country Code'].isin(country_codes))]
    df1.dropna(how='all', axis=1, inplace=True)
    df1.set_index('Country Name', inplace=True)
    # Remove unnecessary columns and transpose
    df1 = df1.drop(columns = ['Country Code', 'Indicator Code', 'Indicator Name'])
    df1_transposed = df1.T
    return df1, df1_transposed

def country_data(filename, country_code, indicator_code ):
    data = pd.read_excel(filename, skiprows=3)
    data = data.loc[(data['Country Code'] == country_code) & (data['Indicator Code'].isin(indicator_code))]
    data.dropna(how='all', axis=1, inplace=True)
    data.set_index('Indicator Name', inplace=True)
    country = data.drop(columns = ['Country Code', 'Indicator Code', 'Country Name'])   
    return country


Green_House_Gas_Emission, Green_House_Gas_Emission_T  = read_data("API_19_DS2_en_excel_v2_4903056.xls", 'EN.ATM.GHGT.KT.CE', ['AUT', 'BEL', 'CHE', 'DEU', 'DNK','FIN','ESP','FRA', 'GBR', 'GRC'])
CO_Emission, CO_Emission_T  = read_data("API_19_DS2_en_excel_v2_4903056.xls", 'EN.ATM.CO2E.KT', ['AUT', 'BEL', 'CHE', 'DEU', 'DNK','FIN','ESP','FRA', 'GBR', 'GRC'])
Methane_Emission, Methane_Emission_T  = read_data("API_19_DS2_en_excel_v2_4903056.xls", 'EN.ATM.METH.KT.CE', ['AUT', 'BEL', 'CHE', 'DEU', 'DNK','FIN','ESP','FRA', 'GBR','GRC'])

Germany = country_data("API_19_DS2_en_excel_v2_4903056.xls", 'DEU',['EN.ATM.GHGT.KT.CE','EN.ATM.CO2E.KT','EN.ATM.NOXE.KT.CE','EN.ATM.METH.KT.CE']).T
United_Kingdom  = country_data("API_19_DS2_en_excel_v2_4903056.xls", 'GBR',['EN.ATM.GHGT.KT.CE','EN.ATM.CO2E.KT', 'EN.ATM.GHGT.KT.CE', 'EN.ATM.NOXE.KT.CE','EN.ATM.METH.KT.CE']).T

GE_line_plot = Green_House_Gas_Emission_T.plot(figsize=(10, 6))
plt.title("Total Green House Emission")
plt.xlabel("Year")
plt.ylabel("kt of CO2 equivalent")
GE_line_plot.legend(loc='upper right', bbox_to_anchor=(1.23, 1.0))
plt.show()

CO_line_plot = CO_Emission_T.plot(figsize=(10, 6))
plt.title("Carbon dioxide emission")
plt.xlabel("Year")
plt.ylabel("kiloton")
CO_line_plot.legend(loc='upper right', bbox_to_anchor=(1.23, 1.0))
plt.show()

ME_line_plot = Methane_Emission_T.plot(figsize=(10, 6))
plt.title("Methane Emission")
plt.xlabel("Year")
plt.ylabel("Methane emissions (kt of CO2 equivalent)")
ME_line_plot.legend(loc='upper right', bbox_to_anchor=(1.23, 1.0))
plt.show()

GH_bar_plot = Green_House_Gas_Emission_T.loc[['1990','2000','2005','2010','2015']].plot(kind='bar', figsize=(10, 6), rot=45)
GH_bar_plot.legend(loc='upper right', bbox_to_anchor=(1.23, 1.0))
plt.title("Total Green House Emission")
plt.xlabel("Year")
plt.ylabel("kt of CO2 equivalent")
plt.show()

print("Total Green House Gas Emission \n" ,Green_House_Gas_Emission_T.describe())
print("Total Green House Gas Emission Minimum values \n", Green_House_Gas_Emission_T.describe().loc["min"])
print("Total Green House Gas Emission Maximum values \n", Green_House_Gas_Emission_T.describe().loc["max"])
print("Carbon Dioxide Emission \n" , CO_Emission_T.describe())
print("Carbon Dioxide Emission Minimum values \n", CO_Emission_T.describe().loc["min"])
print("Carbon Dioxide Emission Maximum values \n", Green_House_Gas_Emission_T.describe().loc["max"])
print("Methane Emission \n" , Methane_Emission.describe())
print("Methane Emission Minimum values \n", Methane_Emission.describe().loc["min"])
print("Methane Emission Maximum values \n", Methane_Emission.describe().describe().loc["max"])


print("Total Green House Emission Skewness")
print("Germany :", stats.skew(Green_House_Gas_Emission_T["Germany"]))
print("United Kingdom :", stats.skew(Green_House_Gas_Emission_T["United Kingdom"]))
print("Switzerland :", stats.skew(Green_House_Gas_Emission_T["Switzerland"]))
print("France :", stats.skew(Green_House_Gas_Emission_T["France"]))
print("Spain :", stats.skew(Green_House_Gas_Emission_T["Spain"]))
print("Total Green House Emission Kurtosis")
print("Germany :", stats.kurtosis(Green_House_Gas_Emission_T["Germany"]))
print("United Kingdom :", stats.kurtosis(Green_House_Gas_Emission_T["United Kingdom"]))
print("Switzerland :", stats.kurtosis(Green_House_Gas_Emission_T["Switzerland"]))
print("France :", stats.kurtosis(Green_House_Gas_Emission_T["France"]))
print("Spain :", stats.kurtosis(Green_House_Gas_Emission_T["Spain"]))

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
plt.title("Heatmap of Germany", fontsize=25)
plt.show()

United_Kingdom_cor = United_Kingdom.corr()
fig, ax = plt.subplots(figsize=(12, 10))
sns.heatmap(United_Kingdom_cor, cmap='YlGnBu')
# Split the indicator names into two lines
ticklabels = [name.get_text().split(' ') for name in ax.get_xticklabels()]
new_ticklabels = []
for names in ticklabels:
    new_ticklabels.append('\n'.join(names))
    
# Set the modified ticklabels on the x-axis
ax.set_xticklabels(new_ticklabels)
plt.title("Heatmap of United Kingdom", fontsize=25)
plt.show()

