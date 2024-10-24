import mysql.connector
from mysql.connector import Error
from config import HOST, USER, PASSWORD


class DbConnectionError(Exception):
    pass

# Connect to the database
def _connect_to_db(db_name):
    try:
        cnx = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=db_name
        )
        return cnx
    except Error as e:
        raise DbConnectionError(f"Error connecting to database: {e}")

#Add a new sweet to db
def add_sweet(sweet):
    conn = _connect_to_db('sweet_shop')
    try:
        cursor = conn.cursor()
        query = """
        INSERT INTO sweets (name, price, description, stock_quantity, category, flavour, ingredients)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            sweet['name'],
            sweet['price'],
            sweet['description'],
            sweet['stock_quantity'],
            sweet['category'],
            sweet['flavour'],
            ', '.join(sweet['ingredients'])  # Join the list into a string
        ))
        conn.commit()  # Commit the transaction
    except Exception as e:
        raise DbConnectionError(f"Failed to add sweet: {e}")
    finally:
        cursor.close()
        conn.close()

# Get all sweets in db
def get_all_sweets():
    conn = _connect_to_db('sweet_shop')
    try:
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM sweets"
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Exception as e:
        raise DbConnectionError(f"Failed to fetch all sweets: {e}")
    finally:
        cursor.close()
        conn.close()

#Select all sweets from db from specific id
def get_sweet_by_id(sweet_id):
    conn = _connect_to_db('sweet_shop')
    try:
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM sweets WHERE sweet_id = %s"
        cursor.execute(query, (sweet_id,))
        result = cursor.fetchone()  # Fetch one record
        return result
    except Exception as e:
        raise DbConnectionError(f"Failed to fetch sweet with ID {sweet_id}: {e}")
    finally:
        cursor.close()
        conn.close()

# Get sweet by name from db
def get_sweet_by_name(name):
    conn = _connect_to_db('sweet_shop')
    try:
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM sweets WHERE name = %s"
        cursor.execute(query, (name,))
        result = cursor.fetchone()  # Fetch one record
        return result
    except Exception as e:
        raise DbConnectionError(f"Failed to fetch sweet with name {name}: {e}")
    finally:
        cursor.close()
        conn.close()


# Deleting sweet
# def delete_sweet(sweet_id):
#     conn = _connect_to_db('sweet_shop')
#     try:
#         cursor = conn.cursor()
#         query = "DELETE FROM sweets WHERE sweet_id = %s"
#         cursor.execute(query, (sweet_id,))
#         conn.commit()
#     except Exception as e:
#         raise DbConnectionError(f"Failed to delete sweet with ID {sweet_id}: {e}")
#     finally:
#         cursor.close()
#         conn.close()

#Getting stock level of a sweet by its name
def get_stock_level(name):
    conn = _connect_to_db('sweet_shop')
    try:
        cursor = conn.cursor(dictionary=True)
        query = "SELECT stock_quantity FROM sweets WHERE name = %s"
        cursor.execute(query, (name,))
        result = cursor.fetchone()  # Fetch one record
        return result
    except Exception as e:
        raise DbConnectionError(f"Failed to get stock level for {name}: {e}")
    finally:
        cursor.close()
        conn.close()

#Updating stock level when order placed
def update_stock_level(name, quantity):
    if quantity < 0:
        raise ValueError("Stock cannot be negative")
    conn = _connect_to_db('sweet_shop')
    try:
        cursor = conn.cursor()
        query = "UPDATE sweets SET stock_quantity = %s WHERE name = %s"
        cursor.execute(query, (quantity, name))
        conn.commit()
    except Exception as e:
        raise DbConnectionError(f"Failed to update stock level for {name}: {e}")
    finally:
        cursor.close()
        conn.close()

#Add order details to orders db
def add_order(name, sweet, cost):
    conn = _connect_to_db('sweet_shop')
    try:
        cursor = conn.cursor()
        query = """
        INSERT INTO orders (customer_name, sweet_ordered, total_cost)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (name, sweet, cost))
        conn.commit()  # Commit the transaction
    except Exception as e:
        raise DbConnectionError(f"Failed to add order to db: {e}")
    finally:
        cursor.close()
        conn.close()

# Get total cost of order
def get_cost(quantity, name):
    conn = _connect_to_db('sweet_shop')
    try:
        cursor = conn.cursor(dictionary=True)
        query = "SELECT price FROM sweets WHERE name = %s"
        cursor.execute(query, (name,))
        result = cursor.fetchone()

        if result is None:
            raise ValueError(f"Sweet '{name}' not found in the database.")

        price_per_unit = result['price']
        total_cost = price_per_unit * quantity
        return total_cost

    except Exception as e:
        raise DbConnectionError(f"Failed to get cost for {name}: {e}")

    finally:
        cursor.close()
        conn.close()
