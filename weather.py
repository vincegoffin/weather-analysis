## TODO: add proper doc
## TODO: add proper comments
## TODO: add proper tests
## TODO: add preprocessing routines (thresholds, pandas...)
## TODO: add post processing routines (percentiles, months...)
## TODO: add regex spliting instead of buggy split and adding zeros

import numpy as np
import matplotlib.pyplot as plt

def get_threshold_data(weather_data, threshold):
    weather_data[weather_data < threshold] = 0
    weather_data[weather_data > threshold] = 1
    return weather_data


def process_threshold(weather_threshold):
    weather_threshold = weather_threshold.astype(int).tolist()
    weather_threshold = [str(e) for e in weather_threshold]
    weather_threshold = ''.join(weather_threshold).split("0")
    return weather_threshold


def get_window_from_threshold(weather_threshold):
    serie = []
    for s in weather_threshold:
        serie.append(len(s))
    for i, s in enumerate(serie):
        if serie[i-1] != 0 and i != 0:
            serie.insert(i, 0)
    return serie


def windowize(weather_data):
    serie = []
    for i, s in enumerate(weather_data):
        if s == 0:
            serie.append(0)
        else:
            for j in range(s):
                serie.append(s)
    return serie

if __name__ == "__main__":
    np.random.seed(1234)
    v = np.random.rand(20)
    v = get_threshold_data(v, 0.5)
    r = process_threshold(v)
    serie = get_window_from_threshold(r)
    serie = windowize(serie)
    plt.plot(serie)
