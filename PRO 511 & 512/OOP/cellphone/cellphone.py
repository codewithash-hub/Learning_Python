class Cellphone:
    def __init__(self, manufact, model, price) -> None:
        self.__manufact = manufact
        self.__model = model
        self.__retail_price = price

    def set_manu(self, manu):
        self.__manufact = manu

    def set_model(self, model):
        self.__model = model

    def set_price(self, price):
        self.__retail_price = price


    def get_manu(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__retail_price 
