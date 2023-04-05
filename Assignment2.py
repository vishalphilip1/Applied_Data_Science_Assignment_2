"""
Created on Thu Mar 30 20:39:36 2023.

@author: Vishal Philip
Following script reads data from the Excel file to create
visualizations and statistics for greenhouse gas emissions,
carbon dioxide emissions, methane emissions for various countries over time.
It  plots lineplot, barplot and heatmap. For heatmap additional indicator
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
    indicator_code (str): indicator code to select rows
    country_codes (list): list of country codes to select rows

    Returns:
    tuple: two data frames, one in original format and one transposed
    """

    # read excel file
    df = pd.read_excel(filename, skiprows=3)
    # select rows based on indicator code country values
    df1 = df.loc[(df['Indicator Code'] == indicator_code) &
                 (df['Country Code'].isin(country_codes))]
    # drop columns with all missing values
    df1.dropna(how='all', axis=1, inplace=True)
    # set country name as index
    df1.set_index('Country Name', inplace=True)
    # Remove unnecessary columns and transpose
    df1 = df1.drop(columns=['Country Code', 'Indicator Code',
                            'Indicator Name'])
    df1_transposed = df1.T
    return df1, df1_transposed


def plot(df, name):
    """Created function to plot lineplot with suitable title and labels

    Args:
    df : name of the dataframe
    name : title name
    """

    # plot the data
    df.plot()
    # add title and labels
    plt.title(name, fontsize=16)
    plt.xlabel("Years", fontsize=16)
    plt.ylabel("kiloton", fontsize=16)
    # add legend to the plot
    plt.legend(loc='upper right', bbox_to_anchor=(1.37, 1.0))
    plt.show()
    return


def bar_plot(df):
    """Create a bar plot showing the total green house
    emission for certain years.

    Args:
    df (DataFrame): The data frame containing the emissions data.
    """
    # Plotting bar plot for specific years
    df = df.loc[['1990', '2000', '2005', '2010',
                '2015']].plot(kind='bar', figsize=(10, 6),
                              rot=45, fontsize=12)
    df.legend(loc='upper right', bbox_to_anchor=(1.23, 1.0))
    plt.title("Total Green House Emission")
    plt.xlabel("Years", fontsize=16)
    plt.ylabel("kt of CO2 equivalent", fontsize=16)
    plt.show()
    return()


def stati1(name, df):
    """ Created function to use statistics tools for different indicators

    Args:
    name : name of the indicator
    df : name of the database
    """
    print(name + "\n", df.describe())
    # Printing minimum values
    print(name + " Minimum values \n", df.describe().loc["min"])
    # Print maximum values
    print(name + " Maximum values \n", df.describe().loc["max"])
    return


def stati2(country_name):
    """ Created function to use statitics tools for different countires

    Args:
    country_name : Name of the countries
    """
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
    """Creates a heatmap to show correlations"""
    # compute orrelation matrix
    correlation = country_name.corr()
    # create new plot with custom size
    fig, ax = plt.subplots(figsize=(12, 10))
    # plot heatmap with the correlation values
    sns.heatmap(correlation, cmap='YlGnBu')
    # Split the indicator names into two lines
    ticklabels = [name.get_text().split(' ') for name in ax.get_xticklabels()]
    new_ticklabels = []
    for names in ticklabels:
        new_ticklabels.append('\n'.join(names))
    # Set the modified ticklabels on the x-axis
    ax.set_xticklabels(new_ticklabels)
    ax.set_yticklabels(new_ticklabels)
    # set the plot title
    plt.title("Heatmap of " + str(name), fontsize=25)
    plt.show()
    return


# reading excel file
Excel_file = "API_19_DS2_en_excel_v2_4903056.xls"
# calling the function read_data
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
# calling the function plot
plot(Green_House_Gas_Emission_T, "Green House Emission")
plot(CO_Emission_T, "Carbon Dioxide Emission")
plot(Methane_Emission_T, "Methane Emission")

# calling the function bar_plot
bar_plot(Green_House_Gas_Emission_T)

# calling the function stati1
stati1("Total Green House Gas Emission", Green_House_Gas_Emission_T)
stati1("Carbon Dioxide Emission", CO_Emission_T)
stati1("Methane_Emission", Methane_Emission)

# calling the function stati2
stati2("Germany")
stati2("United Kingdom")
stati2("Switzerland")
stati2("France")
stati2("Spain")

# calling the functions country_data
Germany = country_data(Excel_file, 'DEU', ['EN.ATM.GHGT.KT.CE',
                                           'EN.ATM.CO2E.KT',
                                           'EN.ATM.NOXE.KT.CE',
                                           'EN.ATM.METH.KT.CE'])
United_Kingdom = country_data(Excel_file, 'GBR', ['EN.ATM.GHGT.KT.CE',
                                                  'EN.ATM.CO2E.KT',
                                                  'EN.ATM.GHGT.KT.CE',
                                                  'EN.ATM.NOXE.KT.CE',
                                                  'EN.ATM.METH.KT.CE'])

# calling the function heatmap
heatmap(Germany, "Germany")
heatmap(United_Kingdom, "United_Kingdom")
