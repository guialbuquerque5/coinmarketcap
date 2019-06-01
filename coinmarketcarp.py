# -*- coding: utf-8 -*-
import json
import requests
import csv
import time

from bs4 import BeautifulSoup
path = '//*[@id="historical-data"]/div/div[2]/table/tbody'
#r = requests.get('https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20190517&end=20190523')

def write_txt(_str):
    text_file = open("bitcoin.txt", "a")
    text_file.write(_str.encode('utf-8'))
    text_file.close()
def read_file(f):
    with open(f, 'r') as file:
        data = file.read().replace('\n', '')
        file.close
        return data

#----------0-----1-------2-------3---------4------5----------6-------#
format = 'Date	Open*	High	Low	Close**	Volume	Market Cap'

def get_rows(data):
    soup = BeautifulSoup(data,'html.parser')
    table = soup.find("table")
    rows = table.find("tbody").find_all("tr")
    result = []
    temp = []
    
    for row in rows:
        temp = []
        fields = row.find_all("td")
        temp.append(str(fields[0].get_text()).replace(', ',' y:'))
        for i in range(1,len(fields)):
            field = fields[i].get('data-format-value')
            if(field != '-'):
                field.replace('.', ',')
                print field
                temp.append(field)
            else:
                temp.append(field)
        result.append(temp)
    return result

def write_data(file_name,data):
    directory = 'data'
    with open(directory+'/'+file_name, mode='w+') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
       ##Cabeçalho
        header = ['Date','Open', 'high', 'Low', 'Close', 'Volume', 'MarketCap']
        writer.writerow(header)
        for row in data:
            writer.writerow(row)
    csvfile.close()
#write_data('bitcoin.csv',get_rows(r.text))


def get_coin_names(): #return coins names
    with open('coins.json') as json_file:  
        data = json.load(json_file)
        json_file.close()
        return data['coin']

def download_data():
    coins = get_coin_names()
    for coin in coins:
        time.sleep(5)
        print(coin)
        r = requests.get('https://coinmarketcap.com/currencies/'+coin+'/historical-data/?start=20130428&end=20190524')
        print(r)
        write_data(coin+'.csv',get_rows(r.text))
download_data()


