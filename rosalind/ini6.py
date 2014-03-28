def ini6():
  data = open('input/rosalind_ini6.txt', 'r').read().strip('\n')

  count = {}
  for s in data.split(' '):
    count[s] = count.get(s, 0) + 1

  open('output/rosalind_ini6_output.txt', 'w').writelines(map(lambda w: w + " " + str(count[w]) + "\n", count))

ini6()
