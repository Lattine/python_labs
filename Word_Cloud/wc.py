# -*- coding: utf-8 -*-

# @Time    : 2019/11/7
# @Author  : Lattine

# ======================


def word_cloud(texts, stops_path=None, font_path=None):
    import jieba
    from wordcloud import WordCloud

    # --------- 加载停用词 -----------
    def load_stopwords(path):
        with open(path, "r", encoding="utf-8") as fr:
            stopwords = [line.strip() for line in fr]
            stopwords = set(stopwords)
            return stopwords

    # -------- 主程序 ---------
    stopwords = load_stopwords(stops_path)

    wc = WordCloud(
        background_color='white',  # 背景颜色
        max_words=100,  # 最大词数
        max_font_size=100,  # 显示字体的最大值
        font_path=font_path,  # 解决显示口字型乱码问题，可更换字体
        random_state=42,  # 为每个词返回一个PIL颜色
        width=1000,  # 图片的宽
        height=860,  # 图片的长
        collocations=False,  # 去除词汇重复显示
    )

    tokens = []
    for text in texts:
        segs = jieba.lcut(text.strip())
        segs = [w for w in segs if w not in stopwords or w.isdigit()]
        tokens.extend(segs)
    text = " ".join(tokens)

    wc.generate(text)
    wc.to_file("./wc.png")


if __name__ == '__main__':
    # 文件需要视情况而定读取方案， 通常加载成句子构成的LIST
    import pandas as pd

    raw = pd.read_csv("../data/train_data.csv")
    texts = raw["content"].values.tolist()
    word_cloud(texts, stops_path="./stopwords.txt", font_path="./simhei.ttf")
