from flask import Flask, request, jsonify
import bcrypt
"""from .required_packages import (
    Blueprint,db001,resJson,adminCred,requests,passwdKey,del_user,
    pymongo,encode_auth_token,app,get_otoken,json,post_event,keystoneEndpoint,
    ObjectId,jsonify,checkPasswd,tokenValidation,mail_sender,validation,
)
"""
import json
from optparse import Values
from uuid import uuid4
import uuid
from flask import Flask, jsonify, request, Blueprint
from flask_swagger_ui import get_swaggerui_blueprint
from pymongo import MongoClient
from passlib.hash import pbkdf2_sha256
import pymongo

AUTH_REQUEST = Blueprint("password", __name__)


@AUTH_REQUEST.route('/register', methods=['POST'])
def registerUser():
    module = request.get_json()
    client = pymongo.MongoClient(host="localhost", port=27017)
    db = client.application
    user_collection = db["passwordhash"]

    #insert in db
    account = {
        "username": module["username"],
        "password": pbkdf2_sha256.encrypt(module["password"])
    }
    account['password'] = pbkdf2_sha256.encrypt(
        account['password'])
    user_collection.insert_one(account)

    return jsonify(account), 200
