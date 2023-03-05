import matplotlib.pyplot as plt
import pandas as pd
def create_barplot(data):
    """
    Parameters
    ----------
    data : pandas.DataFrame
        A DataFrame containing data to be plotted.

    Returns
    -------
    None.
    """
    plt.figure(figsize=(11,7))
    plt.bar(data["Country Name"], data["Australia"], label="Australia")
    plt.title("Market Cap of Australia (% of GDP)")
    plt.xlabel("Year")
    plt.ylabel("GDP %")
    plt.savefig("barplot.png")
    plt.show()
    
df = pd.read_excel('bar_plot.xls')
df = df.T
h = df.iloc[0].values.tolist()
df.columns = h
df = df[4:]
create_barplot(df)