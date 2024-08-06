from db import db


class AttractionDictionary(db.Model):
    __tablename__ = 'ars_attraction_dictionary'

    pk_attraction_dictionary_id = db.Columns(db.Integer, primary_key=True)
    attraction_name = db.Columns(db.String(128), nullable=True)
    is_in_use = db.Columns(db.Boolean(), nullable=True, default=True)
