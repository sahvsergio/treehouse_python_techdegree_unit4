from sqlalchemy import create_engine

# Initialize Sqlite database
engine=create_engine('sqlite://inventory.db')

# Create your database model called Product

## Attributes
###  Product_id=Primary_key, 
###  product_name, 
###  product_quantity, 
###  product_price,
###  date_updated.
