class InvoiceManager:
    def __init__(self):
        self__invoices = []

    def add_invoice(self, invoice: Invoice):
        self__invoices.append(invoice)

    def remove_invoice_number(self, invoice_number):
        self__invoices = [inv for inv in self._invoices if inv.invoice_number != invoice_number]


    def get_all_invoices(self):
        return self.__invoices

    def find_by_number(self, invoice_number):
        for inv in self__invoices:
            if inv.invoice_number == invoice_number:
                return inv
        return None


    def find_by_date(self,date):
        return [inv for inv in self__invoices if inv.date == date]

    def print_all_invoices(self):
        for inv in slef._invoices
            print(f"Rechnungsnummer: {inv.invoice_number}, Rechnungsatum: {inv.invoice_date}")