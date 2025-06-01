#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Dev , Company , Freebie

engine = create_engine('sqlite:///freebies.db')
Base.metadata.bind = engine 
Session = sessionmaker(bind=engine)
session = Session()
# Script goes here!
company1= Company(name="HeatUp")
company2 = Company(name = "YegoTech")

dev1 = Dev(name="Eddy", age=28)
dev2= Dev(name= "Pennie", age=17)

freebie1 = Freebie(item_name= "Oraimo-Headset",value=10,dev= dev1,company=company1)
freebie2 = Freebie(item_name= "Iphone16-Promax",value=17,dev= dev2,company=company2)
freebie3 = Freebie(item_name= "Markbook-air7",value=28,dev= dev1,company=company2)


session.add_all([company1,company2,dev1,dev2,freebie1,freebie2,freebie3])
session.commit()

print("seed data added sucesfully")