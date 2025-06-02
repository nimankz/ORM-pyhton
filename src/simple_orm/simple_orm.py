import sqlite3
from typing import Any, get_type_hints
import datetime

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

    def save(self):
        table = self.__class__.__name__.lower()
        fields = self.__class__.get_fields()
        values = [getattr(self, field) for field in fields]
        placeholders = ", ".join("?" for _ in values)
        columns = ", ".join(fields)
        sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        self.__class__.cursor.execute(sql, values)
        self.__class__.conn.commit()

    def update_by_ID(self, id: int):
        table = self.__class__.__name__.lower()
        fields = self.__class__.get_fields()
        values = [getattr(self, field) for field in fields]
        set_clause = ", ".join(f"{field} = ?" for field in fields)
        sql = f"UPDATE {table} SET {set_clause} WHERE id = ?"
        self.__class__.cursor.execute(sql, values + [id])
        self.__class__.conn.commit()

            
    
    
    def delete_by_ID(self, id: int):
        table = self.__class__.__name__.lower()
        sql = f"DELETE FROM {table} WHERE id = ?"
        self.__class__.cursor.execute(sql, (id,))
        self.__class__.conn.commit()




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
    def show_by_fiter(cls, **kwargs):
        table = cls.__name__.lower()
        conditions = " AND ".join(f"{k} = ?" for k in kwargs.keys())
        sql = f"SELECT * FROM {table} WHERE {conditions}"
        cls.cursor.execute(sql, tuple(kwargs.values()))
        rows = cls.cursor.fetchall()
        return rows