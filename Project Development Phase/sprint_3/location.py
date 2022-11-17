import wiotp.sdk.device
import time
import random

myConfig = {
  "identity": {
    "orgId": "g20wc1",
    "typeId": "h2",
    "deviceId": "h2"
  },
  "auth": {
    "token": "12345678"
  }
}

def myCommandCallback(cmd):
  print("The Message received from IBM IoT Platform is : %s" % cmd.data['command'])
  m=cmd.data['command']

def pub(data):
  client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
  print("Data is published Successfully:%s",myData)

client = wiotp.sdk.device.DeviceClient(config=myConfig)
client.connect()

while True:
  myData={'name':'Train1','lat':10.184363,'lon': 77.922702}
  pub(myData)
  time.sleep(3)
  myData={'name':'Train1','lat':10.213225,'lon': 77.898765}
  pub(myData)
  time.sleep(3)
  myData={'name':'Train1','lat':10.285035,'lon': 77.921569}
  pub(myData)
  time.sleep(3)
  myData={'name':'Train1','lat':10.343369,'lon': 77.958056}
  pub(myData)
  time.sleep(3)
  myData={'name':'Train1','lat':10.356829,'lon': 77.980861}
  pub(myData)
  time.sleep(3)
  client.commandCallback = myCommandCallback
client.disconnect()
