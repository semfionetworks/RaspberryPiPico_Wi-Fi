from machine import Pin, SoftI2C
from time import sleep
from bme680 import *

i2c = SoftI2C(scl=Pin(4), sda=Pin(3))
bme = BME680_I2C(i2c=i2c)

while True:
  try:
    temperature = str(round(bme.temperature, 2)) + ' C'
    #temp = (bme.temperature) * (9/5) + 32
    #temp = str(round(temp, 2)) + 'F'
    
    humidity = str(round(bme.humidity, 2)) + ' %'
    
    pressure = str(round(bme.pressure, 2)) + ' hPa'
    
    gas = str(round(bme.gas/1000, 2)) + ' KOhms'

    print('Temperature:', temperature)
    print('Humidity:', humidity)
    print('Pressure:', pressure)
    print('Gas:', gas)
    print('-------')
  except OSError as e:
    print('Failed to read bme680 sensor.')
 
  sleep(5)
