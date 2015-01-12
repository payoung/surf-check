from flask import Flask, render_template, url_for
import datetime
from scraper import run_scraper


app = Flask(__name__)
# Keep track of the time between scrapes to prevent uncessesarry requests
LAST_SCRAPE = datetime.datetime.now()
# Get an intial set of scaped data
SPOT_CONDITIONS = run_scraper()
print LAST_SCRAPE, SPOT_CONDITIONS
# Intervals between scrapes
DELTA = datetime.timedelta(hours=4)


def get_cond_data():
    """ Test """
    global SPOT_CONDITIONS
    now = datetime.datetime.now()
    if now - LAST_SCRAPE > DELTA:
        SPOT_CONDITIONS = run_scraper()
    return SPOT_CONDITIONS


@app.route('/')
def surfs_up():
    """ 
    Returns surf forecast.  If the scraped data is old (DELTA = 4 hours), then
    new data is scraped.  Otherwise 
    """
    spot_conditions = get_cond_data()
    return render_template('main.html', last_update=str(LAST_SCRAPE),
                           spots=spot_conditions)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
