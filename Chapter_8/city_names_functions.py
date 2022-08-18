# 8-16 asked to copy over a function and import it using different methods. The execution of that exercise 
# can be found in imports_8-16.ipynb

def city_country(city, country):
    """Creates the city/country pair in string format"""
    formatted_string = f"{city.title()}, {country.title()}"
    return formatted_string