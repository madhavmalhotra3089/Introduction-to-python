string='Madhav'
result = True
str_len = len(string)
print str_len
half_len= int(str_len/2)
print half_len
    
for i in range(0, half_len):
  # you need to check only half of the string
    print string[str_len-i-1]
    if string[i] != string[str_len-i-1]:
        result = False
        break
print(result) 