def ini2():
  data = open('input/rosalind_ini2.txt', 'r').read()
  [a, b] = map(int, data.split(' '))
  result = a * a + b * b
  open('output/rosalind_ini2_output.txt', 'w').write(str(result))

ini2()
