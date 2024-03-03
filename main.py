import pandas

df = pandas.read_csv("hotels.csv")


class Hotel:
    def __init__(self, hotel_id):
        self.customer_name = None
        self.customer_name = self.customer_name
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == hotel_id, "name"].squeeze()

    def book(self):
        bookable = df.loc[df["id"] == hotel_id, "available"].squeeze() == "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        availability = df.loc[df["id"] == hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):

        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f""""
        Thank you for your reservation!
        Here are your booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        """
        return content

print(df)
hotel_id = int(input("Enter the ID of the hotel: "))
hotel = Hotel(hotel_id)

if hotel.available():
    hotel.book()
    name = input("enter your name: ")
    reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not free.")
