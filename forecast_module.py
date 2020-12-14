
def baseforecast(maxtemp,KW0): # This function provides point forecasts for the next half hour until the end of the day
    ### Required python packages, just to be on the safe side 
    import os
    import datetime
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    ### Set directory to where the input file is
    os.chdir("C:/users/farshid/dropbox/battery/Monash-Energy-Forecasting/forecast_module") #change as appropriate
    ### Read the required input (so far it extends to the end of May)
    base = pd.read_excel (r'baseincrement.xlsx') # add path as appropriate
    ### Sensitivity to temperature
    bmax = np.array([[-2.306761604,-1.374761527,-0.672261751,-1.48097675,-0.895940568,-0.195139906,-0.062872658,0.285373602,2.214936869,0.984886147,2.679605408,3.115119559,5.845095107,6.336457036,13.16961112,10.06314752,12.93186083,14.75910457,11.78445816,13.67081067,9.379492143,16.52503548,7.11185069,16.30142082,8.824028357,8.393475998,4.053528393,8.291998932,1.311856722,2.904582473,-6.283024952,-2.186548495,-17.57694212,-17.37936084,-34.59017071,-14.15890035,-12.02200115,-6.32463067,-8.824688588,-3.944377066,-6.529590857,-5.550819816,-5.445353838,-4.04840877,-5.141867405,-0.801163887,-7.945921886,-3.221260941
]])
    ### Standard error for each half hour
    sd = np.array([[89.19863192,83.39332942,76.29095765,70.53029189,67.47594017,67.49359863,70.54615454,75.42793596,81.99843743,89.34547547,99.54141365,114.6861736,139.4767923,165.5455594,180.0254723,176.5830019,170.125711,166.454469,166.7548504,167.4359554,165.1328036,162.4985756,161.4729681,163.0495334,169.5212158,179.812579,186.3140517,184.1931333,176.9920682,169.3560044,167.9109606,172.4342436,178.6990679,180.8221532,175.3855777,159.807734,143.3373476,130.305024,124.5470882,124.887941,123.3861496,114.449654,105.287709,98.94664762,95.35331341,93.76906487,93.15430638,89.4211945]])
    ### Determine day and time using system date. Assuming that this module is run after the latest half hour load is available
    x=datetime.datetime.now() 
    today = base.loc[(base["Year"]==x.year) & (base["Month"]==x.month) & (base["Day"]==x.day)] 
    today = np.asmatrix(today)
    h = x.hour*2+ (x.minute // 30)
    ### Determine the load increments for the rest of the day
    base_rest_of_day = today[0,(3+h):51]+maxtemp*bmax[0,h:48]
    ### Forecast load for the rest of the day
    load_rest_of_day = KW0 + np.cumsum(base_rest_of_day)
    #### The following three lines are for checking that the function is working OK. Comment out when done.
    rest_of_day = np.array([[period/2 for period in range(h+1,48+1)]])
    plt.plot(rest_of_day.T,load_rest_of_day.T)  
    plt.show()
    #### End of function check
    return load_rest_of_day





pointforecast = baseforecast(30,8500)





def one_possible_path(maxtemp,KW0): # This simulates a possible load path from the next half hour until the end of the day
    ### Required python packages, just to be on the safe side 
    import os
    import datetime
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    ### Set directory to where the input file is
    os.chdir("C:/users/farshid/dropbox/battery/Monash-Energy-Forecasting/forecast_module") #change as appropriate
    ### Read the required input (so far it extends to the end of May)
    base = pd.read_excel (r'baseincrement.xlsx') # add path as appropriate
    ### Sensitivity to temperature
    bmax = np.array([[-2.306761604,-1.374761527,-0.672261751,-1.48097675,-0.895940568,-0.195139906,-0.062872658,0.285373602,2.214936869,0.984886147,2.679605408,3.115119559,5.845095107,6.336457036,13.16961112,10.06314752,12.93186083,14.75910457,11.78445816,13.67081067,9.379492143,16.52503548,7.11185069,16.30142082,8.824028357,8.393475998,4.053528393,8.291998932,1.311856722,2.904582473,-6.283024952,-2.186548495,-17.57694212,-17.37936084,-34.59017071,-14.15890035,-12.02200115,-6.32463067,-8.824688588,-3.944377066,-6.529590857,-5.550819816,-5.445353838,-4.04840877,-5.141867405,-0.801163887,-7.945921886,-3.221260941
]])
    ### Standard error for each half hour
    sd = np.array([[89.19863192,83.39332942,76.29095765,70.53029189,67.47594017,67.49359863,70.54615454,75.42793596,81.99843743,89.34547547,99.54141365,114.6861736,139.4767923,165.5455594,180.0254723,176.5830019,170.125711,166.454469,166.7548504,167.4359554,165.1328036,162.4985756,161.4729681,163.0495334,169.5212158,179.812579,186.3140517,184.1931333,176.9920682,169.3560044,167.9109606,172.4342436,178.6990679,180.8221532,175.3855777,159.807734,143.3373476,130.305024,124.5470882,124.887941,123.3861496,114.449654,105.287709,98.94664762,95.35331341,93.76906487,93.15430638,89.4211945]])
    ### Determine day and time using system date. Assuming that this module is run after the latest half hour load is available
    x=datetime.datetime.now() 
    today = base.loc[(base["Year"]==x.year) & (base["Month"]==x.month) & (base["Day"]==x.day)] 
    today = np.asmatrix(today)
    h = x.hour*2+ (x.minute // 30)
    ### Determine the load increments for the rest of the day
    base_rest_of_day = today[0,(3+h):51]+maxtemp*bmax[0,h:48]+sd[0,h:48]*np.random.standard_normal(size=(1,48-h))
    ### Forecast load for the rest of the day
    path_rest_of_day = KW0 + np.cumsum(base_rest_of_day)
    #### The following three lines are for checking that the function is working OK. Comment out when done.
    rest_of_day = np.array([[period/2 for period in range(h+1,48+1)]])
    plt.plot(rest_of_day.T,path_rest_of_day.T)  
    plt.show()
    #### End of function check
    return path_rest_of_day





simulated = one_possible_path(30,8500)







