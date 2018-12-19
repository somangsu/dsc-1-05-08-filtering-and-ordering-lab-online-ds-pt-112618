def select_all_female_dogs_name_and_breed():
    return "select name, breed from dogs where gender='F';"

def select_all_dogs_names_in_alphabetical_order():
    return "select name from dogs Order by name;"

def select_nameless_dog():
    return "select * from dogs where name is null;"

def select_hungry_dogs_name_and_breed_ordered_by_youngest_to_oldest():
    return "select name, breed from dogs where hungry = 1  order by age;"


def select_name_age_and_temperament_of_oldest_dog():
    return "select name, age, temperament from dogs order by age desc limit 1;"

def select_name_and_age_of_three_youngest_dogs():
    return "select name, age from dogs order by age  limit 3;"

def select_name_and_breed_of_dogs_between_age_five_and_ten_ordered_by_oldest_to_youngest():
    return "select name, breed from dogs where age between 5 and 10 order by age desc;"

def select_name_age_and_hungry_of_hungry_dogs_between_age_two_and_seven_in_alphabetical_order():
    return "select name, age, hungry from dogs where age between 2 and 7 and hungry = 1 order by name;"
    #return "SELECT name, age, hungry FROM dogs WHERE hungry = 1 AND age BETWEEN 2 AND 7 ORDER BY name;"
