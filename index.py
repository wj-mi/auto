# -*- coding:utf-8 -*-
from flask import Flask, render_template,\
    request, g
import sqlite3
from contextlib import closing

# configuration
DATABASE = '/tmp/index.db'
DEBUG = True
SECRET_KEY = 'wert!@#$lkj'
USERNAME = 'admin'
PASSWORD = '123456'

app = Flask(__name__)
app.config.from_object(__name__)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('data_struct.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


@app.route("/", methods=['GET', 'POST', 'OPTIONS'])
def index():
    if request.method == 'POST':
        things = request.form.get("things", "")
        g.db.execute('insert into entries (text) values (?)', [things])
        g.db.commit()
    things = g.db.execute('select id, text from entries')
    things = [dict(id=row[0], text=row[1]) for row in things.fetchall()]
    return render_template('hello.html', name=things)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
