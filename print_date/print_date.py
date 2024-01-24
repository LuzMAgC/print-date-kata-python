class PrintDate:

    def __init__(self, calendar, printer):
        self.__printer = printer
        self.__calendar = calendar

    def print_current_date(self):
        self.__printer.print_line(self.__calendar.today())
