import sqlite3
from typing import Any, get_type_hints

class Model:
    conn = sqlite3.connect("orm.db")
    cursor = conn.cursor()

    def __init_subclass__(cls):
        fields = cls.get_fields()
        table_name = cls.__name__.lower()
        columns = ", ".join(f"{name} {cls.map_type(tp)}" for name, tp in fields.items())
        sql = f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, {columns})"
        cls.cursor.execute(sql)
        cls.conn.commit()

    

    def save(self):
        table = self.__class__.__name__.lower()
        fields = self.__class__.get_fields()
        values = [getattr(self, field) for field in fields]
        placeholders = ", ".join("?" for _ in values)
        columns = ", ".join(fields)
        sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        self.__class__.cursor.execute(sql, values)
        self.__class__.conn.commit()

    def update_by_ID(self,id:int ,column:str, newValue):
        table = self.__class__.__name__.lower()
        
        sql = f"UPDATE {table} SET {column} = {str(newValue)} WHERE id = {str(id)}"
        self.__class__.cursor.execute(sql)
        self.__class__.conn.commit()
    
    def delete_by_ID(self, id: int):
        table = self.__class__.__name__.lower()
        sql = f"DELETE FROM {table} WHERE id = ?"
        self.__class__.cursor.execute(sql, (id,))
        self.__class__.conn.commit()

    def show_row(self, id: int):
        table = self.__class__.__name__.lower()
        sql = f"SELECT * FROM {table} WHERE id = {id}"
        self.__class__.cursor.execute(sql)
        row = self.__class__.cursor.fetchone()
        return row

    @classmethod
    def all(cls):
        table = cls.__name__.lower()
        cls.cursor.execute(f"SELECT * FROM {table}")
        rows = cls.cursor.fetchall()
        return rows
    
    @classmethod
    def empty_table(cls):
        table = cls.__name__.lower()
        cls.cursor.execute(f"DELETE FROM {table}")
        cls.conn.commit()

    @classmethod
    def show_by_fiter(cls, conditions):
        table = cls.__name__.lower()  
        sql = f"SELECT * FROM {table} WHERE {conditions}"
        cls.cursor.execute(sql)
        rows = cls.cursor.fetchall()
        return rows
    @classmethod
    def inner_join(cls, other, on):
        table1 = cls.__name__.lower()
        table2 = other.__name__.lower()
        sql = f"SELECT * FROM {table1} INNER JOIN {table2} ON {on}"
        cls.cursor.execute(sql)
        rows = cls.cursor.fetchall()
        return rows

    @classmethod
    def get_fields(cls):
        return {k: v for k, v in get_type_hints(cls).items() if not k.startswith("_")}

    @staticmethod
    def map_type(tp: Any) -> str:
        return {
            str: "TEXT",
            int: "INTEGER",
            float: "REAL",
            bool: "INTEGER"  # SQLite stores booleans as 0 or 1
            
        }.get(tp, "TEXT")


