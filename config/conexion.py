from sqlalchemy import *
from sqlalchemy.orm import *

DATABASE_URL ="sqlite:///config/base_datos"

engine_creator = create_engine(DATABASE_URL, echo=True)

sesion_local = sessionmaker(bind= engine_creator, autoflush=False, autocommit =False)

Base = declarative_base()


