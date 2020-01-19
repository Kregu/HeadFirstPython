from flask import Flask, session
from flask import render_template, request, escape
from vsearch import search4letters
from DBcm import UseDatabase, ConnectionError, SQLError
from checker import check_logged_in


app = Flask(__name__)
app.config['dbconfig'] = {'host': '127.0.0.1', 'user': 'vsearch', 'password': 'vsearchpasswd', 'database': 'vsearchlogDB', }

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
@check_logged_in
def view_the_log() -> 'html':
    contents = []
    try:
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """SELECT phrase, letters, ip, browser_string, results FROM log"""
            cursor.execute(_SQL)
            contents = cursor.fetchall()
    except ConnectionError as err:
        print('***** Is your database switched in? Error:', str(err))
    except SQLError as err:
        print('***** Is your query correct? Error:', str(err))
    except Exception as err:
        print('Something went wrong:', str(err))

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
    try:
        log_request(request, results)
    except Exception as err:
        print('***** Logging failed with this error:', str(err))
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


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now loggen in.'


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out'


app.secret_key = 'SuperSecretKey1234'


if __name__ == '__main__':
    app.run(debug=True)
