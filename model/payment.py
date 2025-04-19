Class Payment_manager:
    def __init__(self, payment_method, payment_amount):
        self.__payment_method = []
        self.__payment_amount = payment_amount
       

    @property
    def payment_amount(self):
        return self.__payment_amount