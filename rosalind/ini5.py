def ini5():
  data = open('input/rosalind_ini5.txt', 'r').read().splitlines()
  odd = False
  for line in data:
    odd = not odd
    if odd:
      data.remove(line)
  result = "\n".join(data)
  open('output/rosalind_ini5_output.txt', 'w').write(result)

ini5()
