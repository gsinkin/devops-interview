import json
import os

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import redis

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
db = SQLAlchemy(app)
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOSTNAME", "localhost"),
    port=os.getenv("REDIS_PORT", 6379),
    db=0
)


class KeyValue(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    key_id = db.Column(db.String(80), unique=True, nullable=False)
    value = db.Column(db.JSON, nullable=False)


db.create_all()


@app.route("/key/<key_id>", methods=["GET"])
def get_value(key_id):
    result = redis_client.get(key_id)
    if result is None:
        result = db.session.query(KeyValue).filter(
            KeyValue.key_id == key_id
        ).first()
        result = result.value if result else None
    else:
        result = json.loads(result.decode())
    return jsonify({key_id: result if result else None})


@app.route("/key/<key_id>", methods=["POST"])
def set_value(key_id):
    request_data = request.data.decode()
    request_json = json.loads(request_data)
    existing = db.session.query(KeyValue).filter(
        KeyValue.key_id == key_id
    ).first()
    if existing:
        existing.value = request_json
    else:
        db.session.add(KeyValue(key_id=key_id, value=request_json))

    result = redis_client.set(key_id, request_data)
    db.session.commit()
    return ("", 204)
