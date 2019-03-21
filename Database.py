import sqlite3


class SQL:
    connection = None
    c = None

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
        classname VARCHAR(50),
        attributes VARCHAR(50),
        methods VARCHAR(50)
        );
        """)



    @staticmethod
    def insert_data_into_table():
        classes = [("PEP8Converter", "null", "find_class()"),
                   ("ClassFinder", "all_my_classes", "convert_class()",
                    "Controller", "self.view = View", "start_menu",
                    "View", "null", "print_menu")]
        for aClass in classes:
            format_str = """INSERT INTO class (classname, attributes, methods)
            VALUES ("{classname}", "{attributes}", "{methods}");"""
            SQL.c.execute(format_str.format(classname=aClass[0], attributes=aClass[1], methods=aClass[2]))
            # never forget this, if you want the changes to be saved:
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


SQL.connect_to_db("assignment1")
SQL.create_class_table()
SQL.insert_data_into_table()
SQL.fetch_all_class_data()
SQL.disconnect_db()