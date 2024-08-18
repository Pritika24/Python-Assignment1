###### Write a program to check if the string is palindrome..#############

def palindrome(s):
  reverse=''
  for char in s:
    reverse=char+ reverse
  if (s==reverse):
    return "word is a palindrome"
  else:
    return "word is not a palindrome"
s='madam'
print(palindrome(s))
