import re
import sys


if len(sys.argv) < 3:
    print("Nalezy wprowadzić jako pierwszy argument sciezke do pliku, a jako drugi --zwijane lub --niezwijane")
    exit()


filepath = sys.argv[2]
f = open(filepath, "r")

content = f.read()

def comment_match(file):
    comments = re.search("/\\*[^*]*\\*+(?:[^/*][^*]*\\*+)*/", file)
    if comments:
        return (comments.group())
    else:
        return None

def function_match(file):
    functions = re.search()
    if functions:
        return (funstions.group())
    else:
        return None

result_comment = comment_match(content)
if sys.argv[1] == '--niezwijane':
    result_comment = result_comment.replace('/*', '')
    result_comment = result_comment.replace('*/', '')
    print(result_comment)
elif sys.argv[1] == '--zwijane':
    result_comment = result_comment.replace('/*', '')
    result_comment = result_comment.replace('*/', '')
    result_comment = result_comment.replace('\n', ' ')
    print(result_comment)



