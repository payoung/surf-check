import urllib2
from bs4 import BeautifulSoup
from collections import OrderedDict


def parse_cond_attr(attribute):
    """ Parses the class attribute to get condition value """
    if "cond1" in attribute:
        return "Good"
    elif "cond2" in attribute:
        return "Fair"
    elif "cond3" in attribute:
        return "Poor"
    elif "cond0" in attribute:
        return "N/A"
    else:
        return "!Error!"


def url_to_data(address):
    """ Returns surf condition data from web page using bs4 """
    html = urllib2.urlopen(address).read()
    soup = BeautifulSoup(html)
    panel_divs = soup.findAll("div", {"class":"AccordionPanel"})
    conditions = []
    for panel in panel_divs:
        condition = panel.find("div")
        day = condition.contents[0].strip()
        am_cond = parse_cond_attr(condition.get("class")[1])
        tds = condition.findAll("td")
        pm_cond = parse_cond_attr(tds[1].get("class")[0])
        am_swell = tds[0].contents[0]
        pm_swell = tds[1].contents[0]
        cond_str = [day, am_swell + " " + am_cond, pm_swell + " " + pm_cond]
        conditions.append(cond_str)
    return conditions


def run_scraper():
    """ Runs through the list of spots and gets the scrapped data for each """
    surf_spots = ['Ocean Beach North', 'Ocean Beach South', 'Half Moon Bay', 
                  'Pescadero', 'Davenport', 'Santa Cruz']
    surf_urls = ['http://www.swellinfo.com/surf-forecast/ocean-beach-california-nw',
                 'http://www.swellinfo.com/surf-forecast/ocean-beach-california',
                 'http://www.swellinfo.com/surf-forecast/half-moon-bay-california',
                 'http://www.swellinfo.com/surf-forecast/pescadero-california',
                 'http://www.swellinfo.com/surf-forecast/davenport-california',
                 'http://www.swellinfo.com/surf-forecast/santa-cruz-california']
    spot_conditions = OrderedDict()
    for i in range(len(surf_spots)):
        spot_conditions[surf_spots[i]] = url_to_data(surf_urls[i])
    return spot_conditions


if __name__ == "__main__":
    ADDR = 'http://www.swellinfo.com/surf-forecast/ocean-beach-california-nw'
    TEST_COND = url_to_data(ADDR)
    for item in TEST_COND:
        print item
