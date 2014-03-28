def iprb():
  data = open('input/rosalind_iprb.txt', 'r').read()

  [k, m, n] = map(float, data.split(' '))
  total = k + m + n

  # Probability if both homozygous dominant
  prob = (k / total) * ((k - 1) / total) + \
         (k / total) * (m / total) + \
         (k / total) * (n / total) + \
         (m / total) * ((m - 1) / total) * 0.75 + \
         (m / total) * (n / total) * 0.5

  print prob



iprb()
