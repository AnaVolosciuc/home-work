duration = int(input('write some duration: '))

d = duration / 86400
h = (duration - (86400 * d)) / 3600
m = (duration - (86400 * d) - (3600 * h)) / 60
s = (duration - (86400 * d) - (3600 * h) - (60 * m))

result = ''

if d > 0:
    result = result + str(d) + ' day '
if h > 0:
    result = result + str(h) + ' hour '
if m > 0:
    result = result + str(m) + ' minute '
if s > 0:
    result = result + str(s) + ' sec '

print (result)
