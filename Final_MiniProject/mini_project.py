# Mini Project: WAP to generate everytime a 6 character OTP and print it.

import random
import string

id = ''
characters_list = list ( string.digits + string.ascii_letters )
for i in range ( 6 ):
  id += random.choice ( characters_list )

print( id )