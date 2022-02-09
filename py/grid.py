
p = 'PLAYMODE'
wp = len(p)

w = 20
h = 10

grid = ''

for j in range(h):
    for i in range(w):
        n = (i+j) % wp
        grid += p[n]
    grid += '\n'

print(grid)

