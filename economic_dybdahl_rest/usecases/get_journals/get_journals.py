import json

from economic_dybdahl_rest.api.get_journals import GetJournalsAPI
from economic_dybdahl_rest.dto.journal import Journal


class GetJournalsUseCase:

    @staticmethod
    def get(listener):
        journals_api = GetJournalsAPI()

        next_page = None
        all_journals = []

        while True:

            if next_page is None:
             response = journals_api.get()
            else:
                response = journals_api.get_next_page(next_page)

            if not response.ok:
                if response.status_code == 404:
                    listener.on_does_not_exist()
                    return
                listener.on_unknown_error(response.status_code, response.content)
                return

            _json = json.loads(response.content.decode('utf-8'))

            pagination = _json['pagination']
            journals = _json['collection']

            for journal in journals:
                journal_model = Journal.from_dict(journal)
                all_journals.append(journal_model.to_dict())

            try:
                next_page = pagination['nextPage']
            except KeyError:
                break

        listener.on_success(data=all_journals)
        return
