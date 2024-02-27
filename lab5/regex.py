#ex1
import re
# * ? + 
# * -> [0; +eternity) {0, +eternity}
# + -> [1; +eternity) {1, +eternity}
# ? -> [0;1] {0, 1}
# \w -> [a-zA-Z0-9_]
# \W -> [^a-zA-Z0-9_]
# \d -> [0-9]
# \D -> [^0-9]
p = re.compile('[a0|b]*')
test_string = "abab0"

m = p.match(test_string)
print(m)

#ex2
import re
p = re.compile('ab{2,3}')
test_string = "abbbabb"

m = p.match(test_string)
print(m)

#ex3
import re
s = "hello_world"
p = re.compile('[a-z]+_[a-z]+')
m = p.findall(s)
for match in m:
    print(match)

#ex4
import re
s = "World"
p = re.compile('[A-Z]{1}[a-z]+')
m = p.findall(s)
for match in m:
    print(match)

#ex5
import re
s = "aworld027-b"
p = re.compile('a.*b')
m = p.match(s)
print(m.group())

#ex6
import re
str = "This is a test, string. With spaces, commas, and dots."
p= re.compile('[ ,.]')
replace = ':'
result = re.sub(p, replace, str)

print(result)

#ex7
def snake_to_camel(word):
        import re
        return ''.join(x.capitalize() or '_' for x in word.split('_'))

print(snake_to_camel('hello_world'))


#ex8
import re
text = "SplitThisStringAtUppercaseLetters"
print(re.findall('[A-Z][^A-Z]*', text))

#ex9
import re
def capital_words_spaces(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)

print(capital_words_spaces("HelloWorld"))

#ex10
def camel_to_snake(text):
        import re
        str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()

print(camel_to_snake('HelloWorld'))