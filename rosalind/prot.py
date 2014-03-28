def prot():
  data = open('input/rosalind_prot.txt', 'r').read().strip('\n')
  codon = {"UUU" :  "F", "UUC" :  "F", "UUA" :  "L", "UUG" :  "L", \
           "UCU" :  "S", "UCC" :  "S", "UCA" :  "S", "UCG" :  "S", \
           "UAU" :  "Y", "UAC" :  "Y", "UAA" : "\n", "UAG" : "\n", \
           "UGU" :  "C", "UGC" :  "C", "UGA" : "\n", "UGG" :  "W", \
           "CUU" :  "L", "CUC" :  "L", "CUA" :  "L", "CUG" :  "L", \
           "CCU" :  "P", "CCC" :  "P", "CCA" :  "P", "CCG" :  "P", \
           "CAU" :  "H", "CAC" :  "H", "CAA" :  "Q", "CAG" :  "Q", \
           "CGU" :  "R", "CGC" :  "R", "CGA" :  "R", "CGG" :  "R", \
           "AUU" :  "I", "AUC" :  "I", "AUA" :  "I", "AUG" :  "M", \
           "ACU" :  "T", "ACC" :  "T", "ACA" :  "T", "ACG" :  "T", \
           "AAU" :  "N", "AAC" :  "N", "AAA" :  "K", "AAG" :  "K", \
           "AGU" :  "S", "AGC" :  "S", "AGA" :  "R", "AGG" :  "R", \
           "GUU" :  "V", "GUC" :  "V", "GUA" :  "V", "GUG" :  "V", \
           "GCU" :  "A", "GCC" :  "A", "GCA" :  "A", "GCG" :  "A", \
           "GAU" :  "D", "GAC" :  "D", "GAA" :  "E", "GAG" :  "E", \
           "GGU" :  "G", "GGC" :  "G", "GGA" :  "G", "GGG" :  "G"}

  bases = []
  while data:
    bases.append(data[0:3])
    data = data[3:]

  protein = ''
  for base in bases:
    protein = protein + codon[base]

  open('output/rosalind_prot_output.txt', 'w').write(protein)

prot()
