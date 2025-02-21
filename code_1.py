#1 Dot (r'a.c')
import re


text ="afc"
pattern= r"a.c"
match = re.match(pattern.text)
print(match.group() if match else "No match")

text = " abc ac axc"
patten = r"a.c"
matches = re.findall(pattern,text)
print(matches)

#2 Caret(^)
text = "abcdef"
pattern = r"^abc"
match = re.match(pattern, text)
print(match.group() if match else "No match")

text = " abc def abc"
patten = r"abc"
matches = re.findall(pattern,text)
print(matches)

#3 Dollar($)
text = "xyzabc"
pattern = r"abc$"
match = re.search(pattern, text)
print(match.group() if match else "No match")

text = " abc def abc"
patten = r"abc$"
matches = re.findall(pattern,text)
print(matches)

#4 Square Brackets ([])
text = "Hello"
pattern = r"[aeiou]"
match = re.search(pattern, text)
print(match.group() if match else "No match")

text = "Hello world all item"
patten = r"[aeiou]"
matches = re.findall(pattern,text)
print(matches)

#5 Hypen(-)
text = "abc9123 123"
pattern = r"[0-9]"
match = re.search(pattern, text)
print(match.group() if match else "No match")

text = "abc123 def456 9"
patten = r"[0-9]"
matches = re.findall(pattern,text)
print(matches)

#6 Asterisk (*)
text = "abcc abccc"
pattern = r"abc*"
match = re.match(pattern, text)
print(match.group() if match else "No match")

text = "abcc ab sc s"
patten = r"abc*"
matches = re.findall(pattern,text)
print(matches)

#7 Plus (+)
text_1 = "ac abcc ac abc"
text_2 = "abc ac abc"
pattern = r"abc+"
match = re.match(pattern, text_1)
match_2 = re.match(pattern, text_2)
print(match.group() if match else "No match")
print(match_2.group() if match_2 else "No match_2")

text = "abcc abc a abcd ab"
patten = r"abc+"
matches = re.findall(pattern,text)
print(matches)

#8 Question Mark (?)
text = "abdca"
pattern = r"abc?"
match = re.match(pattern, text)
print(match.group() if match else "No match")

text = "abcc ab abcc abgfda"
patten = r"abc?"
matches = re.findall(pattern,text)
print(matches)

#9 Parentheses (())
text = "abcabcabcabc abc"
pattern = r"(abc)+"
match = re.match(pattern, text)
print(match.group() if match else "No match")

text = "abcabc abchello abdcc"
patten = r"(abc)+"
matches = re.findall(pattern,text)
print(matches)

#10 Bakslash (\.)
text = "file.txt"
pattern = r"\."
match = re.match(pattern, text)
print(match.group(0) if match else "No match")

text = "file.txt image.jpg"
patten = r"\."
matches = re.findall(pattern,text)
print(matches)

