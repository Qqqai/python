# ciyun.py
#导入词云的库  python都是调库 所以很简单  库就是别人给你写好的东西  你直接拿来用就好了
from wordcloud import WordCloud    
import jieba


#打开文件    我这里打开的是D:\vscode\workspace\python\108.txt这个txt文件  以utf-8的编码格式打开  编码格式这个百度吧 这个我解释不清  百度说的很清楚    .read()这是读取方法  调库的  不用管
names = open(r"D:\vscode\workspace\python\108.txt", "r", encoding="utf-8").read()

#names是获取内容   split是分割函数   比如   (a、b).split("、")分割出来就是  a,b
includes = names.split("、")

#遍历从头到尾遍历一遍
for w in includes:
    jieba.add_word(w)

txt = open(r"D:\vscode\workspace\python\sh.txt", "r", encoding="utf-8").read()
# sh_jieba.py
import jieba

names = open(r"D:\vscode\workspace\python\108.txt", "r", encoding="utf-8").read()

includes = names.split("、")

for w in includes:
    jieba.add_word(w)

txt = open(r"D:\vscode\workspace\python\sh.txt", "r", encoding="utf-8").read()

words = jieba.lcut(txt)

counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
items = list(counts.keys())

for word in items:
    if word not in includes:
        counts.pop(word)

wc = WordCloud(
    font_path=r"C:/Windows/Fonts/msyh.ttc",
    background_color="black",
    height=700,
    width=1000,
    max_font_size=150,
    min_font_size=1
)

wc.generate_from_frequencies(counts)

wc.to_file('d:/视频图片/Saved Pictures/ciyun/词云.jpg')
# w = wordcloud.WordCloud(height=700, font_path='C:\Windows\Fonts\STZHONGS.TTF', width=1000)

# w.generate_from_frequencies(namels)

# w.to_file("shuhu.jpg")
