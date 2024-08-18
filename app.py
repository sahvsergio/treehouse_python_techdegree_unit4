from models import (Base, session,
                    Product,engine)
import csv
import datetime
import os  


def clean_date(date_str):
    '''Turns the string into a date object'''
    
    split_date=date_str.split('/')
    month=int(split_date[0])
    day=int(split_date[1])
    year=int(split_date[2])
    
    

    return datetime.date(year,month,day)

def clean_quantity(qty_str):
   
    return int(qty_str)


def clean_price(price_str):
    price_float=float(price_str)
    return int(price_float*100)
   
   
    
  
    

def add_csv():
    with open('inventory.csv') as csvfile:
        data=csv.DictReader(csvfile)
       
        for row in data:
            product_name=row['product_name']
            product_price=clean_price(row['product_price'])
            product_quantity=clean_quantity(row['product_quantity'])
            date=clean_date(row['date_updated'])
         
            
          
          

if __name__=='__main__':
    #Base.metadata.create_all(engine)
    add_csv()
    #clean_date('11/1/2018')
