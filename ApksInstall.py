# coding: utf-8

import time
import os
import subprocess 
import json


PLATFORM_TOOLS = "/Users/juniorportom/Library/Android/sdk/platform-tools/"
BASEDIR = "/Users/juniorportom/projects/uniandes/pruebas_automaticas/parcial2/Parcial2/"
APKDIR = "apk/parcial2/com.evancharlton.mileage-mutant"
APKNAME = "com.evancharlton.mileage_3110-aligned-debugSigned.apk"
PACKAGE = "com.evancharlton.mileage"
ACTIVITY = "it.feio.android.omninotes.MainActivity"
RAMDOM_EVENTS = 200
INITIAL = 1
FINAL = 4548



def log(fn, device):
    msg = device.shell('logcat -d')
    f_log = open(BASEDIR + fn, 'at')
    if msg is None:
        msg = 'None'
    f_log.write(msg.encode('utf-8'))
    f_log.close()
    device.shell('logcat -c')

def createJsonFile(id):
    rip_config = '{ "apkPath": "./apk/parcial2/com.evancharlton.mileage-mutant'+ str(id) + '/com.evancharlton.mileage_3110-aligned-debugSigned.apk",'
    rip_config = rip_config + '"outputFolder": "./output_mutante_' + str(id) + '/",'
    rip_config = rip_config + '''
    "isHybrid": false,
    "executionMode": "events",
    "scriptPath": "./output_base/result.json",
    "executionParams": {
        "events": 100,
        "time": 5
        }
    }'''

    f = open("rip_config.json", "w")
    f.write(rip_config)
    f.close()


def installApp():
    try:
        for i in range(INITIAL, FINAL + 1):
            createJsonFile(i)
            subprocess.call('cd ' + BASEDIR + ' && java -jar  RIPRR.jar rip_config.json >mutante' + str(i), shell=True)

    except Exception as e:
        print("type error: " + str(e))
        print(traceback.format_exc())

installApp()