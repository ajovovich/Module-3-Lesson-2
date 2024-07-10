#Task 1: Formatting Flight Itineraries

def flight_itinerary(itineraries):
    index = 0
    for itinerary in itineraries:
        traveler, origin, destination = itinerary
        index += 1
        print(f"Itinerary {index}: {traveler} is leaving {origin} and landing in {destination} ")


plans = (("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco"))

flight_itinerary(plans)