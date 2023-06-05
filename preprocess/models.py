from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

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

    def __repr__(self):
        return f"<Diamonds id={self.id_}, carat={self.carat}, price={self.price}>"