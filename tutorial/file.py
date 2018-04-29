# file write mode
fo = open('test.txt', 'w')
print('Name:' ,fo.name)
print('Is closed:', fo.closed)
print('Opening Mode :', fo.mode)
fo.write('I love py')
fo.write(' and JavaScript')
fo.close()

fo = open('test.txt', 'r+')
text = fo.read(10)
print('text')
fo.close()


# create a file
fo = open('test2.txt', 'w+')
fo.write('BBQ')
fo.close()
