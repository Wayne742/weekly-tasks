def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Reilly"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)

###
Week 1 Post.
Re: Fibonacci exercise responses
by WAYNE REILLY - Thursday, 25 January 2018, 9:43 PM
My name is Wayne, so the first and last letters of my name are (W+E = 23+5) 28. The 28th number in a Fibonacci Sequence is 317,811.
###
###
Week 2 Post.
Re: Week 2 task
by WAYNE REILLY - Sunday, 4 February 2018, 9:24 PM 
Hi Ian, All,
Here's my response to this weeks homework,
Wayne-Reillys-MacBook-Pro:Python_beg waynereilly$ python Test2.py
My surname is Reilly
The first letter R is number 82
The last letter y is number 121
Fibonacci number 203 is 1188518561323126046432205871807859915657177
Ord( ) - The ord( ) method returns an integer representing Unicode code point for the given Unicode character. Apparently ord( ) is the inverse of chr( ) "Who knew?!?".
Wayne.
###
