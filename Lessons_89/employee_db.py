from sqlalchemy import URL, Column, Integer, MetaData, String, Boolean, TIMESTAMP, Table, create_engine
from sqlalchemy.orm import declarative_base


db_url = URL.create(
    drivername="postgresql",
    username="x_clients_user",
    password="axcmq7V3QLCQwgL39GymqgasJhUlDbH4",
    host="dpg-cl53o6ql7jac73cbgi2g-a.frankfurt-postgres.render.com",
    database="x_clients"
)
engine = create_engine(db_url)
Base = declarative_base()


class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True)
    is_active = Column(Boolean, default=True)
    create_timestamp = Column(TIMESTAMP)
    change_timestamp = Column(TIMESTAMP)
    first_name = Column(String)
    last_name = Column(String)
    middle_name = Column(String)
    phone = Column(String)
    email = Column(String)
    avatar_url = Column(String)
    company_id = Column(Integer)


Base.metadata.create_all(engine)
