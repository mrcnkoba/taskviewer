from flask import Flask, jsonify, render_template, request, abort
from Service.Services import TaskService
from Web.auth import requires_auth

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
@requires_auth
def index():
    user = request.authorization.username
    return render_template('index.html')


@app.route('/api/task', methods=['POST'])
def create():
    if not request.json:
        abort(400)

    title = request.form['title']
    task_service = TaskService()
    task_service.create_task(title, user)
    return jsonify(success=True)


@app.route('/api/task', methods=['GET'])
def get_tasks():
    task_service = TaskService()
    tasks = task_service.get_all_tasks()
    return jsonify(tasks=tasks)


if __name__ == '__main__':
    app.run(debug=True)
