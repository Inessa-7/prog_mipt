from task7 import Vector

N = int(input())
dots = []
max_dist = -1
m_d = None

for i in range(N):
    dots.append(Vector(input()))

for i in dots:
    d = abs(i)
    if d > max_dist:
        max_dist = d
        m_d = i

print('({},{},{})'.format(m_d.x, m_d.y, m_d.z))
