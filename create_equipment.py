import json
import requests
import configparser
import sys, os
import datetime as dt
from datetime import timedelta

configfilename = os.path.abspath(os.path.dirname(sys.argv[0])) + '\properties.ini'
config = configparser.ConfigParser()

config.read(configfilename)
hostname = config['DEFAULT']['hostname']
login = config['DEFAULT']['login']
password = config['DEFAULT']['password']
input_file = config['DEFAULT']['inputfile']
# str_date = config['DEFAULT']['date']
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
template_body = "{\"data\":{\"identity\":\"%s\",\"name\":\"%s\",\"equipment_class_id\":%s,\"department_id\":%s}}"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    req = requests.Session()
    responce = req.post(hostname + '/action/login', data=auth_data)
    c = req.cookies
    h = req.headers

    fout = open(input_file, 'r')
    st_list = fout.readlines()
    fout.close()
    st_list = st_list[1:]
    for line in st_list:
        items = line.strip().split(';')
        body = template_body % (items[0], items[1], items[2],items[3])
        print(body)
        body = body.encode('UTF-8')
        response = req.post(hostname + '/action/equipment/create', data = body, cookies = c, headers = h)
        print(response.content)

responce = req.get(hostname+'/action/logout', cookies=c, headers=h)
print('Done.')