Class Invoice_manager:
   def __init__(self, invoice_number, invoice_date):
        self.__invoice_number = invoice_number
        self.__invoice_date = invoice_date


    @property
    def invoice_number(self):
        return self.__invoice_number

    @property
    def invoice_date(self):
        return self.__invoice_date 