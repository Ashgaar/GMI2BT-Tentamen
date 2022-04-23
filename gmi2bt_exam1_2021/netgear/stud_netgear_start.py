# -*- coding: utf-8 -*-
""" A Python class/program that can query and setup certain Netgear routers"""
#
# https://github.com/roblandry/pynetgear_enhanced
# pip3 install pynetgear_enhanced
#
# Since we are mocking (fakeing) the pynetgear_enhanced lib we don not need
# and should NOT install anything for this examination program to work!
#

from stud_netgear_lib import NetgearEnhanced

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

    netgear.get_...

if __name__ == "__main__":
    main()
