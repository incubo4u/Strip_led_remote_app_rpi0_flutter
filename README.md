# Strip_led_remote_app_rpi0_flutter
this is very simple Flutter app&amp; Python3 script to control led strip using Raspberry pi and ios or andoid or web

###### Requirements:

- Raspberry Pi 
- WS2812 RGB LED Strip
- Andorid or Ios device

###### Leds to Raspberry pi connection tutorial:
https://tutorials-raspberrypi.com/connect-control-raspberry-pi-ws2812-rgb-led-strips/

###### Set up 
1)  the application has to be built and installed on the device using for example e.g. Android studio with Flutter installed.
- Flutter installation tutorial: https://flutter.dev/docs/get-started/install
- Flutter application release: https://flutter.dev/docs/deployment/android 

2)  the next step is to create the request_handler, led_off and led_on Python script for Raspberry pi
- **IMPORTANT**: use 'chmod +x request_handler' that will make the script executable

3)  we'll use crontab to make sure the script is executed  24/7.
to do this we will use the command 'crontab -e' then select the editor for example nano to create a new crontab task by typing 
'* * * * * sudo python3 /full/path/to/request_handler.py &' then press control x to save

###### IMPORTANT ADDITIONAL INFORMATION: 
- led_off and led_on files exist only because I have connected led directly to Raspberry, so the easiest way to turn them off is to set the brightness to 0 (it's not a good solution but it works 😆).
- **you shouldn't connect the leds to Raspberry pi in this way because it's possible to destroy the device in case of a short circuit (please be careful if you do that).** 
- change the IP address in the files to Raspberry pi  IP (use the command 'ifconfig' to know the device IP)
- both devices must operate on the same wifi network for the application to work
- if too many leads are connected to the Raspberry pi the power supply may not be able to start them all, in this case i recommend using an external power source (more information here: https://tutorials-raspberrypi.com/connect-control-raspberry-pi-ws2812-rgb-led-strips/).
