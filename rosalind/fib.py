def fib():
  data = open('input/rosalind_fib.txt', 'r').read()

  [n, k] = map(int, data.split(' '))

  f0 = 0
  f1 = 1
  for i in range(1, n):
    f2 = f1 + k * f0
    f0 = f1
    f1 = f2

  result = f1

  open('output/rosalind_fib_output.txt', 'w').write(str(result))
fib()
