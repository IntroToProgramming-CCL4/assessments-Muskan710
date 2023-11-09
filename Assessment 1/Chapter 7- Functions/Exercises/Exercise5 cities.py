# We will use def to describe city and  its country.
def describe_City(city, country= "Default Country"):
    print(f"{city} is in {country}.")
#calling the function for three different cities
describe_City("Rome","Italy")
describe_City("Tokyo","Japan")
describe_City("London")