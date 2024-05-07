# -*- coding: utf-8 -*-

from flask import Flask, request, render_template

import json

__all__ = ['app']
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test/get', methods=['GET'])
def test_get():
    print('--> test/get, args:')
    params = ''
    for key, value in request.args.items():
        param = key + ':' + value
        print(param)
        params += param + '\n'

    return "Get args:\n" + params


@app.route('/test/post', methods=['POST'])
def test_post():
    print('--> test/post, args:')
    data = json.loads(request.data)
    for key, value in data.items():
        print(key, ':', value)

    return 'Input is:\n' + str(request.data)


