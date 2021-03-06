from os import close
from stud_netgear_lib import NetgearEnhanced
import pandas as pd
from flask import Flask
import json
from tabulate import tabulate


# -*- coding: utf-8 -*-
""" A Python class/program that can query and setup certain Netgear routers"""
#
# https://github.com/roblandry/pynetgear_enhanced
# pip3 install pynetgear_enhanced
#
# Since we are mocking (fakeing) the pynetgear_enhanced lib we don not need
# and should NOT install anything for this examination program to work!
#

header = """
<!doctype html>
<html lang='en'>

<head>
    <link rel='stylesheet' href='style.css' />
    <meta charset='utf-8' />
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <title>Netgear router info</title>
</head>

<header>
    <h1>Poor network admins info</h1>
</header>"""

title_one = "<h2>Netgear router information </h2>"
title_two = "<h2>Traffic Volume in Megabytes | (Week or Month / Average)</h2>"
title_three = "<h2>Connected devices to router</h2>"
footer = """
<footer>
    <h3>Copyrighted by Mikael INC.</h3>
</footer>
</html>
"""

def main():
    """main function"""
    #
    # 1. First task is to let Python write a static web page with stats according to the attached index.html page
    #    Connected devices to router should be sorted by IP-adress, Name, Type or not sorted when no parameter is given
    #    Traffic Volume in Megabytes | (Week or Month / Average) should be formatted according to the attached html page
    #    html. Header and footer should be present so one can style the page if neccessary
    #
    # 2. Second task is similar to first task and can share code
    #    but we generate the web page as a dynamic web page with real-time stats when a client is browsing a specific URL
    #    Connected devices to router should be sorted by IP-adress, Name or Type from a given URL parameter or not sorted when no param is given
    #    You should create a new python file for this task
    #
    netgear = NetgearEnhanced(user='admin', password='admin', ssl=True)

    open("index.html", "w")

    data_devices = netgear.get_attached_devices()
    df_devices = pd.DataFrame.from_dict(data_devices)
    devices_html = df_devices.to_html()

    # F??rst??r inte hur man skall kombinera de 2 kolumnerna f??r att f?? det att se ut som det skall.
    # Du sa att det ??r b??ttre att forts??tta p?? uppgift nummer 2 ist??llet f??r b s?? jag tar ?? g??r det men den h??r anser jag vara klar till 99% f??rutom det d??.
    # Dock har vi ju redan gjort exakt samma som p?? 1.b) i labb 4 s?? tror nog att du vet att jag kan det.
    data_stats = netgear.get_traffic_meter_statistics()
    df_stats = pd.DataFrame(data_stats)
    stats = df_stats.transpose()
    stats_html = stats.to_html()

    data_info = netgear.get_info()
    data = pd.Series(data_info)
    df_info = pd.DataFrame(data)
    info_html = df_info.to_html()


    with open("./templates/index.html", "w") as f:
        f.write(header)
        f.write(title_one)
        f.write(info_html)
        f.write(title_two)
        f.write(stats_html)
        f.write(title_three)
        f.write(devices_html)
        f.write(footer)
        print("passed.")


if __name__ == "__main__":
    main()
