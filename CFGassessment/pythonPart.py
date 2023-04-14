#Section 2
#2.1


def isogram(word):

    word = word.lower()
    repeated_chars = set(word)
    if len(repeated_chars) == len(word):
        return True
    else:
        return False

print(isogram("uncopyrightable"))




"""
    Python Challenge
    
    You are tasked with calculating the minimum classes we need to have so we know how many people to employ. 
    Write a function which when 
    given a number of students, calculates and prints out a string for your proposed number of classes, and a dictionary showing the allocation. 
    
    Key Constraints:
   - The maximum size of a class is 30
   - There needs to be a minimum of 2 classes
   - The distribution of each class should be as even as possible. 
  -  We want to hire as little people as possible - so where possible focus on bigger classes, and less of them!
"""

def calc_mininum_classes(num):

        if num <= 30:
            num = 1
        else:
            num_classes = (num+ 29) // 30


        allocation = {}
        for i in range(num_classes):
            if i < num % num_classes:
                class_size = num// num_classes + 1
            else:
                class_size = num // num_classes
            allocation[f"Class {i + 1}"] = class_size


        print(f"Proposed Allocation: {num_classes} classes")

        return allocation


print(calc_mininum_classes(87))




