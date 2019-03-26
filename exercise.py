#Create a Location class with a name.

#Create a Trip class with a list of Location instances (called stops or destinations or something similar). Define a method that lets you add locations to the trip's list of destinations.

#Make several instances of Locations and add them to an instance of Trip.

#Define a method in the Trip class that iterates through the list of locations and prints something similar to the following:

class Location:
    def __init__(self,names):
        self.name = name

        
        class Trip(Location):
            def __init__(self, stops):
                self.stops = stops

            def locations(self):
                names = 'Toronto','New York', 'Halifax','My Basement ;)','Brampton'


            def add_locations_to_list(self):
                destinations = []
                destinations.append(names)

            def going_on_trip(self):
                for place in destinations:
                    print(f"T")