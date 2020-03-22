#!/usr/bin/env python

'''FarmwareEnVar
Farmware that creates a new or updates an existing enviroment variable on the Raspberry Pi.
'''
import os
from farmware_tools import app
from farmware_tools import device
from farmware_tools import env
from farmware_tools import get_config_value

# Load the arguements
evName = get_config_value(farmware_name='FarmwareEnVar', config_name='name', value_type=str)
evValue = get_config_value(farmware_name='FarmwareEnVar', config_name='value', value_type=str)

#
if evName != "":
    # Check if the environment variable already exists and if so set the value
    currentValue = os.environ.get(evName,"")
    if currentValue != "" :
        device.log(message="Environment variable exists for name: " + str(evName) + " current value is: " + str(currentValue) + " setting value to: " + str(evValue), message_type="success")
        os.environ['evName'] = evValue
    # Otherwise create a new environment variable and set the value
    else :
        device.log(message="Creating environment variable: " + str(evName) + " value is: " + str(evValue), message_type="success")
        os.environ['evName'] = evValue