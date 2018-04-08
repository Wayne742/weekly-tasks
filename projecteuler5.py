#Wayne Reilly 7/04/2018
#Project Euler Number 5
#I tried several times to devise a solution, my best attempt is below. I used ### to show a separation from the script I want to run
#used this link for ideas https://stackoverflow.com/questions/19886324/dividing-integer-by-all-numbers-in-a-range-in-python
#stackoverflow.com code take from answer provide by user:steveha 
#https://stackoverflow.com/questions/8024911/project-euler-5-in-python-how-can-i-optimize-my-solution

###
x = 2520
for i in range(1, 21):
  x = x / i
  if x % 2 == 0:
    print(x)
else:
    x = (x + 20)
###
    
check_list = [11, 13, 14, 16, 17, 18, 19, 20]

def find_solution(step):
    for num in range(step, 999999999, step):
        if all(num % n == 0 for n in check_list):
            return num
    return None

if __name__ == '__main__':
    solution = find_solution(20)
    if solution is None:
        print("No answer found")
    else:
        print("found an answer:", solution)
