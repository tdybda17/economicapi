from economic_dybdahl_rest.dto._model import Model



class Journal(Model):

     def __init__(self, name, journal_number):
         self.name = name
         self.journal_number = journal_number
         super().__init__()

     def to_dict(self):
        return {
            'name': self.name,
            'journal_number': self.journal_number
        }


     @staticmethod
     def from_dict(_dict):
         return Journal(
             name=_dict['name'],
             journal_number=_dict['journalNumber']
         )
