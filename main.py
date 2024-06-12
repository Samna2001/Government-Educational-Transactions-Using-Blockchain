from flask import Flask
from public import public
from admin import admin
from rdd import rdd
from ad import ad
from dde import dde
from deo import deo
from aeo import aeo
app=Flask(__name__)
app.secret_key="aaa"
app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(rdd)
app.register_blueprint(ad)
app.register_blueprint(dde)
app.register_blueprint(deo)
app.register_blueprint(aeo)
app.run(debug=True,port=5550)