# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 20:39:36 2023

@author: acer
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def read_data(filename, indicator_code, country_codes):
    df = pd.read_excel(filename, skiprows=3)
    df1 = df.loc[(df['Indicator Code'] == indicator_code) & (df['Country Code'].isin(country_codes))]
    df1.set_index('Country Name', inplace=True)
    # Remove unnecessary columns and transpose
    df1 = df1.drop(columns = ['Country Code', 'Indicator Code', 'Indicator Name'])
    df1_transposed = df1.T
    return df1, df1_transposed
Population, Population_transposed = read_data(r'C:\Users\acer\OneDrive - University of Hertfordshire\Assignment\Applied data science\Assignment 2\API_19_DS2_en_excel_v2_4903056.xls', 'SP.POP.TOTL', ['VNM', 'BGD', 'PAK', 'ARE', 'AUS','BRA','ESP','FRA', 'GBR'])
Population_line_plot = Population_transposed.loc[[str(i) for i in range(1990,2021)]].plot()
Population_line_plot = Population_line_plot.legend(loc='upper left',fontsize='small', frameon=False)
plt.show()
Population_bar_plot = Population_transposed.loc[['1995','2000','2005','2010','2015','2020']].plot(kind='bar', figsize=(10, 6), rot=45)
Population_bar_plot.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))
plt.show()
