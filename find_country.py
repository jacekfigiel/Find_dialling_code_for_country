country_filename = "country_details.txt"

countries = {}
"""converting txt file into python dictionary"""
with open(country_filename) as country_file:
    country_file.readline()
    for row in country_file:
        data = row.strip("\n").split("|")
        country, capital, code, code3, dialling, timezone, currency = data
        country_dict = {
            "country": country,
            "capital": capital,
            "country_code": code,
            "cc3": code3,
            "dialling_code": dialling,
            "timezone": timezone,
            "currency": currency
        }
        countries[country.casefold()] = country_dict #input filter can be country name or dialling_code
        countries[dialling.casefold()] = country_dict

"""Infinite loop to go thru data stops when input is quite"""
while True:
    input_country = input("Please enter name of the country or dialling code: \n").casefold()
    if input_country in countries:
        country_data = countries[input_country] # input as a slice to find a country in dictionary
        for detail, value in country_data.items():
            print(detail, ":", value)
    elif input_country not in countries or dialling:
        print("Wrong input try again")
    if input_country == "quite":
        break

