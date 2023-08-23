import os
import mysql.connector


def CreateWifiConfig(SSID, password, priority):
    os.system('sudo chmod 777 /etc/wpa_supplicant/wpa_supplicant.conf')

    config_lines = [
        '\n',
        'network={',
        '\tssid="{}"'.format(SSID),
        '\tpsk="{}"'.format(password),
        '\tpriority={}'.format(priority),
        '}'
    ]

    config = '\n'.join(config_lines)
    print(config)

    with open("/etc/wpa_supplicant/wpa_supplicant.conf", "a+") as wifi:
        wifi.write(config)

    print("Wifi config added")


def db():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="icity_admin",
            database="datbase"
        )

    except:
        print("data_base error")
        print('commin self')

    my = mydb.cursor()
    sql_get_table_name = "SELECT  wifi_name,password,priority FROM  system_infomation  ORDER BY created_at   DESC LIMIT 1"
    my.execute(sql_get_table_name)  # exceuting query to sql
    db_get_table_name = my.fetchall()
    print(db_get_table_name[0][0], db_get_table_name[0]
          [1], db_get_table_name[0][2])
    CreateWifiConfig(
        db_get_table_name[0][0], db_get_table_name[0][1], db_get_table_name[0][2])

    os.system('sudo chmod 644 /etc/wpa_supplicant/wpa_supplicant.conf')


db()
