# Python-ukol

To implement this command line application, we can break down the requirements into specific tasks:

1. **Setting Up the Database**:
   - Use PostgreSQL as the relational database.
   - Create tables for IP addresses, URLs, and data sources (origins).

2. **Fetching Data**:
   - Fetch data from the specified URLs using Python's `requests` library.

3. **Processing Data**:
   - Parse and extract IP addresses and URLs from the fetched data.
   - Determine the origin of each data point based on the source URL.

4. **Storing Data**:
   - Store the processed data into the PostgreSQL database.
   - Ensure uniqueness for each IP address and URL.

5. **Command Line Interface**:
   - Create a simple CLI using Python's `argparse` library to trigger the fetch and store operations.

Here's a high-level implementation outline:

1. **Database Setup**:

```python
import psycopg2

def setup_database():
    conn = psycopg2.connect("dbname='iocs' user='user' host='localhost' password='password'")
    cur = conn.cursor()

    # Create tables
    cur.execute("""
    CREATE TABLE IF NOT EXISTS ip_addresses (
        id SERIAL PRIMARY KEY,
        ip_address VARCHAR(15) UNIQUE NOT NULL,
        origin VARCHAR(255) NOT NULL
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS urls (
        id SERIAL PRIMARY KEY,
        url TEXT UNIQUE NOT NULL,
        origin VARCHAR(255) NOT NULL
    )
    """)

    conn.commit()
    cur.close()
    conn.close()
```

2. **Fetching and Processing Data**:

```python
import requests

DATA_SOURCES = {
    "urlhaus": "https://urlhaus.abuse.ch/downloads/csv_recent/",
    "alienvault": "http://reputation.alienvault.com/reputation.data",
    "openphish": "https://openphish.com/feed.txt"
}

def fetch_data():
    for origin, url in DATA_SOURCES.items():
        response = requests.get(url)
        if response.status_code == 200:
            data = response.text.split("\n")
            process_data(data, origin)
```

3. **Storing Data**:

```python
def process_data(data, origin):
    conn = psycopg2.connect("dbname='iocs' user='user' host='localhost' password='password'")
    cur = conn.cursor()

    for line in data:
        # Assuming IP addresses are standalone in lines and URLs start with "http"
        if line.startswith("http"):
            cur.execute("INSERT INTO urls (url, origin) VALUES (%s, %s) ON CONFLICT (url) DO NOTHING", (line, origin))
        else:
            cur.execute("INSERT INTO ip_addresses (ip_address, origin) VALUES (%s, %s) ON CONFLICT (ip_address) DO NOTHING", (line, origin))

    conn.commit()
    cur.close()
    conn.close()
```

4. **CLI**:

```python
import argparse

def main():
    parser = argparse.ArgumentParser(description="Fetch and store IOCs from various data sources.")
    parser.add_argument("--fetch", action="store_true", help="Fetch IOCs and store in the database.")
    args = parser.parse_args()

    if args.fetch:
        fetch_data()

if __name__ == "__main__":
    main()
```

This is a high-level implementation and might need refinements, especially in data parsing. It also doesn't handle all possible errors, so you might want to add appropriate error handling for a production-ready tool.
