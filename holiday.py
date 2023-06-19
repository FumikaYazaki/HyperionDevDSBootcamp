def hotel_cost(num_night):
    #hotel cost is 100 per day
    return 100 * num_night

def plane_cost(city_flight):
    if city_flight == "Rome".lower():
        return 80 
    elif city_flight == "Madrid".lower():
        return 100
    elif city_flight == "Paris".lower():
        return 50
    else:
        input(print("Invalid distination name. Please choose the city name again from Rome, Madrid or Paris."))

def car_rental(rental_days):
    #car rental cost is 100 per day
    return 100 * rental_days

def holiday_cost(hotel, flight, car):
    accomdation_cost = hotel_cost(hotel)
    flight_cost = plane_cost(flight)
    rental_car_cost = car_rental(car)
    return accomdation_cost + flight_cost + rental_car_cost

city_flight = input("Please choose the city you will be fliying to from Rome, Madrid, or Paris).")
num_night = int(input("Please enter the number of nights you will be staying at a hotel."))
rental_days =int(input("Please enter the number of days you will be hiring a car for."))

flight_cost = plane_cost(city_flight)
accomodation_cost = hotel_cost(num_night)
rental_car_cost = car_rental(rental_days)
total_cost = holiday_cost(num_night,city_flight,rental_days)

print(f"Flight cost to", city_flight, ":", flight_cost)
print(f"Total hotel cost for", num_night,"nights:", accomodation_cost)
print(f"Total car rental cost for", rental_days,"days:", rental_car_cost)
print(f"Total holiday cost:", total_cost)
