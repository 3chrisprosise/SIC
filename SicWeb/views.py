# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(req):
    if req.method == "GET":
        return render(req, 'sicWeb/index.html')

def index2(req):
    if req.method == "GET":
        return render(req, 'sicWeb/index2.html')