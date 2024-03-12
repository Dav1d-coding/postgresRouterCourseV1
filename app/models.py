from sqlalchemy import  Column, Integer, String
from config import Base

class PageData(Base):
    __tablename__ = "course_data"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    route = Column(String)
    page_data = Column(String)