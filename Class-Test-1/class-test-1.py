def what_is_dict():
    dict_def = '''
        What is dictionary? give example
            A dictionary is like a list, but instead of using numbers to find items, you use unique keys. 
            Keys can be any data type, often strings because they're easy to remember. 
            Dictionaries store key-value pairs and are great for quickly finding values using their keys. 
            Unlike lists, dictionaries don't keep their items in any specific order.
    '''
    print(dict_def)

    my_dictionary = {
        'first_name': 'ANDREW',
        'last_name': 'OLOROSO',
        'section': 'BSCS-3B',
        'subject': 'CS Elective 3',
        'professor': 'Prof. Mhona Liza Paragas',
    }
    print(f"\nmy_dictionary: {my_dictionary}")
    print(f"my_dictionary first_name: {my_dictionary['first_name']}")

def create_dict_traverse():
    print("\n[2] Write a python script to traverse a dictionary")

    my_dictionary = {
        'first_name': 'ANDREW',
        'last_name': 'OLOROSO',
        'section': 'BSCS-3B',
        'subject': 'CS Elective 3',
        'professor': 'Prof. Mhona Liza Paragas',
    }
    print("\nFirst method:")
    print(f"First dictionary: {my_dictionary}")

    # creating it manually or one by one
    my_dictionary_b = dict()
    my_dictionary_b['first_name'] = 'test first name'
    my_dictionary_b['last_name'] = 'test last name'
    my_dictionary_b['section'] = 'test section'
    my_dictionary_b['subject'] = 'test subject'
    my_dictionary_b['professor'] = 'test professor'
    print("\nSecond method (manually/one-by-one):")
    print(f"Second dictionary: {my_dictionary_b}")

def built_in_methods():
    print("\n[3] Explain 5 list built in methods of dictionary")
    method_1 = '''
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    >>> Method 1:
        dict.items(): Returns a view object that displays a list of dictionary's key-value tuple pairs.
        Example:
            my_dict = {'a': 1, 'b': 2, 'c': 3}
            print(my_dict.items())  
            Expected Output: dict_items([('a', 1), ('b', 2), ('c', 3)])
    '''
    print(method_1, "\nCode Result:")
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print(">>", my_dict.items())

    method_2 = '''
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    >>> Method 2:
        dict.keys(): Returns a view object that displays a list of all the keys in the dictionary.
        Example:
            my_dict = {'a': 1, 'b': 2, 'c': 3}
            print(my_dict.keys())  
            Expected Output: dict_keys(['a', 'b', 'c'])
    '''
    print(method_2, "\nCode Result:")
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print(">>", my_dict.keys())

    method_3 = '''
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    >>> Method 3:
        dict.values(): Returns a view object that displays a list of all the values in the dictionary.
        Example:
            my_dict = {'a': 1, 'b': 2, 'c': 3}
            print(my_dict.values())  
            Expected Output: dict_values([1, 2, 3])
    '''
    print(method_3, "\nCode Result:")
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print(">>", my_dict.values())

    method_4 = '''
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    >>> Method 4:
        dict.get(key, default=None): Returns the value for the specified key if key is in the dictionary. 
                                        If the key is not found, it returns the default value.
        Example:
            my_dict = {'a': 1, 'b': 2, 'c': 3}
            print(my_dict.get('a'))
            Expected Output: 1

            print(my_dict.get('d', 'Not Found'))
            Expected Output: Not Found
    '''
    print(method_4, "\nCode Result:")
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print(">>", my_dict.get('a'))
    print(">>", my_dict.get('d', 'Not Found'))

    method_5 = '''
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    >>> Method 5:
        dict.pop(key, default=None): Removes the specified key and returns the corresponding value. If the key is not found, it returns the default value.
        Example:
            my_dict = {'a': 1, 'b': 2, 'c': 3}
            print(my_dict.pop('a'))
            Expected Output: 1

            print(my_dict)
            Expected Output: {'b': 2, 'c': 3}

            print(my_dict.pop('d', 'Not Found'))
            Expected Output: Not Found
    '''
    print(method_5, "\nCode Result:")
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print(">>", my_dict.pop('a'))
    print(">>", my_dict)
    print(">>", my_dict.pop('d', 'Not Found'))

def key_value_pair():
    print("\n[4] What is key value pair? Explain")
    key_value_pair_def = '''
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    A key is a unique identifier used to retrieve the associated value. 
    Keys must be immutable, meaning they cannot be changed. 
    Common examples of keys include strings, numbers, and tuples.

    A value is the data associated with a key. 
    Values can be of any data type, such as strings, numbers, lists, or even other dictionaries.

    In simple words, a key-value pair is a way to store data where each piece of data (value) is associated with a unique identifier (key). You use the key to get the value.

    Example:
        my_dictionary = {
            'first_name': 'ANDREW',
            'last_name': 'OLOROSO',
            'section': 'BSCS-3B',
            'subject': 'CS Elective 3',
            'professor': 'Prof. Mhona Liza Paragas',
        }

        We want to look for the 'first_name'
        We use keys like 'first_name' to find the values like 'ANDREW'
    '''
    print(key_value_pair_def)

    my_dictionary = {
        'first_name': 'ANDREW',
        'last_name': 'OLOROSO',
        'section': 'BSCS-3B',
        'subject': 'CS Elective 3',
        'professor': 'Prof. Mhona Liza Paragas',
    }
    print(f"\nCode Result: {my_dictionary['first_name']}")

if __name__ == "__main__":
    while True:
        print("\n\n-- MENU --")
        print("[1] What is Dictionary?")
        print("[2] Write a python script to traverse a dictionary")
        print("[3] Explain 5 list built in methods of dictionary")
        print("[4] What is key value pair? Explain")
        user_choice = input("\n>>>")

        if user_choice == '1':
            what_is_dict()
            input("Press Enter to continue")
        elif user_choice == '2':
            create_dict_traverse()
            input("Press Enter to continue")
        elif user_choice == '3':
            built_in_methods()
            input("Press Enter to continue")
        elif user_choice == '4':
            key_value_pair()
            input("Press Enter to continue")
        else:
            print("\n[ERROR] inputs 1-4 only.")
            input("Press Enter to continue")
    