import vehicle

def main():
    car = vehicle.Car('BMW', 2001, 70000, 15000.0, 4)
    truck = vehicle.Truck('Toyota', 2002, 40000, 12000.0, '4WD')
    suv = vehicle.SUV('Volvo', 2000, 30000, 18500.0, 5)
    
    
    # Display the car's data
    print(f'Make: {car.get_make()}')
    print(f'Model: {car.get_mileage()}')
    print(f'price: {car.get_price()}')
    print(f'Number of doors: {car.get_doors()}')
    print()
    
    # Display the truck's data
    print(f'Make: {truck.get_make()}')
    print(f'Model: {truck.get_mileage()}')
    print(f'price: {truck.get_price()}')
    # print('Drive type:', truck.get_drive_type())
    print()
    
    # Display the truck's data
    print(f'Make: {suv.get_make()}')
    print(f'Model: {suv.get_mileage()}')
    print(f'price: {suv.get_price()}')
    # print('Passenger Capacity:', suv.get_pass_cap())
    
    
    

if __name__ == '__main__':
    main()