#!/usr/bin/env python
# -*- coding: utf8 -*-
import databases
import ormar
import sqlalchemy


metadata = sqlalchemy.MetaData()
database = databases.Database("sqlite:///sqlite.db")
engine = sqlalchemy.create_engine("sqlite:///sqlite.db",convert_unicode=True,echo=True)


class MainMata(ormar.ModelMeta):
    metadata = metadata
    database = database
