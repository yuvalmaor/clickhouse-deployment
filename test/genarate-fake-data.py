from clickhouse_driver import Client
import random

# Connect to ClickHouse via port-forwarded service
myport = "9000"  # Change port if necessary
client = Client('localhost', port=myport, user='default', password='', database='default')

# Generate fake data and insert it into the shard_table_distributed
for i in range(100):  # Insert 100 rows for testing
    id = random.randint(1, 10000)  # Random id for better distribution
    name = f"Name_{random.randint(1, 1000)}"
    age = random.randint(20, 50)
    
    # Insert data into the data_table_distributed
    client.execute('''
        INSERT INTO data_table_distributed (id, name, age)
        VALUES
    ''', [(id, name, age)])

print("Fake data inserted into data_table_distributed.")
