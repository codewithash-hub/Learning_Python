import vehicle

class Truck(vehicle.Automobile):
    def __init__(self, make, model, mileage, price, drive_type):
        vehicle.Automobile.__init__(self, make, model, mileage, price)
        self.__drive_type = drive_type
        
        def set_drive_type(self, drive_type):
            self.__drive = drive_type
            
        def get_drive_type(self):
            return self.__drive_type