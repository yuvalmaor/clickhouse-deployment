from clickhouse_driver import Client

# Connect to ClickHouse via port-forwarded service
myport = "9000"
client = Client('localhost', port=myport, user='default', password='', database='default')

# Rest of the code remains the same


# #1. Create a test table
# client.execute('''
#     CREATE TABLE IF NOT EXISTS test_table (
#         id UInt32,
#         name String,
#         age UInt32
#     ) ENGINE = ReplicatedMergeTree('/clickhouse/tables/{shard}/test_table', '{replica}')
#     ORDER BY id;
# ''')

# # 2. Insert some test data
# i=0
# base=i

# while i<2000:
#     data = [
#         (10+i, 'Alice'+str(i), 30),
#         (11+i, 'Bob'+str(i), 25),
#         (12+i, 'Charlie'+str(i), 35)
#     ]
#     client.execute('INSERT INTO data_table (id, name, age) VALUES', data)
#     i=i+3
#     if (i-base) % 1000 == 0:
#         print("Inserted", i, "records")

#3. Query the data
#result = client.execute('SELECT * FROM test_table')
# print("mypoort:", myport)
# # 4. Print the result
# print("Data in test_table:")
# for row in result:
#     print(row)
#client.execute('DROP TABLE IF EXISTS test_table')
result = client.execute('SHOW CREATE TABLE  test_table')
print(result)
ports=["9000","9002","9003","9004","9005"]

for myport in ports:
    print("**************\nmyport:", myport)
    try:
        client = Client('localhost', port=myport, user='default', password='', database='default')
        result = client.execute('SELECT * FROM default.data_table')
        #print("mypoort:", myport)
        # 4. Print the result
        print("Data in data_table:")
        r=0
        for row in result:
            print(row)
            r=r+1
            if r>20:
                break
        try:
            client = Client('localhost', port=myport, user='default', password='', database='default')
            tables = client.execute('SHOW TABLES')
            print("Tables in database:")
            for table in tables:
                print(table[0])
        except Exception as inner_e:
            print(f"Error listing tables on port {myport}: {inner_e}")

        #client.execute('DROP TABLE IF EXISTS test_table')
    except:
        print("Error in port:", myport)
        try:
            client = Client('localhost', port=myport, user='default', password='', database='default')
            tables = client.execute('SHOW TABLES')
            print("Tables in database:")
            for table in tables:
                print(table[0])
        except Exception as inner_e:
            print(f"Error listing tables on port {myport}: {inner_e}")

# 5. Clean up by dropping the test table
#client.execute('DROP TABLE IF EXISTS test_table')
