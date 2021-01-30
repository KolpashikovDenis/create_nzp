import json
import requests
import configparser
import sys, os
import datetime as dt
from datetime import timedelta


if __name__ == "__main__":
    configfilename = os.path.abspath(os.path.dirname(sys.argv[0])) + '\properties.ini'
    config = configparser.ConfigParser()

    config.read(configfilename)
    hostname = config['DEFAULT']['hostname']
    login = config['DEFAULT']['login']
    password = config['DEFAULT']['password']
    is_user = bool(config['DEFAULT']['user'])

    auth_data = "{\"action\":\"login\",\"data\":{\"login\":\""+login+"\",\"password\":\""+password+"\"}}"
    req = requests.Session()
    responce = req.post(hostname + '/action/login', data=auth_data)
    c = req.cookies
    h = req.headers

    print(responce.content)
    print()

    if is_user:
        responce = req.get(hostname + '/rest/collection/user', cookies=c, headers=h)
        j = json.loads(responce.text)
        print (j)
        # if j['meta']['count'] != 0:
            # for item in j['user']:
            #     line = "%s;%s;%s;%s;%s;%s;%s" % (
            #     item['id'], item['disabled'], item['identity'], item['create_stamp'],
            #     item['patronymic_name'], item['last_name'], item['name'])
            #     print(line)
        responce = req.get(hostname + '/rest/collection/role', cookies=c, headers=h)
        j = json.loads(responce.text)
        print(j)

    print()

    responce = req.get(hostname + '/action/logout', cookies=c, headers=h)
    print(responce.content)