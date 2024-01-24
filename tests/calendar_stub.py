from tests.datetime_dummy import datetime_dummy


class CalendarStub:
    def today(self):
        return datetime_dummy
