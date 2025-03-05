sh = [
    [
        "plain-white",
        'white-dots',
        "white-checks",
    ],
    [
        'jeans',
        'light-jeans',
    ],
    [
        "white-checks",
        "blue-checks",
        'maroon-checks',
    ],
    [
        'jeans',
        "plain-white",
        'grey',
        'green'
    ]
]

pt = [
    ['white'],
    ['black'],
    ['jeans', 'light-jeans'],
    ['maroon'],
    ['green']
]

mh = [['white-checks', 'jeans'],
      ['white-checks', 'light-jeans'],
      ['white-checks', 'black'],
      ['green', 'jeans'],
      ['green', 'light-jeans'],
      ['green', 'black'],
      ['green', 'white'],
      ['blue-checks', 'black'],
      ['blue-checks', 'white'],
      ['jeans', 'black'],
      ['jeans', 'white'],
      ['white-dots', 'jeans'],
      ['white-dots', 'maroon'],
      ['white-dots', 'light-jeans'],
      ['white-dots', 'black'],
      ['light-jeans', 'black'],
      ['light-jeans', 'white'],
      ['maroon-checks', 'black'],
      ['grey', 'black'],
      ['plain-white', 'green'],
      ['plain-white', 'jeans'],
      ['plain-white', 'maroon'],
      ['plain-white', 'light-jeans'],
      ['plain-white', 'black']]
# mh = mh[:14]


def gen_mch(seq):
  cmh = seq[-1]
  rs = []
  for (ish, ipt) in mh:
    if (ish, ipt) in seq:
      continue
    fl = True
    for shg in sh:
      if cmh[0] in shg and ish in shg:
        fl = False
        break
    if fl:
      for ptg in pt:
        if cmh[1] in ptg and ipt in ptg:
          fl = False
          break
    if fl:
      rs.append([ish, ipt])
  return rs


def gen_score(seq):
  n = len(seq)
  score = 0
  for i in range(n):
    srt = i+1
    slf = i-1
    while 1:
      if seq[i][0] == seq[srt % n][0]:
        break
      srt += 1
    while 1:
      if seq[i][0] == seq[slf][0]:
        break
      slf -= 1
    prt = i+1
    plf = i-1
    while 1:
      if seq[i][1] == seq[prt % n][1]:
        break
      prt += 1
    while 1:
      if seq[i][1] == seq[plf][1]:
        break
      plf -= 1
    rt = min(srt, prt)
    lf = max(slf, plf)
    score += min(rt-i, i-lf)
  return score


res = {
    'score': 0,
    'seq': []
}
c = 0


def u(seq):
  if len(seq) == len(mh):
    global c
    c += 1
    print(c, end='\r')
    s = gen_score(seq)
    if s > res['score']:
      res['score'] = s
      res['seq'] = [seq]
    elif s == res['score']:
      res['seq'].append(seq)
    return
  for s in gen_mch(seq):
      u(seq + [s])


u([mh[0]])

print(res)
