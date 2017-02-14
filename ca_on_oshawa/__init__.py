from utils import CanadianJurisdiction
from pupa.scrape import Organization


class Oshawa(CanadianJurisdiction):
    classification = 'legislature'
    division_id = 'ocd-division/country:ca/csd:3518013'
    division_name = 'Oshawa'
    name = 'Oshawa City Council'
    url = 'http://www.oshawa.ca'

    def get_organizations(self):
        organization = Organization(self.name, classification=self.classification)

        organization.add_post(role='Mayor', label=self.division_name, division_id=self.division_id)
        for seat_number in range(1, 8):
            organization.add_post(role='Regional Councillor', label='Oshawa (seat {})'.format(seat_number), division_id=self.division_id)
        for seat_number in range(1, 4):
            organization.add_post(role='Councillor', label='Oshawa (seat {})'.format(seat_number), division_id=self.division_id)

        yield organization
