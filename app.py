from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///content.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    intro = db.Column(db.String(200), nullable=False)
    text = db.Column(db.Text, nullable=False)
    release_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Articles %r>' % self.id


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about_me')
def about():
    return render_template("about.html")


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == "POST":
        title = request.form['title']
        intro = request.form['intro']
        text = request.form['text']
        article = Articles(name=title, intro=intro, text=text)
        try:
            db.session.add(article)
            db.session.commit()
            return redirect('/')
        except:

            return print("Error")

    else:
        return render_template("create.html")


if __name__ == "__main__":
    app.run(debug=True)
