def get_people_avg_height(people):
    """
    Get's the average height of people

    >>> get_people_avg_height({'Ben': 110, 'John': 120, 'Mary': 130})
    >>> 120
    """
    final_value = ""

    ################# Start of Code #################
    final_value = sum(people.values()) / len(people.keys())
    ################# End of Code  ##################
    return final_value

def get_min_people_height(people):
    """
    Get's the min height of people

    >>> get_min_people_height({'Ben': 110, 'John': 120, 'Mary': 130})
    >>> 110
    """
    final_value = ""

    ################# Start of Code #################
    final_value = min(people.values())
    ################# End of Code  ##################
    return final_value

def get_max_people_height(people):
    """
    Get's the max height of people

    >>> get_max_people_height({'Ben': 110, 'John': 120, 'Mary': 130})
    >>> 130
    """
    final_value = ""

    ################# Start of Code #################
    final_value = max(people.values())
    ################# End of Code  ##################
    return final_value

def get_tallest_person(people):
    """
    Get's the tallest person

    >>> get_tallest_person({'Ben': 110, 'John': 120, 'Mary': 130})
    >>> 'Mary'
    """
    final_value = ""

    ################# Start of Code #################
    tallest_value = max(people.values())
    for person, height in people:
        if height == tallest_value:
            final_value = person
            break
    ################# End of Code  ##################
    return final_value

def get_shortest_person(people):
    """
    Get's the shortest person

    >>> get_shortest_person({'Ben': 110, 'John': 120, 'Mary': 130})
    >>> 'Ben'
    """
    final_value = ""

    ################# Start of Code #################
    pass
    a = 100
    shortest_value = min(people.values())
    for person, height in people:
        if height == shortest_value:
            final_value = person
            break
    ################# End of Code  ##################
    return final_value
