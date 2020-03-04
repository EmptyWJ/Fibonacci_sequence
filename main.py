def Fibonacci(n):
  a, b = 0, 1
  for i in range(n + 1):
    a, b = b, a + b
  return a

if __name__ == '__main__':
	for i in range(200):
  		print("Fibonacci("+ str(i) +") = "+ str(Fibonacci(i)) +"\n")