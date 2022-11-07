def max_num(a, b, c):
    if a > b and a > c:
        print(a)
    elif b > c and b > a:
        print(b)
    elif c > a and c > b:
        print(c)

def mult_list(num):
    product = 1
    for i in num:
        product = product * i
    print(product)

def rev_string(string):
    print(string[::-1])

def num_within(x, y, z):
    if x in range(y, z):
        print("You're in range")
    else :
        print("Not in range")


triangle = [[1],[1,1]]
def pascal(n):
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      length = len(row_prev)+1
      for i in range(length):
        if i == 0:
          row.append(1)
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    for row in triangle:
      print(row)


max_num(1, 3, 5)

num_list = [2, 3, 4, 5]

mult_list(num_list)

my_string = "Hey Guys"

rev_string(my_string)

num_within(4, 1, 6)
num_within(5, 1, 4)

pascal(4)