#!/usr/bin/env python
# encoding: utf-8
from flask import Flask, request
import time
import json

import analyse
from user import User

app = Flask(__name__)

# get开头接口取自数据库
# query开头接口实时获取

@app.route('/api/v1/confirmName', methods=['POST'])
def confirmName():
    student_id = request.form.get('student_id')
    name = User.getName(student_id)
    return name[:-1]+"*"


@app.route('/api/v1/getName', methods=['POST'])
def getName():
    student_id = request.form.get('student_id')
    name = User.getName(student_id)
    return name


@app.route('/api/v1/savePassword', methods=['POST'])
def savePassword():
    student_id = request.form.get('student_id')
    password = request.form.get('password')
    result = analyse.testPassword(student_id, password)
    if (result == 'error'):
        return 'error'
    User.savePassword(student_id, password)
    return 'ok'


@app.route('/api/v1/saveInfo', methods=['POST'])
def saveInfo():
    student_id = request.form.get('student_id')
    password = request.form.get('password')
    user = analyse.saveStudentInfo(student_id, password)
    return 'ok'


@app.route('/api/v1/getInfo', methods=['POST'])
def getInfo():
    student_id = request.form.get('student_id')
    password = request.form.get('password')
    u = User.getInfo(student_id, password)
    info = {
        "department" : u.department,
        "grade" : u.grade,
        "major" : u.major,
        "name" : u.name,
        "sex" : u.sex,
        "class_id" : u.class_id,
        "student_id" : u.student_id,
        "student_status" : u.student_status,
        "card_id" : u.card_id,
        "ecard_id" : u.ecard_id,
        "birthday" : u.birthday,
        "mobile" : u.mobile,
        "bound" : u.bound
    }
    return json.dumps(info)


@app.route('/api/v1/queryScore', methods=['POST'])
def queryScore():
    student_id = request.form.get('student_id')
    password = request.form.get('password')
    year = request.form.get('year') if request.form.get('year') else str(int(time.strftime('%Y',time.localtime(time.time())) )-1)
    term = request.form.get('term') if request.form.get('term') else '1'
    if (int(student_id[:4]) >= 2015):
        scoreList = analyse.getScoreFor15(student_id, password, year, term)
    else:
        scoreList = analyse.getScoreFor14(student_id, year, term)
    return json.dumps(scoreList)


if __name__ == '__main__':
    app.run()