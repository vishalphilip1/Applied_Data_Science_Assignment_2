"""
Created on Thu Mar 30 20:39:36 2023.

@author: Vishal Philip
Following script reads data from the Excel file to create
visualizations and summary statistics for greenhouse gas emissions,
carbon dioxide emissions, methane emissions for various countries over time.
It also plots lineplot, barplot and heatmap. For heatmap additional indicator
Nitrous Oxide is also added.
"""


import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns


def read_data(filename, indicator_code, country_codes):
    """Reads data from an Excel file, selects rows based on indicator code and
    country codes, drops unnecessary columns, and transposes the resulting data
    frame.

    Args:
    filename (str): name of Excel file
    indicator_code (str): indicator code to select rows by
    country_codes (list): list of country codes to select rows by

    Returns:
    tuple: two data frames, one in original format and one transposed
    """

    df = pd.read_excel(filename, skiprows=3)
    df1 = df.loc[(df['Indicator Code'] == indicator_code) &
                 (df['Country Code'].isin(country_codes))]
    df1.dropna(how='all', axis=1, inplace=True)
    df1.set_index('Country Name', inplace=True)
    # Remove unnecessary columns and transpose
    df1 = df1.drop(columns=['Country Code', 'Indicator Code',
                            'Indicator Name'])
    df1_transposed = df1.T
    return df1, df1_transposed


def plot(df, name):
    df.plot()
    plt.title(name, fontsize=16)
    plt.xlabel("Years", fontsize=16)
    plt.ylabel("kiloton", fontsize=16)
    plt.legend(loc='upper right', bbox_to_anchor=(1.37, 1.0))
    plt.show()
    return


def stati1(name, df):
    print(name + "\n", df.describe())
    # Printing minimum values of Total Green House Gas Emission time series
    print(name + " Minimum values \n", df.describe().loc["min"])
    print(name + " Maximum values \n", df.describe().loc["max"])
    return


def stati2(country_name):
    print("Total Green House Emission Skewness")
    print(country_name, stats.skew(Green_House_Gas_Emission_T[country_name]))
    print("Total Green House Emission Kurtosis")
    print(country_name,
          stats.kurtosis(Green_House_Gas_Emission_T[country_name]))
    return


def country_data(filename, country_code, indicator_code):
    """Reads data from an Excel file, selects rows based on country code and
    indicator codes, drops unnecessary columns, and returns the resulting data
    frame.

    Args:
filename (str): name of Excel file
    country_code (str): country code to select rows by
indicator_code (list): list of indicator codes to select rows by

Returns:
pandas.DataFrame: data frame with selected rows and columns
"""
    data = pd.read_excel(filename, skiprows=3)
    data = data.loc[(data['Country Code'] == country_code) &
                    (data['Indicator Code'].isin(indicator_code))]
    data.dropna(how='all', axis=1, inplace=True)
    data.set_index('Indicator Name', inplace=True)
    country = data.drop(columns=['Country Code',
                                 'Indicator Code', 'Country Name']).T
    return country


def heatmap(country_name, name):
    correlation = country_name.corr()
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(correlation, cmap='YlGnBu')
    # Split the indicator names into two lines
    ticklabels = [name.get_text().split(' ') for name in ax.get_xticklabels()]
    new_ticklabels = []
    for names in ticklabels:
        new_ticklabels.append('\n'.join(names))
    # Set the modified ticklabels on the x-axis
    ax.set_xticklabels(new_ticklabels)
    ax.set_yticklabels(new_ticklabels)
    plt.title("Heatmap of " + str(name), fontsize=25)
    plt.show()
    return


Excel_file = "API_19_DS2_en_excel_v2_4903056.xls"
Green_House_Gas_Emission, Green_House_Gas_Emission_T =\
    read_data(Excel_file, 'EN.ATM.GHGT.KT.CE', ['AUT', 'BEL', 'CHE', 'DEU',
                                                'DNK', 'FIN', 'ESP', 'FRA',
                                                'GBR', 'GRC'])
CO_Emission, CO_Emission_T =\
    read_data(Excel_file, 'EN.ATM.CO2E.KT', ['AUT', 'BEL', 'CHE', 'DEU', 'DNK',
                                             'FIN', 'ESP', 'FRA', 'GBR',
                                             'GRC'])
Methane_Emission, Methane_Emission_T =\
    read_data(Excel_file, 'EN.ATM.METH.KT.CE', ['AUT', 'BEL', 'CHE', 'DEU',
                                                'DNK', 'FIN', 'ESP', 'FRA',
                                                'GBR', 'GRC'])

plot(Green_House_Gas_Emission_T, "Green House Emission")
plot(CO_Emission_T, "Carbon Dioxide Emission")
plot(Methane_Emission_T, "Methane Emission")

GH_bar_plot =\
    Green_House_Gas_Emission_T.loc[['1990', '2000', '2005', '2010',
                                    '2015']].plot(kind='bar', figsize=(10, 6),
                                                  rot=45, fontsize=12)
GH_bar_plot.legend(loc='upper right', bbox_to_anchor=(1.23, 1.0))
plt.title("Total Green House Emission")
plt.xlabel("Years", fontsize=16)
plt.ylabel("kt of CO2 equivalent", fontsize=16)
plt.show()

stati1("Total Green House Gas Emission", Green_House_Gas_Emission_T)
stati1("Carbon Dioxide Emission", CO_Emission_T)
stati1("Methane_Emission", Methane_Emission)

stati2("Germany")
stati2("United Kingdom")
stati2("Switzerland")
stati2("France")
stati2("Spain")

Germany = country_data(Excel_file, 'DEU', ['EN.ATM.GHGT.KT.CE',
                                           'EN.ATM.CO2E.KT',
                                           'EN.ATM.NOXE.KT.CE',
                                           'EN.ATM.METH.KT.CE'])
United_Kingdom = country_data(Excel_file, 'GBR', ['EN.ATM.GHGT.KT.CE',
                                                  'EN.ATM.CO2E.KT',
                                                  'EN.ATM.GHGT.KT.CE',
                                                  'EN.ATM.NOXE.KT.CE',
                                                  'EN.ATM.METH.KT.CE'])


# Read data for all indicators
Green_House_Gas_Emission, Green_House_Gas_Emission_T =\
    read_data("API_19_DS2_en_excel_v2_4903056.xls", 'EN.ATM.GHGT.KT.CE',
              ['AUT', 'BEL', 'CHE', 'DEU', 'DNK', 'FIN', 'ESP', 'FRA', 'GBR',
               'GRC'])
CO_Emission, CO_Emission_T = read_data("API_19_DS2_en_excel_v2_4903056.xls",
                                       'EN.ATM.CO2E.KT', ['AUT', 'BEL', 'CHE',
                                                          'DEU', 'DNK', 'FIN',
                                                          'ESP', 'FRA', 'GBR',
                                                          'GRC'])
Methane_Emission, Methane_Emission_T =\
    read_data("API_19_DS2_en_excel_v2_4903056.xls", 'EN.ATM.METH.KT.CE',
              ['AUT', 'BEL', 'CHE', 'DEU', 'DNK', 'FIN', 'ESP', 'FRA', 'GBR',
               'GRC'])

heatmap(Germany, "Germany")
heatmap(United_Kingdom, "United_Kingdom")
