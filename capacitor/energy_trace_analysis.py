import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




def FR5994_8MHz():
    ADCon_current = pd.read_csv("./FR5994_8MHz_ADCon.csv").tail(5000).loc[ : ,"Current:uinteger"].to_numpy()
    ADCoff_current = pd.read_csv("./FR5994_8MHz_ADCoff.csv").tail(5000).loc[ : ,"Current:uinteger"].to_numpy()

    ADCon_current_static = pd.read_csv("./FR5994_8MHz_Static_ADCon.csv").tail(5000).loc[ : ,"Current:uinteger"].to_numpy()
    ADCoff_current_static = pd.read_csv("./FR5994_8MHz_Static_ADCoff.csv").tail(5000).loc[ : ,"Current:uinteger"].to_numpy()

    ADCon_begin = 130
    ADCoff_begin = 80
    item_number = 500
    
    ADCon_current = ADCon_current[ADCon_begin: ADCon_begin+item_number] / 1e6
    ADCoff_current = ADCoff_current[ADCoff_begin: ADCoff_begin+item_number] / 1e6
    ADCon_current_static = ADCon_current_static[: item_number] / 1e6
    ADCoff_current_static = ADCoff_current_static[: item_number] / 1e6

    plt.plot(ADCon_current, ls='-', lw=2, label="ADC_on")
    plt.plot(ADCoff_current, ls='-', lw=2, label="ADC_off")

    plt.plot(ADCon_current_static, ls='-', lw=2, label="Static ADC_on")
    plt.plot(ADCoff_current_static, ls='-', lw=2, label="Static ADC_off")

    plt.ylabel("Current (mA)")
    plt.legend()
    plt.show()


FR5994_8MHz()