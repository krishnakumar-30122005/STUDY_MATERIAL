from datetime import date

# =====================================
# 1. Guest (Encapsulation)
# =====================================

class Guest:
    def __init__(self, guest_id, name, email, phone):
        self.__guest_id = guest_id
        self.name = name
        self.email = email
        self.phone = phone


    def get_id(self):
        return self.__guest_id


# =====================================
# 2. Room Hierarchy (Inheritance + Polymorphism)
# =====================================

class Room:
    def __init__(self, room_id):
        self.room_id = room_id
        self.is_available = True

    def get_type(self):
        raise NotImplementedError

    def get_price(self):
        raise NotImplementedError

    def book(self):
        self.is_available = False

    def release(self):
        self.is_available = True


class SingleRoom(Room):
    def get_type(self):
        return "Single"

    def get_price(self):
        return 1000


class DoubleRoom(Room):
    def get_type(self):
        return "Double"

    def get_price(self):
        return 1500


# =====================================
# 3. Booking (Composition)
# =====================================

class Booking:
    counter = 1

    def __init__(self, guest, room, check_in, check_out):
        self.booking_id = Booking.counter
        Booking.counter += 1

        self.guest = guest
        self.room = room
        self.check_in_date = check_in
        self.check_out_date = check_out
        self.status = "Active"

        # Mark room as occupied
        self.room.book()

    def get_days(self):
        days = (self.check_out_date - self.check_in_date).days
        return max(1, days)

    def complete(self):
        self.status = "Completed"
        self.room.release()


# =====================================
# 4. Payment (Abstraction)
# =====================================

class Payment:
    def __init__(self, booking):
        self.booking = booking
        self.amount = 0
        self.status = "Pending"

    def process(self):
        days = self.booking.get_days()
        price = self.booking.room.get_price()
        self.amount = days * price
        self.status = "Paid"


# =====================================
# 5. Hotel Manager (Controller)
# =====================================

class HotelManager:
    def __init__(self):
        self.guests = []
        self.rooms = []
        self.bookings = []
        self.payments = []

    # Register guest
    def register_guest(self, name, email, phone):
        guest_id = len(self.guests) + 1
        guest = Guest(guest_id, name, email, phone)
        self.guests.append(guest)
        print(f"Guest Registered: {guest_id}")
        return guest

    # Add room
    def add_room(self, room):
        self.rooms.append(room)

    # Simple availability check
    def find_available_room(self, room_type):
        for room in self.rooms:
            if room.get_type() == room_type and room.is_available:
                return room
        return None

    # Create booking
    def create_booking(self, guest, room_type, check_in, check_out):
        room = self.find_available_room(room_type)

        if not room:
            print("No room available")
            return None

        booking = Booking(guest, room, check_in, check_out)
        self.bookings.append(booking)

        print(f"\nBooking Created")
        print(f"Booking ID: {booking.booking_id}")
        print(f"Room: {room.room_id} ({room_type})")

        return booking

    # Checkout
    def checkout(self, booking):
        payment = Payment(booking)
        payment.process()

        booking.complete()
        self.payments.append(payment)

        print("\nCheckout Successful")
        print(f"Guest: {booking.guest.name}")
        print(f"Amount Paid: ₹{payment.amount}")


# =====================================
# Example Usage
# =====================================


if __name__ == "__main__":
    hotel = HotelManager()

    # Add rooms
    hotel.add_room(SingleRoom(101))
    hotel.add_room(SingleRoom(102))
    hotel.add_room(DoubleRoom(201))

    # Register guest
    guest = hotel.register_guest("Krishna", "krishna@gmail.com", "9876543210")

    # Booking
    check_in = date(2026, 2, 17)
    check_out = date(2026, 2, 20)

    booking = hotel.create_booking(guest, "Single", check_in, check_out)

    # Checkout
    if booking:
        hotel.checkout(booking)
