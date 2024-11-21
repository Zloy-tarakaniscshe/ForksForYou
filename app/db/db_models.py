from typing import List
from datetime import datetime
from sqlalchemy import Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, Mapped, relationship, mapped_column, Email


class Base(DeclarativeBase):
    ...


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(100), unique=True, email=True)
    address: Mapped[List["Tasks"]] = relationship(back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User(name={self.name!r}, fullname={self.fullname!r}, email={self.email!r})>"


class Tasks(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    user: Mapped["User"] = relationship(back_populates="address")
    task_name: Mapped[str] = mapped_column(String(30))
    task_description: Mapped[str] = mapped_column(String(100))
    task_status: Mapped[str] = mapped_column(String(100))
    task_date: Mapped[datetime] = mapped_column(DateTime, nullable=False, server_default=func.now())

    def __repr__(self):
        return f"<Tasks(task_name={self.task_name!r}, task_description={self.task_description!r}, task_status={self.task_status!r}, task_date={self.task_date!r})>"


