from datetime import datetime


class DateTools:
    @staticmethod
    def get_date():
        d1 = datetime.now()
        return d1.strftime("%H:%M:%S %d-%m-%Y")
