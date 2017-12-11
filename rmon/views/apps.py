#coding=utf-8

from flask import render_template
from flask.views import MethodView


class IndexView(MethodView):

    def get(self):
        return render_template("server/index.html")
