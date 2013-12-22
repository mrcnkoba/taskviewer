from flask import Flask, jsonify, render_template, request, abort
from Service.TaskService import TaskService

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/task', methods=['POST'])
def create():
    if not request.json:
        abort(400)
    title = request.form['title']
    task_service = TaskService()
    task_service.create_task(title)
    return jsonify(success=True)


@app.route('/api/task', methods=['GET'])
def get_tasks():
    task_service = TaskService()
    tasks = task_service.get_all_tasks()
    return jsonify(tasks=tasks)
    
if __name__ == '__main__':
    app.run(debug=True)
