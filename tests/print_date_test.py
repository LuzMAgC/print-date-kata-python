import unittest

from print_date import PrintDate
from tests.calendar_stub import CalendarStub
from tests.datetime_dummy import datetime_dummy
from tests.printer_fake import PrinterFake


class PrintDateTest(unittest.TestCase):

    def test_print_current_date_using_doubles_created_by_me(self):
        printer = PrinterFake()
        print_date = PrintDate(CalendarStub(), printer)

        print_date.print_current_date()

        self.assertEqual(printer.line, datetime_dummy)
