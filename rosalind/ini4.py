def ini4():
  data = open('input/rosalind_ini4.txt', 'r').read()

  [a, b] = map(int, data.split(' '))

  sum = 0
  for number in range(a, b + 1):
    if number % 2 == 1:
      sum += number

  open('output/rosalind_ini4_output.txt', 'w').write(str(sum))

ini4()
