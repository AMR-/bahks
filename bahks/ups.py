"""
Sends packages with UPSConnection
https://pypi.python.org/pypi/ClassicUPS
"""

from ClassicUPS.ups import UPSConnection
import credentials
from binascii import a2b_base64
import StringIO

from PIL import Image


ups = UPSConnection(license_number=credentials.ups_access_key, 
    user_id='bahksme', password=credentials.ups_password, 
    shipper_number=credentials.ups_account_number)



# returns a shipment object
# service options are: '1dayair','2dayair','ground',worldwide_expedited'


# helper method for set_up_shipment
def create_shipment(from_addr, to_addr, dimensions, weight, shipping_service):
    shipment = ups.create_shipment(from_addr, to_addr, dimensions, weight, 
                                   shipping_service, file_format='GIF')
    return shipment

# returns a shipment object
# service options are: '1dayair','2dayair','ground',worldwide_expedited'

def set_up_shipment(from_name, from_street_address, from_city, 
    from_state, from_country, from_zip, from_phone, to_name, 
    to_street_address, to_city, to_state, to_country, 
    to_zip, to_phone, length, width, height, weight, service='ground'):
    from_addr = {
        'name': from_name,
        'address1': from_street_address,
        'city': from_city,
        'state': from_state,
        'country': from_country,
        'postal_code': from_zip,
        'phone': from_phone
    }
    to_addr = {
        'name': to_name,
        'address1': to_street_address,
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
    shipment = create_shipment(from_addr, to_addr, dimensions, weight, service)
    return shipment

# helper method for set_up_shipment
def create_shipment(from_addr, to_addr, dimensions, weight, shipping_service):
    shipment = ups.create_shipment(from_addr, to_addr, dimensions, weight, 
        file_format='GIF')
    return shipment

# creates a shipping label gif (saves it in root?)
def save_label(shipment):
    return shipment.save_label(open('/tmp/label.gif', 'wb'))

def get_image_object(shipment):
    raw_epl = shipment.accept_result.dict_response['ShipmentAcceptResponse']['ShipmentResults']['PackageResults']['LabelImage']['GraphicImage']
    binary = a2b_base64(raw_epl)
    s.write(binary)
    image = Image.fromstring("RGBA",(100,50),s.getvalue())
    return image

def get_cost(shipment):
    return shipment.cost()

def get_tracking_number(shipment):
    return shipment.tracking_number()
