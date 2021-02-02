import json
import requests
import configparser
import sys, os
import datetime as dt
from datetime import timedelta

configfilename = os.path.abspath(os.path.dirname(sys.argv[0])) + '\\actualize_prod_state.ini'
config = configparser.ConfigParser()

config.read(configfilename)
hostname_auth = config['DEFAULT']['hostname_auth']
hostname = config['DEFAULT']['hostname']
login = config['DEFAULT']['login']
password = config['DEFAULT']['password']
# str_date = config['DEFAULT']['date']
# input_file = config['DEFAULT']['inputfile']
# is_entity = bool(config['DEFAULT']['entity'])
# is_entity_route_sheet_transaction = bool(config['DEFAULT']['entity_route_sheet_transaction'])
# is_entity_route_sheet = bool(config['DEFAULT']['entity_route_sheet'])
# is_entity_route_sheet_operation = bool(config['DEFAULT']['entity_route_sheet_operation'])
# is_operation = bool(config['DEFAULT']['operation'])
# is_department = bool(config['DEFAULT']['department'])
# is_equipment_class = bool(config['DEFAULT']['equipment_class'])
# is_entity_batch = bool(config['DEFAULT']['entity_batch'])
# is_user = bool(config['DEFAULT']['user'])

auth_data = "{\"action\":\"login\",\"data\":{\"login\":\""+login+"\",\"password\":\""+password+"\"}}"
# template_body = "{\"data\":{\"identity\":\"%s\",\"name\":\"%s\",\"equipment_class_id\":%s,\"department_id\":%s}}"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    req = requests.Session()
    responce = req.post(hostname_auth + '/action/login', data=auth_data)
    print(responce.content)
    c = req.cookies
    h = req.headers

    responce = req.post(hostname + '/action/actualize_production_state', data='', cookies = c, headers=h)
    print(responce)
    print(responce.content)

    responce = req.get(hostname_auth+'/action/logout', cookies=c, headers=h)
    print(responce.content)