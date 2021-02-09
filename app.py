from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///content.db'
db = SQLAlchemy(app)


class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    intro = db.Column(db.String(200), nullable=False)
    text = db.Column(db.Text, nullable=False)
    text = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Articles %r>' % self.id


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about_me')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
