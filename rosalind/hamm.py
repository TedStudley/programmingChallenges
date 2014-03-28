def hamm():
  data = open('input/rosalind_hamm.txt', 'r').read()
  [s, t] = data.splitlines()

  count = 0
  for pair in zip(s, t):
    if pair[0] != pair[1]:
      count = count + 1

  open('output/rosalind_hamm_output.txt', 'w').write(str(count))
hamm()
