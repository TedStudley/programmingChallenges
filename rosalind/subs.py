def subs():
  data = open('input/rosalind_subs.txt', 'r').read()

  [s, t] = data.splitlines()

  locations = []
  index = s.find(t)
  while index != -1:
    locations.append(index + 1)
    index = s.find(t, index + 1)

  open('output/rosalind_subs_output.txt', 'w').write(' '.join(map(str, locations)))

subs()
