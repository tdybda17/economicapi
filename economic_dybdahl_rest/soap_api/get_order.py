from economic_dybdahl_rest.soap_api._soap_api import EconomicSOAPApi


class GetOrderSOAPAPI(EconomicSOAPApi):

    def __init__(self) -> None:
        super().__init__()

    def get_order(self, id):
        response = self.client.service.Order_GetData(entityHandle={
            'Id': id
        })
        return response

    def get_orders(self, order_handles):
        response = self.client.service.Order_GetDataArray(entityHandles={
            'OrderHandle': order_handles
        })
        return response
