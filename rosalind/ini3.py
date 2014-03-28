def ini3():
  data = open('input/rosalind_ini3.txt', 'r').read()
  [string, delimiters] = data.splitlines()
  [a, b, c, d] = map(int, delimiters.split(' '))

  open('output/rosalind_ini3_output.txt', 'w').write(string[a:b + 1] + ' ' + string[c:d + 1])


ini3()
