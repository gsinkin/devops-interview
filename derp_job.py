import json

from app import db, redis_client, KeyValue


def derp_it():
    is_derp = {"derp": True}
    derp_json = json.dumps(is_derp)
    for key_value in KeyValue.query.all():
        key_value.value = is_derp
        redis_client.set(key_value.key_id, derp_json)
    db.session.commit()


if __name__ == "__main__":
    derp_it()
