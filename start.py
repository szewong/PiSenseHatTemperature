import os
import time
import datetime
import json
import requests
import icons
from sense_hat import SenseHat


webhook_url='https://qa-dataflownode.zerionsoftware.com/domain/zerionint/services/webhooks/2f8dc4cd1dca6e7fa75e49271e0562af15481153-5b85c24a0ee8b07f247cd0c3a740bf16b7583510'

g = (0,255,0)
r = (255,0,0)
b = (0,0,255)

sense = SenseHat()

def sendToZerion(data):
    try:
      response = requests.post(webhook_url, data, headers={'Content-Type':'application/json'})
      print(response.text)
      return True
      # sense.set_pixel(0,0,(0,255,0))
      # sense.show_letter("O",(0,255,0))
    except requests.exceptions.RequestException as e:
      print(e)
      return False
      # sense.set_pixel(0,0,(255,0,0))
      # sense.show_letter("O",(255,0,0))



# get CPU temperature
def get_cpu_temp():
  res = os.popen("vcgencmd measure_temp").readline()
  t = float(res.replace("temp=","").replace("'C\n",""))
  return(t)

# use moving average to smooth readings
def get_smooth(x):
  if not hasattr(get_smooth, "t"):
    get_smooth.t = [x,x,x]
  get_smooth.t[2] = get_smooth.t[1]
  get_smooth.t[1] = get_smooth.t[0]
  get_smooth.t[0] = x
  xs = (get_smooth.t[0]+get_smooth.t[1]+get_smooth.t[2])/3
  return(xs)


filename = "/home/pi/data/data_%s.js" % datetime.datetime.now()

# Sleep for 20 seconds, wait for network to start
#for x in range (0,8):
#  sense.set_pixel(x,0,(255,0,0))
#  time.sleep(2)



while True:
  f = open (filename, "a+")
  t1 = sense.get_temperature_from_humidity()
  t2 = sense.get_temperature_from_pressure()
  t_cpu = get_cpu_temp()
  h = sense.get_humidity()
  p = sense.get_pressure()

  # calculates the real temperature compesating CPU heating
  t = (t1+t2)/2
  t_corr = t - ((t_cpu-t)/1.5)
  t_corr = get_smooth(t_corr)
  t_corr_f = t_corr * 9 / 5 + 32

  nowt = datetime.datetime.now()
  data = '{"time":"%s", "temperature":%.2f, "temperature_corrected":%.2f,  "humidity":%.2f,  "pressure":%.2f}' % (nowt, t, t_corr_f, h, p)

  sendOK = sendToZerion(data)
  f.write("%s,\n" % data)
  f.close()
  sense.show_message("%.1f" % (t_corr_f))
  if sendOK:
    sense.set_pixels(icons.wifi)
  else:
    sense.set_pixels(icons.no_wifi)

  time.sleep(5)

    

