from models import (Base, session,
                    Product, engine)
import csv
import sys
import datetime
import os
import time


def menu():
    while True:
        print(
            '''
            Store Inventory

            \n* View a single product\'s inventory(v)
            \r*Add a new product to the database (a)
            \r*Make a backup of the entire inventory(b)

            ''')
        choice = input('What would you like to do?: ')
        if choice in ['v', 'a', 'b']:
            return choice
        else:
            input(
                '''
                \rPlease enter one of the options above
                
                \rletters a, b or v only
                
                \rPress enter to try again:''')
        print()


def view_product():
    try:
        product_id = int(input('Please enter the id of the product: '))
        print()
        print()
        desired_product=session.query(Product).filter(Product.product_id==product_id)
        if desired_product!=None:
            for product in desired_product:
                print(f'''
                      Product Name: {product.product_name}
                      Product Quantity:{product.product_quantity} units
                      Product Price:${product.product_price}            
                      Date last updated:{product.date_updated}          
              '''
              )
        if product_id >len(session.query(Product).all()):
            raise Exception('This  product id is not valid, please try again ')
        
    except ValueError:
        print(f'Please enter a valid value for the id -a number from  1-{len(session.query(Product).all())}')
        view_product()
    except Exception as e:
        print()
        print(e)
        print()
        view_product()
    else:
        time.sleep(5)
        print('returning to main menu')
        time.sleep(10)
        
        
        
        
    


def add_product():
    pass


def create_backup():
    pass


def clean_date(date_str):
    '''Turns the string into a date object'''

    split_date = date_str.split('/')
    month = int(split_date[0])
    day = int(split_date[1])
    year = int(split_date[2])

    return datetime.date(year, month, day)


def clean_quantity(qty_str):

    return int(qty_str)


def clean_price(price_str):
    #print(price_str)
    split_price=price_str.split('$')
   
    price_float =float(split_price[1])
    
    
    return int(price_float *100)


def add_csv():
    with open('inventory.csv') as csvfile:
        data = csv.DictReader(csvfile)

        for row in data:
            product_in_db=session.query(Product).filter(Product.product_name==row['product_name']).one_or_none()
            if product_in_db==None:
                product_name = row['product_name']
                product_price = clean_price(row['product_price'])
                product_quantity = clean_quantity(row['product_quantity'])
                date_updated = clean_date(row['date_updated'])
                new_product=Product(product_name = product_name, product_quantity = product_quantity, product_price = product_price, date_updated = date_updated )
                session.add(new_product)
           
                
        session.commit()


def app():
    add_csv()
    app_running = True
    while app_running:
        choice = menu()
        if choice == 'v':
            # view a single product
            view_product()
            pass

        elif choice == 'a':
            # add a product
            pass

        elif choice == 'b':
            # create backup
            pass
        else:
            app_running = False
            input(
                '''
                \rPlease enter one of the options above
                \rletters a, b or v only
                \rPress enter to try again: ''')

      


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app()
 
   
    
