import netifaces as ni
import urllib.request
import os
import mysql.connector

# this is for flat configaration .when there is flat configaration table found in Rpi then using vpn file name(in vpn filename it contain the flat details)
        # example Cent_C_5_501.conf removing the .conf form file take flat name and sending flat name to configer after api request all switch board config is loaded
        # to Rpi directly then raspbery pi knows how many switch board  which switch board on what location every thing
class Flatconfigaration():
    
    def __init__(self):
        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="icity_admin",
                database="datbase"
            )
            
        except:
            self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="icity_admin"
            )

            mycursor = self.mydb.cursor()
            mycursor.execute("CREATE DATABASE IF NOT EXISTS datbase")
            print("data base created")
        self.my = self.mydb.cursor()
        sql_flat_config = "SELECT * FROM  information_schema.tables WHERE table_name = 'flat_configuration'"
        self.my.execute(sql_flat_config)  # exceuting query to sql
        db_get_sql_flat_config = self.my.fetchall()
        if db_get_sql_flat_config == []:
            host = ni.ifaddresses('tun0')[ni.AF_INET][0]['addr']
            # host='127.0.0.1'
            file_in_folder = os.listdir('/etc/openvpn/')
            for i in file_in_folder:
                if i[-5:] == '.conf':
                    file_name = i[:-5]
                    print("file name",file_name)
            url = "http://3.128.231.248/i-switch/automation/get_rpi.php?rpi_ip=" + \
                host+"&flat_unique_id="+file_name
            print(url)
            ser_rsp = urllib.request.urlopen(url, timeout=6)
            ser_data = ser_rsp.read().decode("utf-8")
            print('flat registartion responce ',ser_data)
            if ser_data == '1':
                print("configaration file loaded succesfully")
            else:
                print("configaration fails")

FlatObj=Flatconfigaration()