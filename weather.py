# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import itertools
import pandas as pd
import time

def make_windows_array(weather_data, threshold):
    '''
    Function to compute the time windows datafile from the weahter time series.
    The time series is an array like [1.34, 1.45, 1.44] with associated time 
    stamps and return an array like [1, 0, 1] where the numbers are the number 
    of time intervals in the window.

    The algorithm works in steps:
	    1) Thresholding to one and zeros (ones are below threshold)
	    2) Transformation of the array into a string to split it on zeros
	    3) Computation of the windows using len(str)
	    4) Construction of the windows array from the lengths array

    Inputs: 
	    weather_data = array with the weather data (numpy array)
	
	    threshold = the threshold related to the nautical spread (float)
    '''
    ### Thresholding

    thresholded = (int(val < threshold) for val in weather_data)

    r = []

    # itertools.groupby:
    # k = the value being repeated
    # g = said sequence
    # eg: itertools.groupby(0001100) returns [(0, [0,0,0]), (1, [1,1]), (0, [0,0])]
    for k , g in itertools.groupby(thresholded):
        if k:
            #
            # Under the threshold: Change [1,...,1] (n times) to [n,...,n] (n times)
            #

            # Extracting the number of consecutive valid hours (under the threshold)
            n = len(list(g))  # CAUTION: g gets "exhausted" and can't be reused!!

            r.extend([n]*n)  # eg: [3]*3 = [3,3,3]
        else:
            #
            # Above the threshold: Leave it as is.
            #
            r.extend(list(g))

    return r

    ###
    ### ONE-LINE VERSION UNDER
    ###

    # Imbricated generator because len(list(g)) needs to be used twice,
    # but its first evaluation "exhausts" it (because g is a generator).
    # return list(itertools.chain(*(  # itertools.chain = multiple list.extend, all in one.
        # [g*k]*g either returns [0,0,0] or [4,4,4,4]
    #     [g*k]*g for k, g in ((k, len(list(g))) for k,g in (itertools.groupby(val < threshold for val in weather_data)))
    # )))

if __name__ == "__main__":
	#np.random.seed(1234)
	#data = np.random.rand(21)
    # Example on actual data:
    # TODO: add datafile
    meteo = pd.read_csv('/home/vincent/git/weather-analysis/meteo.tsv', sep='\t', decimal=',')
    data = list(meteo['Hsig'])
    
    meteo['year']= (time.strptime(meteo['time'][1],"%d/%m/%Y %H:%M")[0])
    meteo['month']= (time.strptime(meteo['time'][1],"%d/%m/%Y %H:%M")[1])
    
    for thresholds in np.arange(0,3.25,0.25):
        v = make_windows_array(data, thresholds)
        meteo['Hsig{thresh}'.format(thresh = int(thresholds * 100))] = v
    
    print(meteo.head())
    # plt.plot(serie)
    plt.plot(data)
