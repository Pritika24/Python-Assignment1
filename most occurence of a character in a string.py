##### Write a program to find the most occurence of a character in a string.######

def most_common_char(word):
    dict = {}
    for i in word:
        if i in dict.keys():
            dict[i] = dict[i] +1
        else:
            dict[i] = 1
    max = 0
    max_key = ""
    for key, value in dict.items():
        if value > max:
            max = value
            max_key = key
    return max_key


word = "kaulaammmopuuuuurrr"
print(most_common_char(word=word))
