
rivers={'Nile':'Egypt','Amazon':'Brazil','Yangtze':'China'}
# we will use loop to print statement about each river.
for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

#we will use loop to print the name of each river.
print("\nrivers:")
for river in rivers:
    print(river.capitalize())

#we will now use loop to print the name of each country.
print("\ncountries:")
for country in rivers.values():
    print(country.capitalize())

