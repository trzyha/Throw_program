#SIMULATION OF ROCK THROWING
from math import *
import os

g = 9.81
# rock_weight = input("set rock weight [kg]: ")




def throwing_range(tp, ta):
  result = round((tp**2*sin(2*sin(radians(ta))))/g,2)
  #return print ("Distance: " + str("%.2f" % result) + "[m]") #"%.2f" % for 2 dec after coma
  return result
  
def throwing_max_h(tp, ta):
  result = round((tp*sin(radians(ta)))**2/2*g,2)
  #return print ("Max. height: " + str("%.2f" % result) + "[m]") #"%.2f" % for 2 dec after coma
  return result
  
def flight_time(tp, ta):
  result = round((2*tp*sin(radians(ta)))/g,2)
  # return print ("Flight time [s]: " + str(round(result,2)) + "[s]") #round for 2 dec after coma
  return result
  
def clean():
  cls = lambda: print('\n'*100)
  cls()

no_count = 0  
again = "y"
#a2 = [["Distance [m]","Max. height [m]","Time of flight [s]"],[str(throwing_range (tp, ta)), str(throwing_max_h(tp, ta)),str(flight_time(tp, ta))]]
a2 = [["No.","Angle [deg]","Power [m/s]", "Distance [m]","Max. height [m]","Time of flight [s]"]]

while True:
  clean()
  if again == "y" or again =="": 
    no_count = no_count + 1
    ta = int(input("Set throwing angle [deg]: "))
    tp = int(input("Set throwing_power [m/s]: "))
    print ("Range: " + str(throwing_range(tp, ta)) + "[m]")
    print ("Max. height: " + str(throwing_max_h(tp, ta)) + "[m]")
    print ("Time of light: " + str(flight_time(tp, ta)) + "[s]")
    a2.extend([[no_count, ta, tp, str(throwing_range (tp, ta)), str(throwing_max_h(tp, ta)),str(flight_time(tp, ta))]])
    for row in a2:
      print ("{: <3} {: ^15} {: ^15} {: ^15} {: ^15} {: ^15}".format(*row))
  elif again == "l":
    for row in a2:
      print ("{: <3} {: ^15} {: ^15} {: ^15} {: ^15} {: ^15}".format(*row))
  elif again == "n":
    for row in a2:
      print ("{: <3} {: ^15} {: ^15} {: ^15} {: ^15} {: ^15}".format(*row))
    break
  else:
    print ("Choose again!")
  
  again = input("Again? [y/n and l for list] (default Enter = y): ").lower()
