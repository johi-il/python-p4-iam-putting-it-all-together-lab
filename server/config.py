#!/usr/bin/env python3

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from sqlalchemy import MetaData

# Configure Flask app first
app = Flask(__name__)
app.secret_key = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# Define metadata for database tables
metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

# Create SQLAlchemy instance with metadata
db = SQLAlchemy(metadata=metadata)

# Initialize SQLAlchemy with app
db.init_app(app)

# Initialize Flask-Migrate with app and db (order matters!)
migrate = Migrate(app, db)

# Initialize other extensions
bcrypt = Bcrypt(app)
api = Api(app)

