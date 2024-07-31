def show_info(city, country, population=''):
    if population:
        return city.title()+','+country.title()+' - population '+str(population)
    return city.title()+','+country.title()
