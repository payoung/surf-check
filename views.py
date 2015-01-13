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
    """ 
    Returns a dictionary of spot conditions. Uses a global to save the forecast
    data between requests.  If the app has just been initialized, it will run
    the scrpaer, ohterwise, it will re-run the scraper if the last scrape is 
    over 4 hours old.
    """
    global SPOT_CONDITIONS, LAST_SCRAPE
    now = datetime.datetime.now()
    if now - LAST_SCRAPE > DELTA:
        SPOT_CONDITIONS = run_scraper()
        LAST_SCRAPE = now
    return SPOT_CONDITIONS


@app.route('/')
def surfs_up():
    """ Returns surf forecast. """
    spot_conditions = get_cond_data()
    return render_template('main.html', last_update=str(LAST_SCRAPE),
                           spots=spot_conditions)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
