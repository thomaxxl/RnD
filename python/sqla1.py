from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
 
from sqlalchemy import create_engine
engine = create_engine('sqlite:////tmp/db.sqlite') # 
 
from sqlalchemy import Column, Text, String
class Header(Base):
    __tablename__ = 'headers'
    url = Column(String(500), unique=True, nullable=False,  primary_key=True)
    data = Column(Text)
 
Base.metadata.create_all(engine)
 
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
 
import requests
url = "https://python-forum.io"
r = requests.get(url)
 
h = Header(url=url, data = str(r.headers))
print(h.data)
 
session.add(h)
session.commit()

