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
        customer_numbers = []

        next_page = None

        try:
            while True:
                response = api.get(next_page)

                validate_response_status(response)
                _json = json.loads(response.content.decode('utf-8'))

                pagination = _json['pagination']
                customers = _json['collection']

                for customer in customers:
                    customer_numbers.append(str(customer['customerNumber']))

                try:
                    next_page = pagination['nextPage']
                except KeyError:
                    break

            listener.on_success(data={
                'customer_numbers': customer_numbers.__str__()
            })
        except DoesNotExistException:
            listener.on_does_not_exist()
            return
        except UnknownErrorException as e:
            listener.on_unknown_error(e.status_code, e.content)
            return


def validate_response_status(response):
    if response.status_code == 200:
        return
    if response.status_code == 404:
        raise DoesNotExistException()

    raise UnknownErrorException(response.status_code, response.content)


class DoesNotExistException(RuntimeError):
    pass


class UnknownErrorException(RuntimeError):

    def __init__(self, status_code, content, *args: object) -> None:
        self.status_code = status_code
        self.content = content
        super().__init__(*args)

