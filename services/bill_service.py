from utilities.base_service import BaseService
from utilities.data_utils import load_data, save_data
from models.bill import Bill

class BillService(BaseService):
    def list_all(self):
        # todo: implement this method
        """list all bills"""
        bills = load_data('bills.txt')
        return [Bill(**bill_data) for bill_data in bills]

        pass

    def add(self):
        # todo: implement this method
        """add bill"""
        bills = load_data('bills.txt')
        bills.append(Bill.to_dict())
        save_data('bills.txt', bills)
        pass

    def remove(self, bill_id):
        # todo: implement this method
        """remove bill by id"""
        bills = load_data('bills.txt')
        bills = [bill for bill in bills if bill['id'] != bill_id]
        save_data('bills.txt', bills)
        pass

    def update(self, bill_id, updated_info):
        # todo: implement this method
        """update bill is_paid only"""
        bills = load_data('bills.txt')
        for bill in bills:
            if bill['id'] == bill_id:
                bill.update(updated_info)
                break
        save_data('bills.txt', bills)
        pass
