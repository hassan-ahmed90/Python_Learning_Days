
import time

y=input("DO you want to find time ")
hour=int(time.strftime("%H"))
if(17>=hour>=12):
  print('its',hour,"afternoon")
elif(0<hour<12):
  print('its',hour,"morning")
else:
  print('its',hour,"evening")
# morning=",good morning, sir"
# afternoon=",good after noon,sir"
# evening=",good evening, sir"
# x=input('enter your name sir : ')
# print('welcome,',x,'sir')
# print('do you wanna what time it is?')
# y=input('=')#only yes is acceptable
# print('its time for you to study')
# print('kidding,sir')
# hour=int(time.strftime("%H"))
# if(17>=hour>=12):
#   print('its',hour,afternoon)
# elif(0<hour<12):
#   print('its',hour,morning)
# else:
#   print('its',hour,evening)
