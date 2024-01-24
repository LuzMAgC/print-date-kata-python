import unittest

from print_date import PrintDate
from tests.calendar_stub import CalendarStub
from tests.datetime_dummy import datetime_dummy
from tests.printer_fake import PrinterFake


class PrintDateTest(unittest.TestCase):

    def test_print_current_date_using_doubles_created_by_me(self):
        print_date = PrintDate(CalendarStub(), PrinterFake())

        print_date.print_current_date()

        self.assertEqual(print_date.printer.line, datetime_dummy)
