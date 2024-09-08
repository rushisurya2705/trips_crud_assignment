from mysql.connector import Error

def get_all_trips(conn):
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM trips")
        trips = cursor.fetchall()
        return trips
    except Error as e:
        print(f"Error fetching trips: {e}")
        return []
    finally:
        cursor.close()

def get_trip_by_id(conn, trip_id):
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM trips WHERE id = %s", (trip_id,))
        trip = cursor.fetchone()
        return trip
    except Error as e:
        print(f"Error fetching trip: {e}")
        return None
    finally:
        cursor.close()

def create_trip(conn, name, location, price):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO trips (name, location, price) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, location, price))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"Error creating trip: {e}")
        conn.rollback()
        return None
    finally:
        cursor.close()

def delete_trip_by_id(conn, trip_id):
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM trips WHERE id = %s", (trip_id,))
        conn.commit()
    except Error as e:
        print(f"Error deleting trip: {e}")
        conn.rollback()
    finally:
        cursor.close()
