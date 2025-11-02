
from operator import itemgetter

def sort_list_of_dicts(data_list, key, descending=False):
    """
    Sorts a list of dictionaries by a specific key.

    Args:
        data_list (list): The list of dictionaries to sort.
        key (str): The dictionary key to sort by.
        descending (bool): Set to True for descending order. 
                           Defaults to False (ascending).

    Returns:
        list: A new list containing the sorted dictionaries.
    """
    return sorted(data_list, key=itemgetter(key), reverse=descending)

# The if __name__ == "__main__": block ensures this code only runs when the script is executed directly.
if __name__ == "__main__":
    # Creating the list of dictionaries.
    # Note: It's best practice to avoid using 'list' as a variable name because it's a built-in Python type.
    people = [
        {'name': 'Anab', 'age': 21, 'county': 'Garissa'},
        {'name': 'Mary', 'age': 30, 'county': 'Nakuru'},
        {'name': 'Zeinab', 'age': 27, 'county': 'Moyale'}
    ]

    print("Original list:")
    print(people)

    # Sorting in ascending order by 'age' using the function
    sorted_asc = sort_list_of_dicts(people, 'age')
    print("\nSorted by 'age' (ascending):")
    print(sorted_asc)

    # Sorting in descending order by 'age' using the function
    sorted_desc = sort_list_of_dicts(people, 'age', descending=True)
    print("\nSorted by 'age' (descending):")
    print(sorted_desc)