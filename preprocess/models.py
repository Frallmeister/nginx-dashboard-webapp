from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

"""
class Titanic(Base):
    __tablename__ = "titanic"

    id_: Mapped[int] = mapped_column(primary_key=True)
    survived: Mapped[int] = mapped_column(nullable=True)
    pclass: Mapped[int] = mapped_column(nullable=True)
    sex: Mapped[str] = mapped_column(String(10), nullable=True)
    age: Mapped[float] = mapped_column(nullable=True)
    sibsp: Mapped[int] = mapped_column(nullable=True)
    parch: Mapped[int] = mapped_column(nullable=True)
    fare: Mapped[float] = mapped_column(nullable=True)
    embarked: Mapped[str] = mapped_column(String(20), nullable=True)
    class_: Mapped[str] = mapped_column(String(10), nullable=True)
    who: Mapped[str] = mapped_column(String(10), nullable=True)
    adult_male: Mapped[bool] = mapped_column(nullable=True)
    deck: Mapped[str] = mapped_column(String(10), nullable=True)
    embark_town: Mapped[str] = mapped_column(String(20), nullable=True)
    alive: Mapped[str] = mapped_column(String(10), nullable=True)
    alone: Mapped[bool] = mapped_column(nullable=True)

    def __repr__(self):
        return f"<Titanic id={self.id_}, survived={self.survived}>"
"""

class Diamonds(Base):
    __tablename__ = "diamonds"

    id_: Mapped[int] = mapped_column(primary_key=True)
    carat: Mapped[float] = mapped_column(nullable=True)
    cut: Mapped[str] = mapped_column(String(255), nullable=True)
    color: Mapped[str] = mapped_column(String(255), nullable=True)
    clarity: Mapped[str] = mapped_column(String(255), nullable=True)
    depth: Mapped[float] = mapped_column(nullable=True)
    table: Mapped[float] = mapped_column(nullable=True)
    price: Mapped[int] = mapped_column(nullable=True)
    # x: Mapped[float] = mapped_column(nullable=True)
    # y: Mapped[float] = mapped_column(nullable=True)
    # z: Mapped[float] = mapped_column(nullable=True)

    def __repr__(self):
        return f"<Diamonds id={self.id_}, carat={self.carat}, price={self.price}>"