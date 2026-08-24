def solution(my_string):
    for vowel in "aeiou":
        my_string = my_string.replace(vowel, "")
    return my_string