import os
import sys
import whois
import datetime
import urllib.request
import argparse
import requests

def get_file_with_urls():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_with_list_of_sites', help='File have to include list of sites')
    arg = parser.parse_args()
    return arg.file_with_list_of_sites

def load_urls4check(file):
    if not os.path.exists(file):
        return None
    with open(file) as file_handler:
        return file_handler.read().splitlines()
 

def is_server_respond_with_200(url):
    response = requests.get(url)
    try:
        if response.status_code == 200:
            return 'status is up'
    except AttributeError:
        pass
    return 'status is down'
    

def get_domain_expiration_date(url):
    today = datetime.date.today()
    get_inf = whois.whois(url)
    exp_date = get_inf.expiration_date
    days = exp_date.date() - today
    return str(days)
    

if __name__ == '__main__':
    urls = load_urls4check(get_file_with_urls())
    for url in urls:
        print(url, is_server_respond_with_200(url), 'and will expire after', get_domain_expiration_date(url))
        

