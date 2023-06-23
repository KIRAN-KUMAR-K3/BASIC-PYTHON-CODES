#3.B) Write a python program to find the string similarity between two given stirngs 
#simple output: original string: python exercises, similarity between two said strigs:1.0

import difflib 
def string_similarity(str1,str2):
    result = difflib. SequenceMatcher(a=str l.lower(), b=str2.lower())
    return result.ratio()
    strl= "Python Excercises"
    str2= "Python Exercises"
    print("Original string:")
    print(str1)
    print(str2)