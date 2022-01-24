country_filename = "country_details.txt"

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
        print(row)
