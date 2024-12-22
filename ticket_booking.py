def book(total, booked, seat):
    if seat in booked:
        print(f"Seat {seat} is already booked.")
    else:
        booked.append(seat)
        print(f"Seat {seat} has been successfully booked.")

def cancel(booked, seat):
    if seat in booked:
        booked.remove(seat)
        print(f"Seat {seat} has been successfully canceled.")
    else:
        print(f"Seat {seat} was not booked.")

def available(total, booked):
    return [seat for seat in range(1, total + 1) if seat not in booked]

total = 10
booked = [2, 5, 7]
book(total, booked, 3)
cancel(booked, 5)
available_seats = available(total, booked)
print("Available seats:", available_seats)
