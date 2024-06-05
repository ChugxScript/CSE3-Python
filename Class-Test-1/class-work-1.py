def sort_dict():
    print("\n[1] Write a Python script to sort (ascending and descending) a dictionary by value.")
    my_dict = {
        'a': 3,
        'b': 1,
        'c': 2,
        'd': 5,
        'e': 4
    }

    print("Original dict:")
    print(my_dict)

    # Sorting the dictionary by value in ascending order
    sorted_dict_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
    print("Dictionary sorted by value in ascending order:")
    print(sorted_dict_asc)

    # Sorting the dictionary by value in descending order
    sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
    print("Dictionary sorted by value in descending order:")
    print(sorted_dict_desc)

def add_key_to_dict():
    print("\n[2] Write a Python script to add a key to a dictionary.")
    my_dict = {
        0: 10,
        1: 20,
    }
    # Original dict
    print("Original dict:")
    print(my_dict)
    
    # Adding a new key-value pair
    my_dict[3] = 30

    # Print the updated dictionary
    print("Updated dictionary:")
    print(my_dict)

def concatenate_dict():
    print("\n[3] Write a Python script to concatenate following dictionaries to create a new one.")
    dic1 = {1:10, 2:20}
    dic2 = {3:30, 4:40}
    dic3 = {5:50, 6:60}

    print("Original dicts:")
    print(f"dict1: {dic1}")
    print(f"dict2: {dic2}")
    print(f"dict3: {dic3}")

    concatenated_dict = dic1.copy()
    concatenated_dict.update(dic2)
    concatenated_dict.update(dic3) 

    print("\nConcatinated dict:")
    print(concatenated_dict)

def check_dict_key():
    print("\n[4] Write a Python script to check if a given key already exists in a dictionary.")
    my_dict = {'a': 1, 'b': 2, 'c': 3}

    # Key to check
    key_to_check_a = 'b'
    key_to_check_b = 'd'

    # Check if 'key_to_check_a' exists
    if key_to_check_a in my_dict:
        print(f"The key '{key_to_check_a}' exists in the dictionary.")
    else:
        print(f"The key '{key_to_check_a}' does not exist in the dictionary.")
    
    # Check if 'key_to_check_b' exists
    if key_to_check_b in my_dict:
        print(f"The key '{key_to_check_b}' exists in the dictionary.")
    else:
        print(f"The key '{key_to_check_b}' does not exist in the dictionary.")

def iterate_over_dicts():
    my_dict = {'a': 1, 'b': 2, 'c': 3}

    # Iterate over keys
    print("Iterating over keys:")
    for key in my_dict:
        print(key)

    # Iterate over keys and values
    print("\nIterating over keys and values:")
    for key, value in my_dict.items():
        print(f"Key: {key}, Value: {value}")

def generate_dict_by_given_n():
    print("\n[6] Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).")
    given_n = int(input("Enter n: "))
    sample_dict = {}
    print("Original dict:")
    print(sample_dict)

    for n in range(1, given_n + 1):
        sample_dict[n] = n*n
    
    print("Updated dict:")
    print(sample_dict)

def generate_dict_1_to_15():
    print("\n[7] Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.")
    sample_dict = {}
    print("Original dict:")
    print(sample_dict)

    for n in range(1, 16):
        sample_dict[n] = n*n
    
    print("Updated dict:")
    print(sample_dict)

def merge_python_dict():
    print("\n[8] Write a Python script to merge two Python dictionaries.")
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}

    print("Original dicts:")
    print(f"dict1: {dict1}")
    print(f"dict2: {dict2}")

    # Merge dict2 into dict1
    dict1.update(dict2)

    print("Merged dictionary using dictionary update:")
    print(dict1)

def sum_dict_items():
    print("\n[10] Write a Python program to sum all the items in a dictionary.")
    my_dict = {'a': 10, 'b': 20, 'c': 30}

    # Initialize sum
    total_sum = 0

    # Sum all the values
    for value in my_dict.values():
        total_sum += value

    print("Sum of all items in the dictionary:", total_sum)


if __name__ == "__main__":
    while True:
        print("\n\n-- MENU --")
        print("[1] Write a Python script to sort (ascending and descending) a dictionary by value.")
        print("[2] Write a Python script to add a key to a dictionary.")
        print("[3] Write a Python script to concatenate following dictionaries to create a new one.")
        print("[4] Write a Python script to check if a given key already exists in a dictionary.")
        print("[5] Write a Python program to iterate over dictionaries using for loops.")
        print("[6] Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).")
        print("[7] Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.")
        print("[8] Write a Python script to merge two Python dictionaries.")
        print("[9] Write a Python program to iterate over dictionaries using for loops.")
        print("[10] Write a Python program to sum all the items in a dictionary.")
        user_choice = input("\n>>>")

        if user_choice == '1':
            sort_dict()
            input("Press Enter to continue")
        elif user_choice == '2':
            add_key_to_dict()
            input("Press Enter to continue")
        elif user_choice == '3':
            concatenate_dict()
            input("Press Enter to continue")
        elif user_choice == '4':
            check_dict_key()
            input("Press Enter to continue")
        elif user_choice == '5':
            print("\n[5] Write a Python program to iterate over dictionaries using for loops.")
            iterate_over_dicts()
            input("Press Enter to continue")
        elif user_choice == '6':
            generate_dict_by_given_n()
            input("Press Enter to continue")
        elif user_choice == '7':
            generate_dict_1_to_15()
            input("Press Enter to continue")
        elif user_choice == '8':
            merge_python_dict()
            input("Press Enter to continue")
        elif user_choice == '9':
            print("\n[9] Write a Python program to iterate over dictionaries using for loops.")
            iterate_over_dicts()
            input("Press Enter to continue")
        elif user_choice == '10':
            sum_dict_items()
            input("Press Enter to continue")
        else:
            print("\n[ERROR] inputs 1-10 only.")
            input("Press Enter to continue")