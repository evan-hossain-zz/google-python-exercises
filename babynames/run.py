build_command = 'python babynames.py'
for i in range(1990, 2009, 2):
  build_command += ' ' + 'baby' + str(i) + '.html'
print(build_command)