from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A simple list to store tasks
tasks = []

@app.route('/', methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        task_title = request.form.get('task')
        if task_title:
            tasks.append({"title": task_title, "done": False})
        return redirect(url_for('todo'))
    return render_template('todo.html', tasks=tasks)

@app.route('/complete/<int:index>')
def complete(index):
    if 0 <= index < len(tasks):
        tasks[index]['done'] = not tasks[index]['done']
    return redirect(url_for('todo'))

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect(url_for('todo'))

app.run(debug=True)
