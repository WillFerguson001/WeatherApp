import sqlite3
import os

def create_database_avalanche():
    conn = sqlite3.connect('avlanche_advisory.db')
    c = conn.cursor()

    # Drop existing table if it exists
    c.execute('DROP TABLE IF EXISTS Regions')

    # Create table with a primary key
    c.execute('''
        CREATE TABLE Regions (
            id INTEGER PRIMARY KEY,  -- Ensures id is unique and a primary key
            title TEXT, 
            risk_level_overview TEXT, 
            overview TEXT,
            issue_time TEXT,
            valid_time TEXT, 
            risk_level_high TEXT,
            risk_d_high TEXT, 
            risk_level_alpine TEXT,
            risk_d_alpine TEXT,
            risk_level_sub TEXT,
            risk_d_sub TEXT,
            problem_1 TEXT,
            risk_d_problem_1 TEXT,
            risk_trend_1 TEXT,
            risk_time_of_day TEXT,
            likelihood_problem1 TEXT,
            size_problem1 TEXT,
            problem_2 TEXT,
            risk_d_problem_2 TEXT,
            risk_trend_2 TEXT,
            risk_time_of_day_2 TEXT,
            likelihood_problem2 TEXT,
            size_problem2 TEXT,
            recent_avalanche_activity TEXT,
            current_snowpack_conditions TEXT,
            mountain_weather TEXT,
            sliding_danger TEXT)
    ''')

    conn.commit()
    conn.close()


def update_database_avalanche(data):
    conn = sqlite3.connect('avlanche_advisory.db')
    c = conn.cursor()

    try:
        print("Inserting new data into database...")
        # Insert new data into the table
        c.execute('''INSERT INTO Regions (title, 
            risk_level_overview, 
            overview,
            issue_time,
            valid_time, 
            risk_level_high,
            risk_d_high, 
            risk_level_alpine,
            risk_d_alpine,
            risk_level_sub,
            risk_d_sub,
            problem_1,
            risk_d_problem_1,
            risk_trend_1,
            risk_time_of_day,
            likelihood_problem1,
            size_problem1,
            problem_2,
            risk_d_problem_2,
            risk_trend_2,
            risk_time_of_day_2,
            likelihood_problem2,
            size_problem2,
            recent_avalanche_activity,
            current_snowpack_conditions,
            mountain_weather,
            sliding_danger) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', data)
        conn.commit()
        print("New data added to database.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()


def format_text_avalanche(row):
    conn = sqlite3.connect('avlanche_advisory.db')
    cursor = conn.cursor()

    # Construct the SQL query to select data from a specific row based on the input ID
    query = "SELECT * FROM Regions WHERE id = ?"
    cursor.execute(query, (row,))

    # Fetch the row
    data = cursor.fetchone()

    response1 = f"""
{data[1]} - {data[2]}
{data[4]}
{data[5]}
- Overview: {data[3]}

- Risk:
High Alpine: {data[6]}
Alpine: {data[8]}
Sub Alpine: {data[10]}
"""

    response2 = f"""
- Problem 1: {data[12]}
{data[13]}
- Trend: {data[14]}
- Time of day: {data[15]}
- Likelihood: {data[16]}/5
- Size: {data[17]}/5

- Problem 2: {data[18]}
{data[19]}
- Trend: {data[20]}
- Time of day: {data[21]}
- Likelihood: {data[22]}/5
- Size: {data[23]}/5"""

    response3 = f"""
- Recent Activity:
{data[24]}"""

    response4 = f"""
- Current Snowpack Conditions:
{data[25]}"""

    response5 = f"""
- Mountain Weather:
{data[26]}

- Sliding Danger:
{data[27]}
"""


    # Close the cursor and connection
    cursor.close()
    conn.close()

    # You can perform formatting or other operations here

    return response1, response2, response3, response4, response5


def deleteDB():
    if os.path.exists('avalanche_advisory.db'):
        os.remove('avalanche_advisory.db')
        print("Existing database deleted.")
    
    # Create a new database
    create_database_avalanche()
    print("New database created.")


# print(format_text_avalanche(1))