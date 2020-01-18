from flask import Flask
from flask import render_template, request, escape
from vsearch import search4letters
from DBcm import UseDatabase


app = Flask(__name__)
app.config['dbconfig'] = {'host': '127.0.0.1', 'user': 'vsearch', 'password': 'vsearchpasswd', 'database': 'vsearchlogDB', }

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """SELECT phrase, letters, ip, browser_string, results FROM log"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()

        return render_template('viewlog.html',
                               the_title='View Log',
                               the_row_titles=('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results'),
                               the_data=contents,)


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    title = 'Here are your results:'
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,)


def log_request(req: 'flask_request', res: str) -> None:
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = '''insert into log (phrase, letters, ip, browser_string, results) values (%s, %s, %s, %s, %s)'''
        cursor.execute(_SQL, (
                            req.form['phrase'],
                            req.form['letters'],
                            req.remote_addr,
                            req.user_agent.browser,
                            res,))


if __name__ == '__main__':
    app.run(debug=True)
