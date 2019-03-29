import sqlite3


class SQL:
    connection = None
    c = None
    classes = None

    # Adam wrote this
    @staticmethod
    def connect_to_db(db_name):
        try:
            SQL.connection = sqlite3.connect(db_name)
        except PermissionError:
            return PermissionError
        except FileNotFoundError:
            return FileNotFoundError
        except AttributeError:
            return AttributeError
        except:
            return Exception
        else:
            SQL.c = SQL.connection.cursor()


    # Adam wrote this
    @staticmethod
    def create_class_table():
        SQL.c.execute("""
        CREATE TABLE IF NOT EXISTS class (
        key varchar(10),
        classname VARCHAR(150)
        );
        """)

    # Leroi wrote this
    @staticmethod
    def insert_data_into_table(classes):
        for aClass in classes:
            format_str = """INSERT INTO class (key, classname)
            VALUES ("{key}", "{classname}");"""
            SQL.c.execute(format_str.format(key=aClass[0], classname=aClass[1]))
            SQL.connection.commit()

    # Leroi wrote this
    @staticmethod
    def fetch_all_class_data():
        try:
            SQL.c.execute("SELECT * FROM class")
            result = SQL.c.fetchall()
        except PermissionError:
            return PermissionError
        except FileNotFoundError:
            return FileNotFoundError
        except AttributeError:
            return AttributeError
        except:
            return Exception
        else:
            return result

    # Leroi wrote this
    @staticmethod
    def disconnect_db():
        SQL.c.close()
        SQL.connection.close()
