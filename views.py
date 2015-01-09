from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
def surfs_up():
	""" return surf forecast """
	return render_template('main.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
