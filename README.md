# surf-check

A little app that scrapes some surf websites and presents the surf conditions in a more concise format.  Normally, I would have to click through a handful of web pages (heavily loaded with grahics and advertisements, e.g. very slow to load) to check the different conditions at all the local spots.  Instead, the program scrapes the relevant data and displays it all on a single page.  I use Python's urllib2 and BeutifulSoup4 to get the data and Flask and simple html/css to serve the data to the web.

Installation
------------
After cloning the repo, setup the virtual environment in the project directory with `virtualenv .` and activate it with `. bin/activate`.  If you have pip, install the dependencies using `pip install -r requirements.txt`.  Run the application with `python views.py`

Additional Notes
-----------
To prevent over-scraping, I limit the scrapes to when a request is made to the Flask server.  I keep the data in a cache for a few hours (the forecast data is only good for ~6-12 hours before it becomes obsolete), so that additional page requests will load fairly quickly, and this further limits the number of times I have to scrape the forecast website.  The downside to this approach is that the first request can take up to 10 seconds to load because it has to wait for the scraping to complete (as I mentioned earlier, the pages are pretty bulky).

If I was less conscientious about scraping, I would have the scraper run on a schedule that would closely track the update schedule of the forecast website.  This would ensure that the data was ready to go upon request and the page load would be pretty fast.

Demo
----
http://surfcheck.pyoung.net/

Other Resources
---------------

http://www.blog.pyoung.net/2015/01/13/surf-check/


