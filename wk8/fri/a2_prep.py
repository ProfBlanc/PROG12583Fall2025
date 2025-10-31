def get_people_avg_height(people):
    """
    Get's the average height of person

    >>> get_people_avg_height({'Ben': 110, 'John': 120, 'Mary': 130})
    >>> 120
    """
    final_value = ""

    final_value = sum(people.values()) / len(people.keys())

    return final_value
