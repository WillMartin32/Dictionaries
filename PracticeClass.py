class Practice:
    def __init__(self,num,use,size,price):
        self.__roomnum = num
        self.__roomuse = use
        self.__roomsize = size
        self.__roomprice = price

    def set_room_number(self,num):
        self.__roomnum = num

    def set_room_number(self,use):
        self.__roomuse = use

    def set_room_number(self,size):
        self.__roomsize = size

    def price_per_sqft(self,size,price):
        p_sqft = size/price
        return p_sqft

    def get_room_number(self):
        return self.__roomnum

    def get_room_use(self):
        return self.__roomuse

    def get_room_size(self):
        return self.__roomsize