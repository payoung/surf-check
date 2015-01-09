import urllib2
from bs4 import BeautifulSoup


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
        if day in ["Saturday", "Tuesday", "Wednesday"]:
            cond_str = (day + ":\t" + am_swell + " " + am_cond + "\t" + 
                        pm_swell + " " + pm_cond)
        else:
            cond_str = (day + ":\t\t" + am_swell + " " + am_cond + "\t" + 
                        pm_swell + " " + pm_cond)
        conditions.append(cond_str)
    return conditions


def run_scraper():
    surf_spots = ['http://www.swellinfo.com/surf-forecast/ocean-beach-california-nw',
                  'http://www.swellinfo.com/surf-forecast/ocean-beach-california',
                  'http://www.swellinfo.com/surf-forecast/half-moon-bay-california',
                  'http://www.swellinfo.com/surf-forecast/pescadero-california',
                  'http://www.swellinfo.com/surf-forecast/davenport-california',
                  'http://www.swellinfo.com/surf-forecast/santa-cruz-california']
    spot_conditions = []
    for spot in surf_spots:
        spot_conditions.append(url_to_data(spot))
    return spot_conditions


if __name__ == "__main__":
    address = 'http://www.swellinfo.com/surf-forecast/ocean-beach-california-nw'
    conditions = url_to_data(address)
    for item in conditions:
        print item
