def revc():
  data = open('input/rosalind_revc.txt', 'r').read().strip('\n')

  data = data.replace('G', 'c')
  data = data.replace('C', 'G')
  data = data.replace('T', 'a')
  data = data.replace('A', 'T')

  open('output/rosalind_revc_output.txt', 'w').write(data.upper()[::-1])

revc()
