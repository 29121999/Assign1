import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def plot_pie_chart(labels, values):
    """
    Plots a pie chart of the top 10 medicines used in the UK.

    Parameters
    ----------
    labels : numpy.ndarray
        An array of strings representing the names of the medicines.
    values : numpy.ndarray
        An array of floats representing the usage values of the medicines.

    Returns
    -------
    None.

    """
    plt.figure()
    plt.pie(values, labels=labels, autopct='%1.2f')
    plt.title("Top 10 Medicines Used in the UK")
    plt.savefig("top_10_medicines.png")
    plt.show()

medicines_df = pd.read_excel("drugspie.xlsx", sheet_name="Data")
medicines_df = medicines_df[4:]
medicines_df.columns = ['Rank', 'Medicine', 'Usage Value']
medicine_names = np.array(medicines_df['Medicine'])
medicine_usage = np.array(medicines_df['Usage Value'])

plot_pie_chart(medicine_names[:10], medicine_usage[:10])
