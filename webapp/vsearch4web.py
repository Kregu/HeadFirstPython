from flask import Flask
from flask import render_template, request, escape
from vsearch import search4letters


app = Flask(__name__)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
def view_the_log() -> 'html':
    contents = []
    with open('vsearch.log', 'r') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))

        return render_template('viewlog.html',
                               the_title='View Log:',
                               the_row_titles=('Form Data', 'Remote_addr', 'User_agent', 'Results'),
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
    with open('vsearch.log', 'a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')


if __name__ == '__main__':
    app.run(debug=True)
