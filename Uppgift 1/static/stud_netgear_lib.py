# -*- coding: utf-8 -*-
""" A Python class/program that can query and setup certain Netgear routers"""
#
# https://github.com/roblandry/pynetgear_enhanced
# pip3 install pynetgear_enhanced
#
# Since we are mocking (fakeing) the pynetgear_enhanced lib we don not need
# and should NOT install anything for this examination program to work!
#

import datetime
from collections import namedtuple

# example usage fakeing/simulating some of the the pynetgear_enhanced library functions
Device = namedtuple(
    "Device", ["name", "ip", "mac", "type", "signal", "link_rate",
               "allow_or_block", "device_type", "device_model",
               "ssid", "conn_ap_mac"])

class NetgearEnhanced():
    """Represents a session to a Netgear Router."""

    """Class that simulate some library functions"""
    def __init__(self, password=None, host=None, user=None, port=None,  # noqa
                 ssl=False, url=None, force_login_v2=False):

        # default login
        if not user:
            user = 'admin'
        if not password:
            password = 'password'

        self.username = user
        self.password = password
        self.ssl = ssl

    def get_info(self):
        """Get the router information"""
        return {'ModelName': 'R7800', 'Description': 'Netgear Smart Wizard 3.0, specification 1.6 version', 'SerialNumber': '4H615C5B0ABCD', 'Firmwareversion': 'V1.0.2.82SF', 'SmartAgentversion': '3.0', 'FirewallVersion': 'net-wall 2.0', 'VPNVersion': None, 'OthersoftwareVersion': 'N/A', 'Hardwareversion': 'R7800', 'Otherhardwareversion': 'N/A', 'FirstUseDate': 'Sunday, 30 Sep 2007 01:10:03', 'DeviceName': 'R7800', 'FirmwareDLmethod': 'MANUAL', 'FirmwareLastUpdate': '2019_10.29_22:55:4', 'FirmwareLastChecked': '2021_1.19_22:30:5', 'DeviceMode': '0'}

    def get_traffic_meter_statistics(self):
        """Get the router traffic meter statistics"""
        return {'NewTodayConnectionTime': datetime.timedelta(days=1, seconds=600), 'NewTodayUpload': 1117.0, 'NewTodayDownload': 26669.0, 'NewYesterdayConnectionTime': datetime.timedelta(days=1), 'NewYesterdayUpload': 2106.0, 'NewYesterdayDownload': 30506.0, 'NewWeekConnectionTime': datetime.timedelta(days=3, seconds=600), 'NewWeekUpload': (5693.0, 1897.0), 'NewWeekDownload': (101578.0, 33859.0), 'NewMonthConnectionTime': datetime.timedelta(days=19, seconds=540), 'NewMonthUpload': (54070.0, 2845.0), 'NewMonthDownload': (507380.0, 26704.0), 'NewLastMonthConnectionTime': datetime.timedelta(days=30, seconds=86340), 'NewLastMonthUpload': (181028.0, 5839.0), 'NewLastMonthDownload': (1012012.0, 32645.0)}
        # Example and description of returned result
        # 'NewTodayConnectionTime':'23:19'
        # 'NewTodayUpload':'1088.0'
        # 'NewTodayDownload':'26564.0'
        # 'NewYesterdayConnectionTime':'24:0'
        # 'NewYesterdayUpload':'2106.0'
        # 'NewYesterdayDownload':'30506.0'
        # 'NewWeekConnectionTime':'71:19'
        # 'NewWeekUpload':'5663.0/1887.0'           # Upload/Avg
        # 'NewWeekDownload':'101473.0/33824.0'      # Download/Avg
        # 'NewMonthConnectionTime':'455:18'
        # 'NewMonthUpload':'54040.0/2844.0'         # Upload/Avg
        # 'NewMonthDownload':'507275.0/26698.0'     # Download/Avg
        # 'NewLastMonthConnectionTime':'743:59'
        # 'NewLastMonthUpload':'181028.0/5839.0'    # Upload/Avg
        # 'NewLastMonthDownload':'1012012.0/32645.0'# Download/Avg

    def get_attached_devices(self):
        """Get the routers attached devices"""
        return [Device(name='ESP_8C258D', ip='192.168.2.106', mac='D8:F1:5B:8C:25:8D', type='wireless', signal=16, link_rate=25, allow_or_block='Allow', device_type=None, device_model=None, ssid=None, conn_ap_mac=None), Device(name='<unknown>', ip='192.168.2.11', mac='E8:AB:FA:63:F8:F5', type='wireless', signal=54, link_rate=70, allow_or_block='Allow', device_type=None, device_model=None, ssid=None, conn_ap_mac=None), Device(name='MI9SE-MI9SE', ip='192.168.2.103', mac='60:AB:67:E4:C1:B8', type='wireless', signal=54, link_rate=422, allow_or_block='Allow', device_type=None, device_model=None, ssid=None, conn_ap_mac=None), \
            Device(name='GALAXY-S20', ip='192.168.2.108', mac='26:EE:34:DA:C2:54', type='wireless', signal=98, link_rate=187, allow_or_block='Allow', device_type=None, device_model=None, ssid=None, conn_ap_mac=None), Device(name='MI9SE-MI9SE', ip='192.168.2.115', mac='60:AB:67:E6:EB:B5', type='wireless', signal=32, link_rate=317, allow_or_block='Allow', device_type=None, device_model=None, ssid=None, conn_ap_mac=None), Device(name='ESP_52C4B0', ip='192.168.2.105', mac='C8:2B:96:52:C4:B0', type='wireless', signal=24, link_rate=56, allow_or_block='Allow', device_type=None, device_model=None, ssid=None, conn_ap_mac=None), \
            Device(name='SAMSUNG-GALAXY-S7', ip='192.168.2.113', mac='8C:F5:A3:69:C7:51', type='wireless', signal=48, link_rate=93, allow_or_block='Allow', device_type=None, device_model=None, ssid=None, conn_ap_mac=None), Device(name='<unknown>', ip='192.168.2.101', mac='00:04:4B:49:A4:7F', type='wired', signal=100, link_rate=None, allow_or_block='Allow', device_type=None, device_model=None, ssid=None, conn_ap_mac=None), Device(name='ESP_95DC0D', ip='192.168.2.104', mac='C4:4F:33:95:DC:0D', type='wireless', signal=26, link_rate=56, allow_or_block='Allow', device_type=None, device_model=None, ssid=None, conn_ap_mac=None), \
            Device(name='ESP_59BCBE', ip='192.168.2.107', mac='C8:2B:96:59:BC:BE', type='wireless', signal=40, link_rate=70, allow_or_block='Allow', device_type=None, device_model=None, ssid=None, conn_ap_mac=None), Device(name='MI9-MI9', ip='192.168.2.114', mac='A8:9C:ED:BF:25:D4', type='wireless', signal=48, link_rate=634, allow_or_block='Allow', device_type=None, device_model=None, ssid=None, conn_ap_mac=None), Device(name='<unknown>', ip='192.168.2.10', mac='E8:AB:FA:68:74:6F', type='wireless', signal=46, link_rate=50, allow_or_block='Allow', device_type=None, device_model=None, ssid=None, conn_ap_mac=None), \
            Device(name='RASPBERRYPI', ip='192.168.2.3', mac='B8:27:EB:EB:E3:5A', type='wired', signal=100, link_rate=None, allow_or_block='Allow', device_type=None, device_model=None, ssid=None, conn_ap_mac=None), Device(name='NB-DN36FC2', ip='192.168.2.100', mac='00:0E:C6:E1:D7:12', type='wired', signal=100, link_rate=None, allow_or_block='Allow', device_type=None, device_model=None, ssid=None, conn_ap_mac=None), Device(name='HUAWEI_MATEPAD_PRO-70EE54', ip='192.168.2.102', mac='22:D1:2C:9A:3B:E6', type='wireless', signal=42, link_rate=457, allow_or_block='Allow', device_type=None, device_model=None, ssid=None, conn_ap_mac=None), \
            Device(name='PARADISET', ip='192.168.2.2', mac='5C:26:0A:46:D5:99', type='wired', signal=100, link_rate=None, allow_or_block='Allow', device_type=None, device_model=None, ssid=None, conn_ap_mac=None), Device(name='<unknown>', ip='192.168.2.110', mac='2C:26:17:D0:3D:1A', type='wireless', signal=86, link_rate=845, allow_or_block='Allow', device_type=None, device_model=None, ssid=None, conn_ap_mac=None), Device(name='HUAWEI_MEDIAPAD_M5-4B80F6', ip='192.168.2.116', mac='A8:7D:12:22:84:A0', type='wireless', signal=66, link_rate=317, allow_or_block='Allow', device_type=None, device_model=None, ssid=None, conn_ap_mac=None), \
            Device(name='HUAWEI_MATEPAD_PRO-FD899D', ip='192.168.2.111', mac='1A:B2:FC:4E:F6:40', type='wireless', signal=94, link_rate=845, allow_or_block='Allow', device_type=None, device_model=None, ssid=None, conn_ap_mac=None), Device(name='HUAWEI_MEDIAPAD_M5-194E58', ip='192.168.2.120', mac='A8:7D:12:22:84:96', type='wireless', signal=40, link_rate=114, allow_or_block='Allow', device_type=None, device_model=None, ssid=None, conn_ap_mac=None), Device(name='<unknown>', ip='192.168.2.129', mac='00:04:4B:3A:54:3E', type='wired', signal=100, link_rate=None, allow_or_block='Allow', device_type=None, \
            device_model=None, ssid=None, conn_ap_mac=None), Device(name='GOOGLE-HOME-MINI', ip='192.168.2.109', mac='44:07:0B:8C:7D:2A', type='wireless', signal=30, link_rate=317, allow_or_block='Allow', device_type=None, device_model=None, ssid=None, conn_ap_mac=None)]
