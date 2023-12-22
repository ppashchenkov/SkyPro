from sqlalchemy import URL, Column, Integer, MetaData, String, Boolean, TIMESTAMP, Table, create_engine

metadata_obj = MetaData()


employee_table = Table(
    "employee",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("first_name", String),
    Column("last_name", String),
    Column("phone", String),
    Column("company_id", Integer),
)
