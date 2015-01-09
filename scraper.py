import urllib2
from bs4 import BeautifulSoup

class daily_

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
        am_hieght = tds[0].contents[0]
        pm_hieght = tds[1].contents[0]
        conditions.append([day am_cond + am_hieght + pm_cond + pm_hieght)
    return conditions




address = 'http://www.swellinfo.com/surf-forecast/ocean-beach-california-nw'
soup = url_to_soup(address)




"""
if __name__ == "__main__":
    address = 'http://www.swellinfo.com/surf-forecast/ocean-beach-california-nw'
    soup = url_to_soup(address)
    print soup
"""

"""
#Create list of spots we want to check
address = []
address.append('http://www.swellinfo.com/surf-forecast/ocean-beach-california-nw')
address.append('http://www.swellinfo.com/surf-forecast/ocean-beach-california')
address.append('http://www.swellinfo.com/surf-forecast/half-moon-bay-california')
address.append('http://www.swellinfo.com/surf-forecast/pescadero-california')
address.append('http://www.swellinfo.com/surf-forecast/davenport-california')
address.append('http://www.swellinfo.com/surf-forecast/santa-cruz-california')
"""