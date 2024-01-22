from flask import Flask , jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from form import NewCafe

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        dict = {column.name : getattr(self,column.name) for column in self.__table__.columns}
        return dict





@app.route('/cafes')
def cafes():
    cafes_list = Cafe.query.all()
    print(cafes_list)
    return render_template('index.html', cafes=cafes_list)


@app.route('/cafe/<id>')
def cafe_id(id):
    cafe = Cafe.query.get(id)
    return render_template('cafe.html', cafe=cafe)


@app.route('/add_cafe', methods=['GET','POST'])
def add_cafe():
    form = NewCafe()
    if form.validate_on_submit():
        data = form.data
        new_cafe = Cafe(name = data['name'], map_url = data['map_url'], img_url = data['img_url'], 
                        location = data['location'], seats = data['seats'], has_toilet = data['has_toilet'],
                        has_wifi = data['has_wifi'], has_sockets = False, 
                        can_take_calls = False,
                        coffee_price = data['coffee_price'])
        db.session.add(new_cafe)
        db.session.commit()
        return redirect('cafes')
    return render_template('add_cafe.html', form = form)

@app.route('/delete_cafe/<id>')
def delete_cafe(id):
    print(id)
    cafe_to_delete = db.get_or_404(Cafe, id)    
    db.session.delete(cafe_to_delete)
    db.session.commit()
    return redirect(url_for('cafes'))

if __name__ == '__main__':
    app.run(debug=True)