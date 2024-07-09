import sqlite3
import pandas as pd

# Function to create a SQLite connection and load data
def create_sqlite_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to SQLite database: {db_file}")

        # Load data from CSV into SQLite
        csv_file = 'transformed_weather_data.csv'
        df = pd.read_csv(csv_file)

        # Write DataFrame to SQLite table
        df.to_sql('weather_data', conn, if_exists='replace', index=False)
        print("Data loaded into SQLite table successfully.")

    except sqlite3.Error as e:
        print(f"Error connecting to SQLite database: {e}")
    finally:
        if conn:
            conn.close()
            print("SQLite connection closed.")

# Main script
if __name__ == '__main__':
    db_file = 'weather_data.db'  # SQLite database file name
    create_sqlite_connection(db_file)
