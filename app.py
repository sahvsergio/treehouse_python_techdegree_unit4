from models import (Base, session,
                    Product,engine)
import csv
import datetime
import os  


def menu():
    while True:
        print(
            '''
            Store Inventory

            \n* View a single product\'s inventory(v)
            \r*Add a new product to the database (a)
            \r* Make a backup of the entire inventory(b)
            
            ''')
        choice=input('What would you like to do?: ')
        if choice in ['v','a','b']:
            return choice
        else:
            input(
                '''
                \rPlease enter one of the options above
                \rletters a, b or v only
                \rPress enter to try again''')
        
            
       


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

def app():
    app_running=True
    while app_running:
        choice=menu()
        if choice=='v':
            #view a single product
            
            pass
        elif choice=='a':
            # add a product
            pass
       


        elif choice=='b':
            # create backup
            pass

        else:
            'Good bye'
            app_running=False
            
           
         
            
          
          

if __name__=='__main__':
    app()
    #Base.metadata.create_all(engine)
    #menu()
    #add_csv()
    #clean_date('11/1/2018')
