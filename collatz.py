# Wayne Reilly 2018-02-11
# Collatz Conjecture https://en.wikipedia.org/wiki/Collatz_conjecture
# Inspiration from the web https://stackoverflow.com/questions/13366830/collatz-conjecture-sequence?rq=1
# I had a lot of troulble getting this out
# Issues included; Defining Odd & Even for a computer, getting stuck in a loop. 

x = 50 #set the number you want to check
print('input was: ' + str(x)) #verify input to user

seq = [x]#create a list to preserve your sequence
while x > 1: #iterate through the list until x is 1 or less than 1 
	if x % 2 == 0: #action on even
		x = x / 2
	else:
		x = 3 * x + 1 #action on uneven

	seq.append(x)  #add to list
	print(x) #priint new value of x

print(seq) #print the sequence 
