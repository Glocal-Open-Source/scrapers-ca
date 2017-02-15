from utils import CanadianScraper, CanadianPerson as Person

COUNCIL_PAGE = 'http://www.villagesenneville.qc.ca/fr/membres-du-conseil-municipal'


class SennevillePersonScraper(CanadianScraper):
    def scrape(self):
        page = self.lxmlize(COUNCIL_PAGE)

        councillors = page.xpath('//div[@class="field-item even"]//tr')
        assert len(councillors), 'No councillors found'
        for councillor in councillors:
            district = councillor.xpath('./td[1]//strong/text()')[0].replace('no. ', '')
            role = 'Conseiller'
            if 'Maire' in district:
                district = 'Senneville'
                role = 'Maire'
            name = councillor.xpath('./td[2]//p//text()')[0].title()
            email = self.get_email(councillor)
            p = Person(primary_org='legislature', name=name, district=district, role=role)
            p.add_source(COUNCIL_PAGE)
            try:
                p.image = councillor.xpath('.//img/@src')[0]
            except IndexError:
                pass
            p.add_contact('email', email)
            yield p
