def dna():
  data = open('input/rosalind_dna.txt', 'r').read()

  open('output/rosalind_dna_output.txt', 'w').write(" ".join(map(str, map(lambda b: data.count(b), ['A', 'C', 'G', 'T']))))

dna()
