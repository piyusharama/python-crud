from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Load configurations from environment variables
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'supersecretkey')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///items.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model for CRUD
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)

# Routes
@app.route('/')
def index():
    items = Item.query.all()
    return render_template('index.html', items=items)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        new_item = Item(name=name, description=description)
        db.session.add(new_item)
        db.session.commit()
        flash('Item added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    item = Item.query.get_or_404(id)
    if request.method == 'POST':
        item.name = request.form['name']
        item.description = request.form['description']
        db.session.commit()
        flash('Item updated successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('edit.html', item=item)

@app.route('/delete/<int:id>')
def delete(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    flash('Item deleted successfully!', 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=5000)