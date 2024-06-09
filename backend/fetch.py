import psycopg2
import pandas as pd
from dotenv import load_dotenv
import os


load_dotenv()

# Connect to the PostgreSQL database
try:
    conn = psycopg2.connect(
            
            dbname=os.environ.get('DB_NAME'),
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASSWORD'),
            host=os.environ.get('DB_HOST'),
            port=os.environ.get('DB_PORT')
        )
    
    print("Connection to the database established successfully.")
except Exception as e:
    print(f"Error: {e}")

# Query to execute
query = "SELECT * FROM myschema.mydbtable;"

# Execute the query and fetch the data
try:
    df = pd.read_sql_query(query, conn)
    print("Query executed successfully.")
except Exception as e:
    print(f"Error: {e}")

# Display the data in a table format
print(df)

# Close the database connection
conn.close()
print("Database connection closed.")