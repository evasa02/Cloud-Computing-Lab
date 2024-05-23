# Import the libraries we need
from pymongo import MongoClient
import requests




from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://saloninimgaonkar:66d2fHT5lWEaQrG9@cluster0.6ovojbj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


# Connect to the database with the connection string we got from Atlas, replacing user and password.
client = MongoClient('mongodb+srv://saloninimgaonkar:66d2fHT5lWEaQrG9@cluster0.6ovojbj.mongodb.net/test?retryWrites=true&w=majority')


# Next we define the database we are using.
# It does not have to exist first, like with relational databases.
db = client.get_database('coin_markets')

# Now, we make the API call and prices the results to the terminal.
prices = requests.get('https://api.coingecko.com/api/v3//coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false')
prices = prices.json()
print(prices)

# We define the collection we will store this data in,
# which is created dynamically like the database,
# and insert the data into the collection.
db_prices = db.get_collection('prices')
inserted = db_prices.insert_many(prices)
# Print a count of documents inserted.
print(str(len(inserted.inserted_ids)) + " documents inserted")