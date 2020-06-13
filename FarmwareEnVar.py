from farmware_tools import device
from farmware_tools import get_config_value
import json
import os

evName = get_config_value(farmware_name='FarmwareEnVar', config_name='evName', value_type=str)
evValue = get_config_value(farmware_name='FarmwareEnVar', config_name='evValue', value_type=str)

device.log(message="Recieved environment variable name: " + str(evName) + " environment variable value: " + str(evValue), message_type="success")

config = {evName: evValue}   
configFileName = '/tmp/farmware/config.json'

# If the file exists delete it
if os.path.isfile(configFileName) :
    os.remove(configFileName)
    device.log(message="Config file: " + str(configFileName) + " existed so deleteing it", message_type="success")

# Create a new file and load the config
with open(configFileName, 'w') as f:
    json.dump(config, f)
    filepath = os.path.abspath(f.name)
    f.close()
device.log(message="Created new config file: " + str(configFileName) + " path: " + str(filepath) + " and wrote environment variables to it", message_type="success")