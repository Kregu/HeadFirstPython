from flask import Flask
from flask import render_template
from vsearch import search4letters

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    render_template()


@app.route('/search4')
def do_search() -> str:
    return str(search4letters('qeradfzcv', 'azsx'))


app.run()
