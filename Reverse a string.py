#####WAP to reverse a string without using [::-1].#######


def reverse_str(s):
  reversed_str=""
  for i in s:
   reversed_str= i + reversed_str
  return reversed_str 

s='python'
print(reverse_str(s))
