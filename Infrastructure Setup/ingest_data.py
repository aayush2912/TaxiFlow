import os
import argparse
from time import time
import pandas as pd
from sqlalchemy import create_engine
import requests

def main(params):
    user = params.user
    password = params.password
    host = params.host 
    port = params.port 
    db = params.db
    table_name = params.table_name
    url = params.url
    
    # Download the parquet file
    parquet_name = 'output.parquet'
    def download_file(url, filename):
        response = requests.get(url, stream=True)
        with open(filename, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

    download_file(url, "output.parquet")

    # Create SQLAlchemy engine
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    # Read parquet file in chunks
    if not os.path.exists("output.parquet"):
        raise FileNotFoundError("Parquet file error.")

    df = pd.read_parquet("output.parquet")
    
    # Convert date columns
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    # Calculate number of chunks
    chunk_size = 100000
    num_chunks = len(df) // chunk_size + 1

    # Create table schema
    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    # Insert data chunk by chunk
    for i in range(num_chunks):
        t_start = time()
        
        chunk_start = i * chunk_size
        chunk_end = min((i + 1) * chunk_size, len(df))
        df_chunk = df.iloc[chunk_start:chunk_end]

        if not df_chunk.empty:
            df_chunk.to_sql(name=table_name, con=engine, if_exists='append')
            t_end = time()
            print('Inserted chunk %d/%d, took %.3f second' % (i+1, num_chunks, t_end - t_start))

    print("Finished ingesting data into the postgres database")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest Parquet data to Postgres')
    parser.add_argument('--user', required=True, help='user name for postgres')
    parser.add_argument('--password', required=True, help='password for postgres')
    parser.add_argument('--host', required=True, help='host for postgres')
    parser.add_argument('--port', required=True, help='port for postgres')
    parser.add_argument('--db', required=True, help='database name for postgres')
    parser.add_argument('--table_name', required=True, help='name of the table where we will write the results to')
    parser.add_argument('--url', required=True, help='url of the parquet file')

    args = parser.parse_args()
    main(args)