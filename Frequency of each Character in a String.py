##### WAP to find the Frequency of each Character in a String.###################

def most_common_char(word):
    dict = {}
    for i in word:
        if i in dict.keys():
            dict[i] = dict[i] +1
        else:
            dict[i] = 1
    return dict

word = "kaulaammmopuuuuurrr"
print(most_common_char(word))
