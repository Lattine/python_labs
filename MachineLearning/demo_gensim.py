# -*- coding: utf-8 -*-

# @Time    : 2019/11/28
# @Author  : Lattine

# ======================
import gensim
import jieba
import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn import preprocessing
from sklearn import model_selection

stopwords = set([line.strip() for line in open("data/stopwords.txt", encoding="utf-8")])


# -------------------- Common Methods -----------------
def filter_stopwords(item):
    words = jieba.lcut(item)
    words = [w for w in words if w not in stopwords]
    return words


def multiclass_logloss(predicted, actual, eps=1e-15):
    """ 对数损失度量，多分类版本 """
    if len(actual.shape) == 1:
        actual2 = np.zeros((actual.shape[0], predicted.shape[1]))  # [条数 x 类别]
        for i, val in enumerate(actual):
            actual2[i, val] = 1
        actual = actual2
    clip = np.clip(predicted, eps, 1 - eps)
    rows = actual.shape[0]
    vsota = np.sum(actual * np.log(clip))
    return -1.0 / rows * vsota


def sent2vec(words, embeddings):
    """函数会将语句转化为一个标准化的向量"""
    M = []
    words = [w for w in words if not w[0].isdigit()]
    for w in words:
        try:
            M.append(embeddings[w])
        except:
            continue
    M = np.asarray(M)
    v = M.sum(axis=0)
    if type(v) != np.ndarray:
        return np.zeros(300)
    return v / np.sqrt((v ** 2).sum())


# -------------------- Main Process -------------------
raw = pd.read_csv("data/result_20191121.csv")
raw["tokens"] = raw["content"].apply(filter_stopwords)
tokens = raw["tokens"].values.tolist()
# 用scikit-learn中的Label Encoder将文本标签（Text Label）转化为数字(Integer)
lbl_enc = preprocessing.LabelEncoder()
y = lbl_enc.fit_transform(raw.label.values)
train_x, valid_x, train_y, valid_y = model_selection.train_test_split(raw.tokens.values, y, stratify=y, test_size=0.1, shuffle=True, random_state=123)

# Word2Vec还有3个值得关注的参数，iter是模型训练时迭代的次数，假如参与训练的文本量较少，就需要把这个参数调大一些；
# sg是模型训练算法的类别，1 代表 skip-gram，;0代表 CBOW;
# window控制窗口，它指当前词和预测词之间的最大距离，如果设得较小，那么模型学习到的是词汇间的功能性特征（词性相异），如果设置得较大，会学习到词汇之间的相似性特征（词性相同）的大小，假如语料够多，笔者一般会设置得大一些，8~10。
# model = gensim.models.Word2Vec(tokens, size=50)
# model.save("data/news.model")
model = gensim.models.Word2Vec.load('data/news.model')
embeddings = dict(zip(model.wv.index2word, model.wv.syn0))
print(f"Found {len(embeddings)} word vectors.")

train_x_w2v = [sent2vec(s, embeddings) for s in train_x]
valid_x_w2v = [sent2vec(s, embeddings) for s in valid_x]
train_x_w2v = np.asarray(train_x_w2v)
valid_x_w2v = np.asarray(valid_x_w2v)

# --------- xgboost
clf_xgb = xgb.XGBClassifier(nthread=10, silent=False)
clf_xgb.fit(train_x_w2v, train_y)
predictions = clf_xgb.predict_proba(valid_x_w2v)
print("xgboost + w2v loss :", multiclass_logloss(predictions, valid_y))
clf_xgb = xgb.XGBClassifier(max_depth=7, n_estimators=200, colsample_bytree=0.8, subsample=0.8, nthread=10, learning_rate=0.1)
clf_xgb.fit(train_x_w2v, train_y)
predictions = clf_xgb.predict_proba(valid_x_w2v)
print("xgboost + w2v + param loss :", multiclass_logloss(predictions, valid_y))
# xgboost + w2v loss : 0.41536483030204147
# xgboost + w2v + param loss : 0.3402714746276225
