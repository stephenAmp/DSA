"""
NON - PRIMITIVE DATA STRUCTURES
Lists
ordered,mutable,can duplicate, syntax = []
eg arr =['5','4','6']
Methods  map(int,arr) applies a given function(eg, int) to all elements of list
        read about list unpacking

tuple
ordered,can duplicate,not mutable syntax = ()
tuples can be used to interchange values of variables ie.
a= 5,b=1 
a,b = b,a => a=1,b=5

set
unordered,cant duplicate,mutatable syntax = {}

dictionary
ordered,cant duplicate,mutable syntax = {'key':'value'}
"""

# 5
# append 10
# append 20
# insert 1 15
# remove 10
# print

# SOLUTION
n = int(input())
list = []
for i in n:
    s,*d = input().split()
    d= list(map(int,d))
    if s=='print':
        print(list)
    else:
        getattr(list,s)*d


#given n as input

# SOLUTION
n = input()
user_input = map(int,n.split())
t = tuple(user_input)
print(hash(t))

"""
DICTIONARY - DATA STRUCTURE
Write function to output key,value pairs of a given dictionary
"""

dict1 = {'name':'Stephen','age':25,'Job':'Software Developer'}

def handle_dictionary(dict:dict) -> str:
    for key,value in dict.items():
        print(f'{key}:{value}')

handle_dictionary(dict1)

"""
HASH FUNCTION AND HASH SET
"""

def hash_function(word)->int:
    summation = sum([ord(ch) for ch in word])
    return summation % 10 #byte size should range  from 0 - 9

print(hash_function('World'))


hash_set = set()
hash_set.add(123)
hash_set.add(124)
hash_set.add(125)

#CONSTANT TIME COMPLEXITY O(1)
print(123 in hash_set)
print(124 in hash_set)
print(121 in hash_set)
print(hash_set)

#IMMUTABILITY
student_ids = set()
student_ids.add(1)
student_ids.add(2)
student_ids.add(3)
student_ids.add(3)
print(student_ids)

hashed_set = set(['ham','sugar','butter','milk'])
copied_set = hashed_set.copy()

print(copied_set)
copied_set.remove('ham')
print(copied_set)



#COMPARING DATA HANDLING IN HASH SETS TO LISTS

def hash_set_operation():
    hash_set = set()
    list_data = []

    elements  = 10**7 
    for i in range(elements):
        hash_set.add(i)
        list_data.append(i)

    #defining test element outside of range
    test_element = elements + 1

    import time
    start_time = time.time()
    print('hash set result is: ',test_element in hash_set)
    print('time taken in hash set: ',start_time - time.time())

    start_time = time.time()
    print('list data result is: ',test_element in list_data)
    print('time taken in list: ',start_time = time.time())
    return

hash_set_operation()


list_one = [1,2,3,4,5]
set1  = set()
for i in list_one:
    set1.add(i)
print(set1)


list_data_one = ['kofi','ama','kojo','kwame']
list_data_two = ['kwesi','ama','kojo','yaw']

def find_intersection(list_one,list_two):
    set_one = set(list_one)
    set_two = set(list_two)
    intersection = set_one & set_two
    intersection_list = list(intersection)
    return(sorted(intersection_list))

def find_unique_elements(list1,list2):
    set1 = {item.lower() for item in list1}
    set2 = {item.lower() for item in list2}

    unique_list1 = sorted(list(set1 - set2))
    unique_list2 = sorted(list(set2 - set1))
    return (unique_list1,unique_list2)


#filtering out repeating elements
def repeated_elements(list1):
    seen , repeated = set(),set()
    for item in list1:
        if item in seen:
            repeated.add(item)
        else:
            seen.add(item)
    return list(repeated)


# Problem 1: Unique String in the List
def find_unique_string(list1):
    seen, duplicate = set(), set()
    for item in list1:
        if item in seen:
            duplicate.add(item)
        seen.add(item)
    for item in list1:
        if item in duplicate:
            return duplicate
    return ""
        
#finding pairs of anagram from 2 different lists

list1 = ['team','halo','pea','silent']
list2 = ['mate','aloha','ape','listen']

