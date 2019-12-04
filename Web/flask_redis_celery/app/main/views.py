# -*- coding: utf-8 -*-

# @Time    : 2019/11/26
# @Author  : Lattine

# ======================
import random
from flask import Flask, jsonify, url_for
from . import main
from .tasks import main_task


@main.route("/long-task", methods=["GET", "POST"])
def long_task():
    task_flag = "task_" + str(random.randint(1, 100))
    task = main_task.apply_async(args=[task_flag])
    return jsonify({'Location': url_for('main.task_status', task_id=task.id), 'task_flag': task_flag})


@main.route("/task-status/<task_id>/", methods=["GET", "POST"])
def task_status(task_id):
    task = main_task.AsyncResult(task_id)
    if task.state == 'PENDING':
        response = {
            'state': task.state,
            'current': 0,
            'total': 'calculating...',
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'current': task.info.get('current', 0),
            'total': task.info.get('total', 1),
            'status': task.info.get('status', '')
        }
        if 'result' in task.info:
            response['result'] = task.info['result']
    else:
        # 异常反馈
        response = {
            'state': task.state,
            'current': 1,
            'total': 1,
            'status': str(task.info),  # this is the exception raised
        }
    return jsonify(response)
