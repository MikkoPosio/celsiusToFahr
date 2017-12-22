# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 15:42:12 2017

@author: mikkopos
"""
""" this function change temperature from celsius to Fahrenhait
    Parameters
    ----------
    tempCelsius: <numerical>
        Temperature in Celsius
        
    Returns
    --------
    <float>
        Converted temperature
            """

def celsiusToFahrenhait(tempcelsius):
    ''' this function change temperature from celsius to Fahrenhait
    Parameters
    ----------
    tempCelsius: <numerical>
        Temperature in Celsius
        
    Returns
    --------
    <float>
        Converted temperature
        '''
    return 9/5 * tempcelsius + 32

freezingpoint = celsiusToFahrenhait(0.0)
print ("ulkona on", celsiusToFahrenhait (2))

 