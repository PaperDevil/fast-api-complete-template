from datetime import datetime

import sqlalchemy
from sqlalchemy import Column, Table, ForeignKey, Integer, String, DateTime, Sequence, CheckConstraint, Text, Boolean
from sqlalchemy.sql import expression

naming_convention = {
    'all_column_names': lambda constraint, table: '_'.join([
        column.name for column in constraint.columns.values()
    ]),
    'ix': 'ix__%(table_name)s__%(all_column_names)s',
    'uq': 'uq__%(table_name)s__%(all_column_names)s',
    'ck': 'ck__%(table_name)s__%(all_column_names)s',
    'fk': (
        'fk__%(table_name)s__%(all_column_names)s__'
        '%(referred_table_name)s'
    ),
    'pk': 'pk__%(table_name)s'
}

metadata = sqlalchemy.MetaData(naming_convention=naming_convention)

user_table = Table(
    'user', metadata,
    Column('id', Integer, Sequence('user_id_seq', start=1), primary_key=True),
    Column('created_at', DateTime, nullable=False, default=datetime.now),
    Column('edited_at', DateTime, nullable=False, default=datetime.now, onupdate=datetime.now),
    Column('is_delete', Boolean, default=False, server_default=expression.false(), nullable=False),
    Column('phone', String(10), CheckConstraint('char_length(phone) <= 11'), unique=True, nullable=False),
    Column('email', Text, CheckConstraint('char_length(email) >= 4 AND char_length(email) <= 100'), unique=True),
    Column('login', String(64), CheckConstraint('char_length(login) >= 2 AND char_length(login) <= 64'), unique=True),
    Column('hash_password', Text, CheckConstraint('char_length(hash_password) >= 3 AND char_length(hash_password) <= 1000')),
    Column('first_name', String(32), CheckConstraint('char_length(first_name) >= 2 AND char_length(first_name) <= 32')),
    Column('middle_name', String(32), CheckConstraint('char_length(middle_name) >= 2 AND char_length(middle_name) <= 32')),
    Column('last_name', String(32), CheckConstraint('char_length(last_name) >= 2 AND char_length(last_name) <= 32')),
)
