class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("My restaurant name is " + self.restaurant_name.title())
        print("Type of cusine available in my restaurant is " +
              self.cuisine_type.title())

    def open_restaurant(self):
        print("Restaurant is open")

    def set_number_served(self, num_serv):
        self.number_served = num_serv

    def read_number_served(self):
        print("No of customer served by my restaurant=" + str(self.number_served))

    def increment_number_served(self, customer):
        self.number_served += customer


# restaurant_1 = Restaurant("Ron's Bake House", 'Chinese')
# restaurant_2 = Restaurant("Thambal Hotel", 'Indian')
# restaurant_3 = Restaurant("Elle's", 'Italian')
# restaurant_1.describe_restaurant()
# restaurant_2.describe_restaurant()
# restaurant_3.describe_restaurant()


restaurant = Restaurant("ron's bake house", 'chinese')
restaurant.set_number_served(30)
restaurant.read_number_served()
restaurant.increment_number_served(10)
restaurant.read_number_served()
