# -*- coding: utf-8 -*-

"""Top-level package for flask_platform."""

__author__ = """Gillian Donlon"""
__email__ = 'gillian.donlon@ucdconnect.ie'
__version__ = '0.1.0'


from flask import Flask
app = Flask(__name__)
from flask_platform import views
