from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')


@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/query')
def query():
    return render_template('query.html')


@app.route('/tagset')
def tagset():
    return render_template('tagset.html')


@app.route('/info')
def info():
    return render_template('info.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


if __name__ == '__main__':
    app.run()
