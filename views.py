from flask import Flask, render_template, url_for
from datetime import datetime
from scraper import run_scraper


app = Flask(__name__)
LAST_SCRAPE = 0


@app.route('/')
def surfs_up():
    """ return surf forecast """
    now = datetime.now()
    if LAST_SCRAPE == 0:
        spot_conditions = run_scraper()
    return render_template('main.html', last_update=str(LAST_SCRAPE),
                           spots=spot_conditions)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
