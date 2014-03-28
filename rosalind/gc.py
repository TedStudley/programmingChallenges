def gc():
  data = open('input/rosalind_gc.txt', 'r').read().replace('\n', '')

  max_gc = 0

  data = data + '>'
  data = data.lstrip('>')
  while data:
    id = data[0:13]
    dna = data[13:data.index('>')]

    gc = float(dna.count('C') + dna.count('G')) / len(dna) * 100
    if gc > max_gc:
      max_id = id
      max_gc = gc

    data = data[data.index('>'):]
    data = data.lstrip('>')

  print max_id
  print max_gc

  o = open('output/rosalind_gc_output.txt', 'w')
  o.write(str(max_id) + '\n')
  o.write(str(max_gc) + '\n')

gc()
