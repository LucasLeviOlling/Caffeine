import psycopg2
import cred
from psycopg2 import Error

try:
    # Connect to an existing database
    connection = psycopg2.connect(user=cred.USR,
                                  password=cred.PASS,
                                  host="127.0.0.1",
                                  port="5432",
                                  database="redbull-tracker")

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)




def main():
    list_flavours()
    print("All the flavours:")
    list_flavours()

def list_flavours():
    cursor = connection.cursor()
    cursor.execute("SELECT naam FROM flavours")
    record = cursor.fetchone()
    for item in record:
        print(item)
    cursor.close()



if __name__ == "__main__":
    main()

if (connection):
    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")

