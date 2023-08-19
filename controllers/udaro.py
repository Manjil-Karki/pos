from models.udaro import UdaroModel


class UdaroController:

    def __init__(self):
        self.model = UdaroModel()

    def add_update_udaro(self, records):
        not_used = [1, 3,4]
        records = [elem for i, elem in enumerate(records) if i not in not_used]
        result = self.model.check_name(records[1])
        if result is None:
            self.model.add_to_udaro(records)
        else:
            records = records[1:]
            result = list(result)[1:-1]
            records[1] = records[1] + result[1]
            records[2] = records[2] + result[2]
            records[3] = records[3] + result[3]
            records[4] = records[4] + result[4]
            print(records, result)
            self.model.update_by_name(records)
