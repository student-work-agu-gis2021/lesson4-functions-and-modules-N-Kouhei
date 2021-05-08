def fahr_to_celsius(temp_fahrenheit):
  """Returns a value which converted from Fahrenheit to Celsius.
  -----Parameter-----
  temp_fahrenheit : int or float
    
  -----Return-----
  converted_temp : float  
  """
  converted_temp=(temp_fahrenheit-32)/1.8
  return converted_temp



def temp_classifier(temp_celsius):
  """
  Return values which grouped by Celsius value.
  -----Parameter-----
  temp_celsius : float
  -----Return-----
  0 : int
   when temp_celsius < -2
  1 : int
   when -2<= temp_celsius < 2
  2 : int
   when 2 <= temp_celsius < 15
  3 : int
  when 15 <= temp_celsius
  """
  if temp_celsius<-2:
    return 0
  elif -2<=temp_celsius<2:
    return 1
  elif 2<=temp_celsius<15:
    return 2
  else:
    return 3


"""
This file contains two functions, "fahr_to_celsius" and "temp_classifier".
"""