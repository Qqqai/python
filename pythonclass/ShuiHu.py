# sh_jieba.py
import jieba

names = open(r'D:\vscode\workspace\python\108.txt', 'r', encoding='utf-8').read()

includes = names.split('、')

for w in includes:
    jieba.add_word(w)

txt = open(r'D:\vscode\workspace\python\sh.txt', 'r', encoding='utf-8').read()
words=jieba.lcut(txt)

counts = {}
for word in words:
    if len(word)==1:
        continue
    else:
        counts[word] = counts.get(word, 0)+1
items = list(counts.items())
items.sort(key = lambda x:x[1], reverse=True)

pm = 1

for word, count in items:
    if word in includes:
        print('{0}:{1},{2}'.format( pm, word, count))
        pm = pm+1



