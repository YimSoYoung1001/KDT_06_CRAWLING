import re

m = re.match('[a-z]+', 'Python')
print(m)
print(re.search('apple', 'I like apple!'))

p = re.compile('[a-z]+')
m = p.match('python')
print(m)
print(p.search('I like apple 123'))


print('-'*50)
m = re.match('[a-z]+', 'pythoN')
print(m)

m = re.match('[a-z]+', 'PYthon')
print(m)


print('-'*50)
print(re.match('[a-z]+', 'regexpython'))
print(re.match('[a-z]+', ' regexpython'))
print(re.match('[a-z]+', 'regexpythoN'))
print(re.match('[a-z]+$', 'regexpythoN'))
print(re.match('[a-z]+', 'regexPython'))
print(re.match('[a-z]+$', 'regexpython'))


print('-'*50)
p = re.compile('[a-z]+')
print(p.findall('life is too short! Regular expression test'))

result = p.search('I like apple 123')
print(result)
print(result.group())

result = p.findall('I like apple 123')
print(result)


print('-'*50)
tel_checker = re.compile("^(\d{2,3})-(\d{3,4})-(\d{4})$")

print(tel_checker.match('02-123-4567'))
print(tel_checker.match('02-123-4567').group())
print(tel_checker.match('053-950-45678'))
print(tel_checker.match('053950-4567'))

