from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Dev(Base):
    __tablename__ = 'devs'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    freebies = relationship("Freebie", back_populates="dev")

    @classmethod
    def get_freebies(cls, session, dev_id):
        dev = session.query(cls).filter_by(id=dev_id).first()
        if dev:
            return dev.freebies
        return []

class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    freebies = relationship("Freebie", back_populates="company")

    @classmethod
    def get_freebies(cls, session, company_id):
        company = session.query(cls).filter_by(id=company_id).first()
        if company:
            return company.freebies
        return []

class Freebie(Base):
    __tablename__ = 'freebies'
    id = Column(Integer, primary_key=True)
    item_name = Column(String, nullable=False)
    value = Column(Integer)
    dev_id = Column(Integer, ForeignKey('devs.id'))
    company_id = Column(Integer, ForeignKey('companies.id'))

    dev = relationship("Dev", back_populates="freebies")
    company = relationship("Company", back_populates="freebies")

