import sqlalchemy as sa
from sqlalchemy import orm
from datetime import timedelta

from .db_session import SqlAlchemyBase


class Notes(SqlAlchemyBase):
    __tablename__ = 'notes'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    team_leader = sa.Column(sa.Integer, sa.ForeignKey('users.id'))
    note = sa.Column(sa.String, nullable=True)
    work_size = sa.Column(sa.Integer, nullable=True)
    collaborators = sa.Column(sa.String, nullable=True)
    is_finished = sa.Column(sa.Boolean, nullable=True)

    user_team_leader = orm.relationship('User')
