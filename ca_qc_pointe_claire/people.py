from utils import CanadianScraper, CanadianPerson as Person

COUNCIL_PAGE = 'http://www.pointe-claire.ca/fr/ville/conseil-municipal/membres'


class PointeClairePersonScraper(CanadianScraper):
    def scrape(self):
        page = self.lxmlize(COUNCIL_PAGE)

        councillors = page.xpath('//section[contains(@id, "js-council-member")]')
        assert len(councillors), 'No councillors found'
        for index, councillor in enumerate(councillors):
            name = ' '.join(councillor.xpath('.//h2/text()'))
            district = councillor.xpath('.//span[contains(@class, "c-info-list_label")][contains(text(), "District ")]')
            role = 'Conseiller'

            if not district and index == 0:
                district = 'Pointe-Claire'
                role = 'Maire'
            elif district:
                district = district[0].text_content().split(' – ')[0]

            p = Person(primary_org='legislature', name=name, district=district, role=role)
            p.image = councillor.xpath('.//@src')[0]
            p.add_contact('email', self.get_email(councillor))
            p.add_contact('voice', self.get_phone(councillor, area_codes=[514]), 'legislature')
            p.add_source(COUNCIL_PAGE)
            yield p
