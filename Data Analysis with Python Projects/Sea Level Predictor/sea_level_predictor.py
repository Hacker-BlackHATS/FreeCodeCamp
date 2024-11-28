import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(16, 9))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    # Slope 1
    x = np.arange(1880, 2080, 20)
    slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    y = slope * x + intercept

    plt.plot(x, y, color='red', label=f'Line: y = {slope}*x + {intercept}')

    # Create second line of best fit
    # Slope 2
    x = np.arange(2000, 2080, 20)
    slope, intercept, r_value, p_value, std_err = linregress(df.loc[df["Year"] >= 2000]["Year"], df.loc[df["Year"] >= 2000]["CSIRO Adjusted Sea Level"])
    y = slope * x + intercept

    plt.plot(x, y, color='green', label=f'Line: y = {slope}*x + {intercept}')


    # Add labels and title
    plt.title("Rise in Sea Level")
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")


    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()