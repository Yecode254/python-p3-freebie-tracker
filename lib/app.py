from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from models import Base ,Dev , Company, Freebie

engine = create_engine("sqlite:///freebies.db")
Session = sessionmaker(bind= engine)
session = Session()


Base.metadata.create_all(engine)

freebies = session.query(Freebie).all()
for f in freebies:
    print(f"{f.itame_name} given to {f.dev.name} by {f.company.name}")