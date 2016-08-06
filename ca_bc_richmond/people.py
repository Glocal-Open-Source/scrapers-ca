from __future__ import unicode_literals
from utils import CanadianScraper, CanadianPerson as Person

COUNCIL_PAGE = 'http://www.richmond.ca/cityhall/council/about/members.htm'
CONTACT_URL = 'http://www.richmond.ca/contact/departments/council.htm'


class RichmondPersonScraper(CanadianScraper):

    def scrape(self):
        councillor_seat_number = 1

        contact_page = self.lxmlize(CONTACT_URL)
        email = self.get_email(contact_page)

        page = self.lxmlize(COUNCIL_PAGE)
        for url in page.xpath('//a/@href[contains(., "members/")]'):
            page = self.lxmlize(url)
            role, name = page.xpath('//h1//text()')[0].split(' ', 1)
            photo_url = page.xpath('//img/@src')[0]

            if role == 'Mayor':
                district = 'Richmond'
            else:
                district = 'Richmond (seat {})'.format(councillor_seat_number)
                councillor_seat_number += 1

            p = Person(primary_org='legislature', name=name, district=district, role=role)
            p.image = photo_url
            p.add_source(COUNCIL_PAGE)
            p.add_source(CONTACT_URL)
            p.add_source(url)
            p.add_contact('email', email)  # same for all
            yield p
