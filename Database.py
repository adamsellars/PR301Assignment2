import sqlite3


class SQL:
    connection = None
    c = None
    classes = None

    @staticmethod
    def connect_to_db(db_name):
        try:
            SQL.connection = sqlite3.connect(db_name)

        except Exception as e:
            print(e)
        else:
            print("Opened database successfully")
        finally:
            print("Finishing connecting to database")
            SQL.c = SQL.connection.cursor()

    @staticmethod
    def create_class_table():
        SQL.c.execute("""
        CREATE TABLE IF NOT EXISTS class (
        key varchar(10),
        classname VARCHAR(150)
        );
        """)

    @staticmethod
    def insert_data_into_table(classes):
        for aClass in classes:
            format_str = """INSERT INTO class (key, classname)
            VALUES ("{key}", "{classname}");"""
            SQL.c.execute(format_str.format(key=aClass[0], classname=aClass[1]))
            SQL.connection.commit()

    @staticmethod
    def fetch_all_class_data():
        SQL.c.execute("SELECT * FROM class")
        print("fetchall:")
        result = SQL.c.fetchall()
        for r in result:
            print(r)

    @staticmethod
    def fetch_one_class_data():
        SQL.c.execute("SELECT * FROM class")
        print("\nfetch one:")
        res = SQL.c.fetchone()
        print(res)

    @staticmethod
    def disconnect_db():
        SQL.c.close()
        SQL.connection.close()


# classes = [("1", "Controller"), ("2", "View")]
# SQL.connect_to_db("assignment1")
# SQL.c.execute("""DROP TABLE class;""")
# SQL.create_class_table()
# SQL.insert_data_into_table()
# SQL.fetch_all_class_data()

