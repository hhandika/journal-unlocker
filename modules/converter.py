#!/usr/bin/python

import re, webbrowser as wb, click

#Convert the address to lsu library address. Setup click command line function
def convert_url(web,libs):
    '''
    A function to open paywalled scientific papers using lsu library access. 
    It takes paywalled journal/article urls or full doi web address. 
    '''
    com = '.com'
    org = '.org'
    edu = '.edu'
    if com in web:
        split_url = web.split('.com')
        #unpack the url
        first_part, second_part = split_url
        #Replace dot in the first part to dash
        first_part = first_part.replace('.','-')
        #Merge all the url components
        lsulib_address = first_part + '-com.' + libs + second_part
        return lsulib_address
    if org in web:
        split_url = web.split('.org')
        #unpack the url
        first_part, second_part = split_url
        #Replace dot in the first part to dash
        first_part = first_part.replace('.','-')
        #Merge all the url components
        lsulib_address = first_part + '-org.' + libs + second_part
        return lsulib_address
    if edu in web:
        split_url = web.split('.edu')
        #unpack the url
        first_part, second_part = split_url
        #Replace dot in the first part to dash
        first_part = first_part.replace('.','-')
        #Merge all the url components
        lsulib_address = first_part + '-edu.' + libs + second_part
        return lsulib_address
    else:
        print('Sorry... the url is not supported') 