def finding_anagram(list1,list2):
    anagram_dict1 = {}
    anagram_dict2 = {}
    for word in list1:
        sorted_word = ''.join(sorted(word))
        anagram_dict1[sorted_word] = word
    for word in list2:
        sorted_word = ''.join(sorted(word))
        anagram_dict2[sorted_word] = word
    anagram_pairs = []
    for key in anagram_dict1:
        if key in anagram_dict2:
            anagram_pairs.append((anagram_dict1[key],anagram_dict2[key]))
    return anagram_pairs
    

"""
HASH TABLES / HASH MAPS (dictionaries)
Collision can also be a situation where you have 2 different keys
pointing to the same index after being processed by a hash function
2 Methods to address collision:
- CHAINING
- OPEN ADDRESSING
"""
#DICTIONARIES

# Create a Python dictionary similar to a Hash Table
book_ratings = {"Moby-Dick": 8, "The Great Gatsby": 9, "War and Peace": 10, "The Catcher in the Rye": 8}

# Access a value with its key. This happens in O(1) time
print(book_ratings["Moby-Dick"])   # Outputs: 8
# Another way to access a value with its key is by providing the default value if the key is not there. Complexity is also O(1).
print(book_ratings.get("Moby-Dick", 0)) # Outputs: 8
print(book_ratings.get("Moby Dick", 0)) # Outputs: 0

# Add a new key-value pair. The addition operation is also O(1)
book_ratings["To Kill a Mockingbird"] = 9
book_ratings["The Great Gatsby"] = 8
print(book_ratings)
# Outputs: {"Moby-Dick": 8, "The Great Gatsby": 8, "War and Peace": 10, "The Catcher in the Rye": 8, "To Kill a Mockingbird": 9}

# Remove a key-value pair. Deletion is also a constant time operation
del book_ratings["War and Peace"]
print(book_ratings)
# Outputs: {"Moby-Dick": 8, "The Great Gatsby": 9, "The Catcher in the Rye": 8, "To Kill a Mockingbird": 9}

"""
PRACTICE
# Initialize an empty dictionary to serve as the hash table
# Add some books to the dictionary
# Print out the hash table/dictionary
# Now, let's attempt to add a new book with an ID that's already used
# Print out the updated dictionary
# Let's remove the book with ID 2 from the dictionary
# Print out the dictionary after deletion operation
# The time complexity of adding, accessing, and deleting operations in a Python dictionary is O(1)

NB: Dictionaries are mostly used to track frequencies and indexes
"""
book_library = {}

book_library[1] = "The Catcher in the Rye"
book_library[2] = "To Kill a Mockingbird"
book_library[3] = "1984"

print("Initial book library:")
for key, value in book_library.items():
    print(f"Book ID: {key}, Title: {value}")

book_library[1] = "Moby-Dick"

print("\nUpdated book library:")
for key, value in book_library.items():
    print(f"Book ID: {key}, Title: {value}")

del book_library[2]

print("\nBook library after deletion:")
for key, value in book_library.items():
    print(f"Book ID: {key}, Title: {value}")


#DICTIONARY APPLICATION

def frequent_word_finder(texts):
    from collections import defaultdict
    word_count = defaultdict(int)
    texts = texts.lower()
    text_list = texts.split()
    for word in text_list:
        word_count[word] += 1
    return sorted(word_count.items(), key = lambda x: x[1], reverse = True)[:3] #returning first 3

def password_strength_counter(password):
    password_strength = {
        'length':False,
        'lower_case':False,
        'upper_case':False,
        'digit':False
    }
    if len(password) >= 8:
        password_strength['length'] = True
    for char in password:
        if char.islower():
            password_strength['lower_case'] = True
        elif char.isupper():
            password_strength['upper_case'] = True
        elif char.isdigit():
            password_strength['digit'] = True
    return password_strength    
    

#employees is a list of dictionaries with employee data
def bonus_calculator(employees):
    bonus = 0
    for employee in employees:
        if employee['role'] == 'developer':
            bonus = 0.1 * employee['salary']
        employee['bonus'] = bonus
    return employees


def multi_password_strength_counter(passwords):
    special_characters = "!@#$%^&*()-+"
    # implement this
    result = []
    for password in passwords:
        password_strength = {
            'length': len(password) >= 8,
            'digit': any(char.isdigit() for char in password),
            'lowercase': any(char.islower() for char in password),
            'uppercase': any(char.isupper() for char in password),
            'special_char': any(char in special_characters for char in password)  
        }
        result.append(password_strength)
    return result
    pass

