from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


engine = create_engine('sqlite:///candledb.db')

Session = sessionmaker(bind=engine)
session = Session()


Base = declarative_base()


class Symbol(Base):
    __tablename__ = 'symbols'
    symbol_id = Column(Integer, primary_key=True)
    symbol_name = Column(String, unique=True)



class Candle(Base):
    __tablename__ = 'candles'
    candle_id = Column(Integer, primary_key=True)
    symbol_id = Column(Integer, ForeignKey('symbols.symbol_id'))
    timestamp = Column(String)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)

    symbol = relationship(Symbol)


