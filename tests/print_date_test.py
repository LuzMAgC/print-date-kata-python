import unittest
from unittest.mock import Mock

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

    def test_print_current_date_using_doubles_created_with_library(self):
        calendar = Mock()
        calendar.today.return_value = datetime_dummy
        printer = Mock()
        print_date = PrintDate(calendar, printer)

        print_date.print_current_date()

        printer.print_line.assert_called_once_with(datetime_dummy)

