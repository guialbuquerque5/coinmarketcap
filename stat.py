import csv
directory_data = 'data'

def plot():
    import matplotlib.pyplot as plt
    plt.plot([1,2,3,4])
    plt.ylabel('some numbers')
    plt.show()

def get_data(data_name):
    reader = csv.reader(open(data_name), delimiter= ',', quotechar='"')
    for row in reader:
        print(row)

def plot_1():
    import plotly.plotly as py
    import plotly.graph_objs as go

    # Create random data with numpy
    import numpy as np

    N = 500
    random_x = np.linspace(0, 1, N)
    random_y = np.random.randn(N)

    # Create a trace
    trace = go.Scatter(
        x = random_x,
        y = random_y
    )

    data = [trace]

    py.iplot(data, filename='basic-line')

get_data(directory_data + '/' +'bitcoin.csv')
plot_1()
