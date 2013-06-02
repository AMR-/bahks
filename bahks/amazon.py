from python-amazon-mws.mws.mws import create_inbound_shipment_plan
from python-amazon-mws.mws.mws import MWS
from python-amazon-mws.mws.mws import InboundShipments
import credentials

InboundShipmentPlanRequestItem = { 'SellerSKU': '56789','Quantity': 1, 'ASIN': 'B0EXAMPLEG' }
access_key = credentials.aws_access_key
secret_key = credentials.aws_secret_key
account_id = credentials.amzn_merchant_id


inbound_shipments = InboundShipments( MWS(access_key, secret_key, account_id) )

def __prep_shipment_to_warehouse(address):
	return inbound_shipments.create_inbound_shipment_plan(address.name, address.addressLine1, 
	address.addressLine2, address.city, address.state, address.postalCode,
	InboundShipmentPlanRequestItem['SellerSKU'], 
	InboundShipmentPlanRequestItem['ASIN'])

def shipment_to_warehouse(address): # ShipmentID, InboundShipmentHeader, InboundShipmentItems
	shipment_plan = __prep_shipment_to_warehouse(address)
	