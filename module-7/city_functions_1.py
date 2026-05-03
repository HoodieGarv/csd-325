# 5/4/2026
# Module 7 Assignment - CSD-325
# Garvin Stewart

def city_country(city, country, population=None, language=None):
    """
    Return a formatted string for a city and country.
    
    Parameters:
        city (str):         Name of the city.
        country (str):      Name of the country.
        population (int):   Optional population figure.
        language (str):     Optional primary language spoken.

    Returns:
        str: Formatted string, e.g. 'Santiago, Chile - population 5000000, Spanish'
    """
    result = f"{city}, {country}"
    if population:
        result += f" - population {population}"
    if language:
        result += f", {language}"
    return result


# Three calls demonstrating each argument tier
print(city_country("Santiago", "Chile"))                              # city + country only
print(city_country("Paris", "France", population=2161000))            # with population
print(city_country("Tokyo", "Japan", population=13960000, language="Japanese"))  # fully specified
