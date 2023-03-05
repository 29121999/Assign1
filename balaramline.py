import matplotlib.pyplot as plt
import pandas as pd

def plot_tourism_data(data):
    """
    Plots a line chart of tourism data for different countries.

    Parameters
    ----------
    data : pandas.DataFrame
        A DataFrame containing the tourism data.

    Returns
    -------
    None.

    """
    plt.figure()
    plt.plot(data["Country Name"], data["China"], label="China")
    plt.plot(data["Country Name"], data["France"], label="France")
    plt.plot(data["Country Name"], data["United Kingdom"], label="United Kingdom")
    plt.plot(data["Country Name"], data["United States"], label="United States")
    plt.title('Tourism Data for Different Countries')
    plt.xlabel('Years')
    plt.ylabel('Number of people Visited ')
    plt.legend()
    plt.savefig("tourism_data.png")
    plt.show()


tourism_data_df = pd.read_excel("tourism.xls", sheet_name="Data")
tourism_data_df = pd.DataFrame.transpose(tourism_data_df)
header = tourism_data_df.iloc[0].values.tolist()
tourism_data_df.columns = header
tourism_data_df = tourism_data_df[4:]

plot_tourism_data(tourism_data_df)
