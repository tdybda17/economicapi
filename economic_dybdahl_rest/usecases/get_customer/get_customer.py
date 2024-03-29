import json
import requests

from economic_dybdahl_rest.api.get_contacts import GetContactsApi
from economic_dybdahl_rest.api.get_customer import GetCustomerApi
from economic_dybdahl_rest.dto.customer import Customer
from economic_dybdahl_rest.dto.delivery_location import DeliveryLocation


class GetCustomerUseCase:

    @staticmethod
    def get(customer_number, listener):
        api = GetCustomerApi()
        response = api.get(customer_number)
        if response.status_code == 200:
            _json = json.loads(response.content.decode('utf-8'))
            customer = Customer.from_response(_json)

            customer.contacts = GetCustomerUseCase._crawl_contact_pages(customer_number, [], skip_pages=0)

            delivery_locations_url = _json['deliveryLocations']
            response = requests.get(
                url=delivery_locations_url,
                headers=api.headers
            )
            _json = json.loads(response.content.decode('utf-8'))
            collection = _json.get('collection', [])
            delivery_locations = []
            for d in collection:
                delivery_locations.append(DeliveryLocation.from_dict(d))

            customer.delivery_locations = delivery_locations
            listener.on_success(data=customer.to_dict())
        elif response.status_code == 404:
            listener.on_does_not_exist()
        else:
            listener.on_unknown_error(response.status_code, response.content)

    @staticmethod
    def _crawl_contact_pages(customer_number, contacts, skip_pages=0):
        contact_response = GetContactsApi().get(
            customer_number=customer_number,
            skip_pages=skip_pages
        ).json()

        contacts.extend(contact_response['collection'])
        if 'nextPage' in contact_response['pagination']:
            return GetCustomerUseCase._crawl_contact_pages(
                customer_number=customer_number,
                contacts=contacts,
                skip_pages=skip_pages + 1,
            )
        return contacts
