import mysql.connector

def create_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='thanh1',
        database='hotel'
    )
    return connection

# Example usage
if __name__ == "__main__":
    conn = create_connection()
    if conn.is_connected():
        print("Connected to MySQL database")
    conn.close()
