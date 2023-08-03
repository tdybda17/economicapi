from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
import json
import base64

from economic_dybdahl_rest.api.get_attachments import Attachment, HasAttachment
from economic_dybdahl_rest.api.post_vouchers import Vouchers
from economic_dybdahl_rest.usecases.get_customer.get_customer import GetCustomerUseCase
from economic_dybdahl_rest.usecases.get_customer.get_customer_listener import GetCustomerListener


class AttachmentEndpoint(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, journal_id, accounting_year, attachment_id):

        attc_response = Attachment().get(journal_id, accounting_year, attachment_id)

        return JsonResponse(data={'attachment': base64.b64encode(attc_response.content).decode('utf-8')},
                            status=attc_response.status_code)
