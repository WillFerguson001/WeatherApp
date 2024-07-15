import sqlite3

def create_database_parks():
    conn = sqlite3.connect('metservice_parks.db')
    c = conn.cursor()

    # Drop existing table if it exists
    c.execute('DROP TABLE IF EXISTS Regions')

    # Create table with a primary key
    c.execute('''
        CREATE TABLE Regions (
            id INTEGER PRIMARY KEY,  -- Ensures id is unique and a primary key
            title TEXT, today_date TEXT, tomorrow_date TEXT,
            today_overview TEXT, tomorrow_overview TEXT,
            today_weather_hazards TEXT, tomorrow_weather_hazards TEXT,
            today_issue_time TEXT, tomorrow_issue_time TEXT
        )
    ''')

    conn.commit()
    conn.close()


def update_database_parks(data):
    conn = sqlite3.connect('metservice_parks.db')
    c = conn.cursor()

    try:
        print("Inserting new data into database...")
        # Insert new data into the table
        c.execute('''INSERT INTO Regions (title, today_date, tomorrow_date, today_overview, tomorrow_overview,
                     today_weather_hazards, tomorrow_weather_hazards, today_issue_time, tomorrow_issue_time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', data)
        conn.commit()
        print("New data added to database.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

