def add(num1, num2):
    if isinstance(num1, (int,float)) and isinstance(num2, (float, int)):
        return num1 + num2

def average(list_of_numbers):
    if isinstance(list_of_numbers, list):
        
        for value in list_of_numbers:
            if not isinstance(value, (int, float)):
                return
        
        return sum(list_of_numbers) / len(list_of_numbers)


def mode(values):
    tracker = dict()
    end = list()

    for value in values:
        if value not in tracker:
            tracker[value] = 1
        else:
            tracker[value] += 1
    max_occurences = max(tracker.values())
    for key, value in tracker.items():
        if value == max_occurences:
            end.append(key)

    #return end[0] if len(end) == 1 else end
    if len(end) == 1:
        return end[0]
    return end