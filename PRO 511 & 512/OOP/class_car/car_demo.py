import vehicle

def main():
    used_car = vehicle.Car('Audi', 2007, 12500, 21500.0, 4)
    
    print(f'Make: {used_car.get_make()}')
    print(f'Model: {used_car.get_model()}')
    print(f'Mileage: {used_car.get_mileage()}')
    print(f'price: {used_car.get_price()}')
    print(f'Number of doors: {used_car.get_doors()}')
    
    
if __name__ == '__main__':
    main()