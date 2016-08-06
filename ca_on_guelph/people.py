from __future__ import unicode_literals
from utils import CSVScraper

COUNCIL_PAGE = 'http://guelph.ca/city-hall/mayor-and-council/city-council/'


class GuelphPersonScraper(CSVScraper):
    csv_url = 'http://open.guelph.ca/wp-content/uploads/2015/01/GuelphCityCouncil2014-2018ElectedOfficalsContactInformation1.csv'
    many_posts_per_area = True
