from __future__ import unicode_literals
from utils import CanadianJurisdiction
from pupa.scrape import Organization


class Milton(CanadianJurisdiction):
    classification = 'legislature'
    division_id = 'ocd-division/country:ca/csd:3524009'
    division_name = 'Milton'
    name = 'Milton Town Council'
    url = 'http://www.milton.ca'

    def get_organizations(self):
        organization = Organization(self.name, classification=self.classification)

        organization.add_post(role='Mayor', label=self.division_name, division_id=self.division_id)
        organization.add_post(role='Regional Councillor', label='Wards 1, 6, 7 and 8')
        organization.add_post(role='Regional Councillor', label='Wards 2, 3, 4 and 5')
        for ward_number in range(1, 9):
            organization.add_post(role='Councillor', label='Ward {}'.format(ward_number))

        yield organization
