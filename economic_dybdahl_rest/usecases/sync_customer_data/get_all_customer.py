import json
import requests

from economic_dybdahl_rest.api.get_all_customers import GetAllCustomersApi
from economic_dybdahl_rest.api.get_contacts import GetContactsApi
from economic_dybdahl_rest.api.get_customer import GetCustomerApi
from economic_dybdahl_rest.dto.customer import Customer
from economic_dybdahl_rest.dto.delivery_location import DeliveryLocation


class GetAllCustomerUseCase:

    @staticmethod
    def get(listener):
        api = GetAllCustomersApi()
        response = api.get()

        if response.status_code == 200:
            _json = json.loads(response.content.decode('utf-8'))

            data = _json['collection']

            customer_numbers = []
            for number in data:
                customer_numbers.append(number['customerNumber'])

            listener.on_success(data={
                'customer_numbers': customer_numbers.__str__()
            })
        elif response.status_code == 404:
            listener.on_does_not_exist()
        else:
            listener.on_unknown_error(response.status_code, response.content)
