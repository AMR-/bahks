from mws.mws import MWS
from mws.mws import InboundShipments
import credentials

InboundShipmentPlanRequestItem = { 'SellerSKU': '56789','Quantity': 1, 'ASIN': 'B0EXAMPLEG' }
print InboundShipmentPlanRequestItem['ASIN']
access_key = credentials.aws_access_key_id
secret_key = credentials.aws_secret_key
account_id = credentials.amzn_merchant_id


inbound_shipments = InboundShipments(access_key, secret_key, account_id)


def __prep_shipment_to_warehouse(**address):
    return inbound_shipments.create_inbound_shipment_plan('SELLER_LABEL',
        address['name'], address['addressLine1'], 
        address['city'], address['state'], address['postalCode'], address['countryCode'],
        InboundShipmentPlanRequestItem['SellerSKU'], 
        InboundShipmentPlanRequestItem['ASIN']).parsed
"""
__prep_shipment_to_warehouse returns this beast...
{
'InboundShipmentPlans':
    {
    'member': 
        {
        'ShipToAddress': 
            {
            'StateOrProvinceCode': {'value': 'VA'}, 
            'City': {'value': 'CHESTER'}, 
            'Name': {'value': 'Amazon.com.kydc LLC'}, 
            'CountryCode': {'value': 'US'}, 
            'value': '\n          ', 
            'AddressLine1': {'value': '1901 MEADOWVILLE TECHNOLOGY PKWY'}, 
            'PostalCode': {'value': '23836'} 
            }, 
        'Items': 
            {
            'member': 
                {
                'FulfillmentNetworkSKU': {'value': 'X000GIOBYN'}, 
                'SellerSKU': {'value': '56789'}, 
                'value': '\n            ', 
                'Quantity': {'value': '0'}
                }, 
            'value': '\n          '
            }, 
        'LabelPrepType': {'value': 'SELLER_LABEL'}, 
        'value': '\n        ', 
        'ShipmentId': {'value': 'FBA13HJFTX'}, 
        'DestinationFulfillmentCenterId': {'value': 'RIC2'}
        }, 
        'value': '\n      '
    }, 
    'value': '\n    '
}
"""



def shipment_to_warehouse(**address): # ShipmentID, InboundShipmentHeader, InboundShipmentItems
    shipment_plan = __prep_shipment_to_warehouse(**address)
    member = shipment_plan['InboundShipmentPlans']['member']
    shipmentId = member['ShipmentId']
    shipmentId = shipmentId['value']
    destinationId = member['DestinationFulfillmentCenterId']
    labelType = member['LabelPrepType']
    labelType =  labelType['value']

    #InboundShipmentHeader
    name = member['ShipToAddress']['Name']
    name =  name['value']
    addressLine1 = member['ShipToAddress']['AddressLine1']
    addressLine1 = addressLine1['value']
    #addressLine2 = member['ShipToAddress']['AddressLine2']
    #print addressLine2
    city = member['ShipToAddress']['City']
    city = city['value']
    state = member['ShipToAddress']['StateOrProvinceCode']
    state = state['value']
    zipCode = member['ShipToAddress']['PostalCode']
    zipCode = zipCode['value']
    country = member['ShipToAddress']['CountryCode']
    country = country['value']

    sellerSKU = member['Items']['member']['SellerSKU'] #not sure how it handles multiple items
    sellerSKU = sellerSKU['value']
    quantity = member['Items']['member']['Quantity']
    quantity = quantity['value']

    #fulfillmentSKU = member['Items']['member']['FulfillmentNetworkSKU']
    ship_id = inbound_shipments.create_inbound_shipment(shipmentId, 
            name, addressLine1, city, state, zipCode, country,
            destinationId, labelType, sellerSKU, quantity).parsed
    print ship_id


"""
re ShipmentStatus...
is used with the CreateInboundShipment operation:
* WORKING - The shipment was created by the seller, but has not yet shipped.
* SHIPPED - The shipment was picked up by the carrier.
The following is an additional valid
ShipmentStatus value when InboundShipmentHeader
is used with the UpdateInboundShipment
operation:
* CANCELLED - The shipment was
cancelled by the seller after the
shipment was sent to the Amazon
fulfillment center.

"""
