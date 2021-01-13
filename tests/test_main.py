import sys, os

sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))
from modeling.models.region import Region


from modeling.models.tariff import Tariff

def test_main():
    country = Region.query.first()
    assert country.id == 2


