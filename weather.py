import numpy as np
import matplotlib.pyplot as plt

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
    
    # Initialization of the of the weather data array
    weather_thresh = np.zeros(len(weather_data))
    
    # Thresholding using numpy array methods and properties 
    weather_thresh[weather_data < threshold] = 1
    
    # Creation of the data string, casting to integer, conversion to list then 
    # join to string, split on "0", return list. 
    weather_thresh = ''.join([str(e) for e in weather_thresh.
                              astype(int).tolist()]).split("0")
    
    ### Creation of the windows array
    # Initialization of the array    
    serie = []
    
    # Iteration over the list of string to get length (number of ones)
    for s in weather_thresh:
        serie.append(len(s))
    
    # Addition of the zeros stripped in the splitting process 
    for i, s in enumerate(serie):
        if serie[i-1] and i:
            serie.insert(i, 0)
    
    ### Creation of the weather data array
    # Initialization of the array
    windows = []
    
    # Building of the array by iterating over the windows array:
    # if zero: add a zero
    # if > zero: add an array of len(element) and value = element.
    # ie: [0,2,0,3] gives [0,2,2,0,3,3,3]. 
    r = range
    
    for i, s in enumerate(serie):
        if not s:
            windows.append(0)
        else:
            for j in r(s):
                windows.append(s)
    
    return windows

if __name__ == "__main__":
    np.random.seed(1234)
    data = np.random.rand(21)
    print(data)
    v = make_windows_array(data, 0.5)
    plt.plot(data)
