# Day 3 Assignment-Implement a decorator mod_div() which assures that the numerator is always greater than the denominator

def mod_div(fun):
  def inner(a, b):
    if a < b:
      a, b = b, a
    fun(a, b)   

  return inner

@mod_div
def div(a, b):
  print(a / b)

div(2, 4)