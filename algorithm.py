import subprocess
import os
import schedule
# from swp_v2 import iswitch


class iswitchFeature():

    def __init__(self):
        pass

    def VpnNotWorking(self):
        y = subprocess.run(["tail", "/var/log/daemon.log"],
                           stdout=subprocess.PIPE)
        y = y.stdout.decode('utf-8')
        # y = y.decode('utf-8')
        # z = y.split('/n')

        Vpn_error_list = ['TLS Error: TLS key negotiation failed to occur within 60 seconds (check your network connectivity)',
                          'TLS Error: TLS handshake failed', 'UDP link local: (not bound)', 'SIGUSR1[soft,tls-error] received, process restarting']
        count = 0
        for error in Vpn_error_list:
            if error in y:
                count += 1

        if count > 2:
            # disable = subprocess.run(
            #     ['sudo', 'systemctl', 'disable', ' openvpn'], stdout=subprocess.PIPE)
            # disable = disable.stdout.decode('utf-8')
            # print(disable)
            # enable = subprocess.run(
            #     ['sudo', 'systemctl', 'enable', ' openvpn'], stdout=subprocess.PIPE)
            # enable = enable.stdout.decode('utf-8')
            # print(enable)
            # os.system("sudo systemctl disable openvpn")
            # os.system("sudo systemctl enable openvpn")
            # print("vpn issue. system is restarting ")
            # os.system("sudo reboot")
            os.system("sudo service openvpn restart")
            print("vpn restarted")

    # def schedule_switches(self, id, from_time, to_time):
    #     # print(id, from_time, to_time)

    #     on_time = str(from_time)
    #     off_time = str(to_time)
    #     on_time = on_time[:-3]
    #     off_time = off_time[:-3]
    #     if on_time[1] == ':':
    #         on_time = '0'+on_time
    #     if off_time[1] == ':':
    #         off_time = '0'+off_time

    #     print(on_time, off_time)
    #     schedule.every().day.at(on_time).do(self.PostData, id, '1')
    #     schedule.every().day.at(off_time).do(self.PostData, id, '0')


fetobj = iswitchFeature()
