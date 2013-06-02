"""
Sends packages with UPSConnection
https://pypi.python.org/pypi/ClassicUPS
"""

from ClassicUPS.ups import UPSConnection

ups = UPSConnection(license_number=credentials.ups_access_key, 
    user_id='bahksme', password=credentials.ups_password, 
    shipper_number=credentials.ups_account_number)


# returns three dictionaries: from_addr, to_addr, dimensions
def set_up_shipment(from_name, from_street_address, from_city, 
    from_state, from_country, from_zip, from_phone, to_name, 
    to_street_address, to_city, to_state, to_country, 
    to_zip, to_phone, length, width, height):
    from_addr = {
        'name': from_name,
        'address1': from_addr,
        'city': from_city,
        'state': from_state,
        'country': from_country,
        'postal_code': from_zip,
        'phone': from_phone
    }
    to_addr = {
        'name': to_name,
        'address1': to_addr,
        'city': to_city,
        'state': to_state,
        'country': to_country,
        'postal_code': to_zip,
        'phone': to_phone
    }
    dimensions = {  # in inches
        'length': length,
        'width': width,
        'height': height
    }
    return from_addr, to_addr, dimensions

# use this to create a shipment object
def create_shipment(from_addr, to_addr, dimensions, weight):
    shipment = ups.create_shipment(from_addr, to_addr, dimensions, weight, file_format='GIF')
    return shipment

# creates a shipping label gif (saves it in root?)
def save_label(shipment):
    shipment.save_label(open('label.gif', 'wb'))