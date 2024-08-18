#### write a program to find the most occurence of a character in a string.######

def count_char(word):
    count = 0
    for i in word:
        count += 1
    return count

word = 'python java'

print(count_char(word))
