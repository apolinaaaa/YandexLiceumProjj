import sqlalchemy as sa
import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    surname = sa.Column(sa.String, nullable=True)
    name = sa.Column(sa.String, nullable=True)
    age = sa.Column(sa.Integer, nullable=True)
    position = sa.Column(sa.String, nullable=True)
    speciality = sa.Column(sa.String, nullable=True)
    address = sa.Column(sa.String, nullable=True)
    email = sa.Column(sa.String, unique=True, nullable=True)
    hashed_password = sa.Column(sa.String, nullable=True)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

    def __repr__(self):
        return f'<Colonist> {self.id} {self.surname} {self.name}'

    @property
    def fio(self) -> str:
        return f'{self.surname} {self.name}'
