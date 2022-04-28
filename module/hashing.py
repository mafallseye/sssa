from distutils.log import debug
from flask import Flask, request, jsonify
import pymongo
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)


@app.route('/<password>')
def index(password):

    module = request.get_json()
    client = pymongo.MongoClient(host="localhost", port=27017)
    db = client.passe
    hash_collect = db["hash"]

    hash_value = generate_password_hash(password, method='sha256')
    # stores_password = 'pbkdf2:sha256:150000$WolKDNSv$dccc6dc09a428121e483de1400556ca32b358bfd2bcc4e8d22565197852bba56'
    # result = check_password_hash(stores_password, password)
    # return hash_value

    user = {
        "username": module["username"],
        "password": hash_value
    }
    hash_collect.insert_one(user)

    return jsonify(user), 200


if __name__ == '__main__':
    app.run(debug=True)
