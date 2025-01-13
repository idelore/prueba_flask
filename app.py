# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 12:32:43 2025

@author: idelore
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "¡Hola, mundo!"

if __name__ == "__main__":
    app.run(debug=True)
