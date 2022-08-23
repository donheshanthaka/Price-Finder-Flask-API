from app import utils

def test_get_price():
    """
    GIVEN a name of a vehicle
    WHEN trying to find the current market price
    THEN check the returned value is a string 
    (cannot check for an exact value since market value is not constant, 
    therefore checking the return type is the only option available)
    """
    price = utils.get_price("Toyota Aqua 2014")
    assert type(price) == str