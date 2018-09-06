import json
import werkzeug
from flask import Flask, jsonify, url_for, send_from_directory
from flaskext.mysql import MySQL
from flask_restplus import Resource, Api, reqparse, inputs
import logging
from logging.handlers import RotatingFileHandler

APP = Flask(__name__)
API = Api(APP, doc="/doc", title="SmartView Quality")
MYSQL = MySQL()