passwords = ["password", "Pa$$w0rd", "SuperSecurePwd!", "weakpw"]
results = multi_password_strength_counter(passwords)
for result in results:
    print(result)

"""
return a dictionary with keys as url and values as count of url of email. 
emails with domain not in the url list should be ignored

"""
email = ['foo@.com','bar@a.com','b@zab.com','qux@d.com']
urls = ['www.a.com','www.b.com','www.c.com']

def mail_details(list1,list2):
    from collections import defaultdict
    url_count = defaultdict(int)
    for mail in list1:
        seperating_email = mail.split('@')
        url_in_mail = seperating_email[1]
    for url in list2:
        if url_in_mail in url:
            url_count[url] += 1
    return url_count 

from collections import defaultdict

def mail_details(emails, urls):
    url_count = defaultdict(int)

    # Extract domains from URLs
    domain_set = {url.split("www.")[-1] for url in urls}  # Extract "a.com" from "www.a.com"

    for email in emails:
        if '@' in email:
            domain = email.split('@')[-1]  # Extract domain from email

            if domain in domain_set:  # Check if domain is in URL list
                url_count[f"www.{domain}"] += 1  # Store full URL in dictionary

    return dict(url_count)  # Convert defaultdict to normal dict

# Test cases
emails = ['foo@.com', 'bar@a.com', 'b@zab.com', 'qux@d.com']
urls = ['www.a.com', 'www.b.com', 'www.c.com']

result = mail_details(emails, urls)
print(result)  # Expected Output: {'www.a.com': 1}

lst = [12,45,67,8,9]
def return_second_highest(list1):
    sorted_list = sorted(list1, reverse=True)
    return sorted_list[1]

return_second_highest(lst)

#Reverse indexing / inverted eind
from typing import List
def keyword_index(documents: List) -> dict:
    dictionary = {}
    for doc_index, doc in enumerate(documents):
        for word in doc.split():
            if word not in dictionary:
                dictionary[word] = {}
            if doc_index not in dictionary[word]:
                dictionary[word][doc_index] = 0
            dictionary[word][doc_index] += 1
            
    return dictionary

#Frequency count DICTIONARY

def elect_board_member(votes):
    # implement this
    exclusive_board_members =  len(votes) // 3
    freq = {}
    exclusive_board_list = []
    
    for vote in votes:
        freq[vote] = freq.get(vote, 0) + 1
        
    for var, attr in freq.items():
        if attr >= exclusive_board_members:
            exclusive_board_list.append(var)
    if exclusive_board_list:
        import random
        return random.choice(exclusive_board_list)
    else:
        return -1
        
            


print(elect_board_member([1, 2, 3, 3, 3]))  # Expected output: 3
print(elect_board_member([1, 2, 3, 4, 5]))  # Expected output: -1
print(elect_board_member([1, 1, 1, 2, 2, 3, 3, 3]))  # Expected output: 1


"""
RECURSION
Three Foundational Problems to note:
- Fibonacci Sequence - Implement memoization(store previously calculated fib numbers. to prevent redundnacy time complexity = 0(N^2))
- Finding sum of all numbers in array
- Calculating Factorials

Recursion works if there is a sequence and a base case to break it
"""

#Fibonacci Sequence (time complexity = O(N))
def fib(n, computed = {0:0, 1:1}):
    if n not in computed:
        computed[n] = fib(n-1, computed) + fib(n-2, computed)
    return computed[n]

#Adding elements in array With Recursion
def sum_array(arr, index=0):
    if arr[index] == len(arr):
        return 0
    return arr[index] + sum_array(arr,index + 1)

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)


def factorial(num):
    #  Implement this function according to the task description
    if num == 1 or num == 0:
        return 1
    elif num < 0:
        return 'Error'
    return num * factorial(num - 1)
    pass


def factorials(nums):
    results = []
    for num in nums:
        f = factorial(num)
        if f is not None:
            results.append(f)
        else:
            results.append('Error')
    return results


print(factorials([2, 3, 4]))  # Should print: [2, 6, 24]
print(factorials([1, 5, 6]))  # Should print: [1, 120, 720]
print(factorials([0, -3, 10]))  # Should print: [1, 'Error', 3628800]