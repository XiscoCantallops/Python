#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#Author: eduar766
from requests import get, exceptions

def check_internet_connection():
    try:
        get('http://google.com', timeout = 3)
        print('connected')
    except exceptions.ConnectionError:
        print('not connected')

check_internet_connection()
