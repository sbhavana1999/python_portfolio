from flask import Flask, render_template,redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5


app = Flask(__name__)


#DB Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy()
db.init_app(app)

#bootstrap
bootstrap = Bootstrap5(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable=False)
    item = db.Column(db.String)
    done = db.Column(db.Boolean)


with app.app_context():
    db.create_all()    

@app.route('/todo', methods=["GET","POST"])
def todo():
    items = Todo.query.all()
    if request.method == "POST":
        new_item = request.form.get("new_item")
        done = request.form.get("item_done")
        print(done)
        if new_item != None:
            new_todo = Todo(item=new_item, done=False)
            db.session.add(new_todo)
            db.session.commit()
        return redirect(url_for('todo'))
    return render_template('index.html', todo_list=items)

@app.route('/delete/<id>')
def delete_item(id):
    item_to_delete = db.get_or_404(Todo, id)
    db.session.delete(item_to_delete)
    db.session.commit()
    return redirect(url_for('todo'))

@app.route('/update_item/<id>')
def update_item(id):
    update_item = db.get_or_404(Todo, id)
    update_item.done = True
    db.session.commit()
    return redirect(url_for('todo'))


if __name__ == "__main__":
    app.run(debug=1)