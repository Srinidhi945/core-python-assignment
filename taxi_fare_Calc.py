def calc_fare(distance):
    base_fare = 50
    distance_fare = distance * 10
    return base_fare + distance_fare

def total_fare(trips):
    fares = [calc_fare(dist) for dist in trips]
    trip_num = 1  
    for fare in fares:
        print(f"Trip {trip_num}: ${fare}")
        trip_num += 1
    print(f"Total Fare: ${sum(fares)}")

trips = [5, 10, 3]
total_fare(trips)

