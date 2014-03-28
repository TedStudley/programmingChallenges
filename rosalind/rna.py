def rna():
  data = open('imput/rosalind_rna.txt', 'r').read()

  open('output/rosalind_rna_output.txt', 'w').write(data.replace('T', 'U'))

rna()
