# -*- coding: utf-8 -*-

# @Time    : 2019/11/28
# @Author  : Lattine

# ======================
import jieba
import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn import preprocessing
from sklearn import decomposition
from sklearn import model_selection
from sklearn import pipeline
from sklearn import metrics
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer


# ---------------- Common Mothods ---------------------
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


def number_normalizer(tokens):
    """将所有数字标识为一个固定标志，以实现降维操作"""
    return ["#NUM" if token[0].isdigit() else token for token in tokens]


class NumberNormalizingVectorizer(TfidfVectorizer):
    def build_tokenizer(self):
        tokenize = super(NumberNormalizingVectorizer, self).build_tokenizer()
        return lambda doc: list(number_normalizer(tokenize(doc)))


# ----------------- Main Process ----------------------
stopwords = [line.strip() for line in open("data/stopwords.txt", encoding="utf-8")]
raw = pd.read_csv("data/train_3k.csv")
print("head", raw.head())
print("unique label", raw.label.unique())

raw["tokens"] = raw["content"].apply(lambda item: " ".join(jieba.lcut(item)))
print("tokens", raw.head())

# 用scikit-learn中的Label Encoder将文本标签（Text Label）转化为数字(Integer)
lbl_enc = preprocessing.LabelEncoder()
y = lbl_enc.fit_transform(raw.label.values)

# 将数据分成训练和验证集。 使用scikit-learn的model_selection模块中的train_test_split来完成
train_x, valid_x, train_y, valid_y = model_selection.train_test_split(raw.tokens.values, y, stratify=y, test_size=0.1, shuffle=True, random_state=123)
print("shape of split", f"train_x : {train_x.shape}, valid_x : {valid_x.shape}")

# ------------- 构建基础模型 TF-IDF + Logistic Regression
tfidf_vec = NumberNormalizingVectorizer(min_df=4, max_df=0.5, max_features=None, ngram_range=(1, 3), use_idf=True, smooth_idf=True, stop_words=stopwords)
tfidf_vec.fit(list(train_x) + list(valid_x))
train_x_tfv = tfidf_vec.transform(train_x)
valid_x_tfv = tfidf_vec.transform(valid_x)
# 利用提取的TFIDF特征来fit一个简单的Logistic Regression
clf_rg = LogisticRegression(C=1.0, solver="lbfgs", multi_class='multinomial')
clf_rg.fit(train_x_tfv, train_y)
predictions = clf_rg.predict_proba(valid_x_tfv)
loss_rg = multiclass_logloss(predictions, valid_y)
print("logistic regression loss(TF-IDF)", loss_rg)

# ----------- 构建词袋模型 BagOfWords + Logistic Regression
bow_vec = CountVectorizer(min_df=4, max_df=0.5, ngram_range=(1, 3), stop_words=stopwords)
bow_vec.fit(list(train_x) + list(valid_x))
train_x_bow = bow_vec.transform(train_x)
valid_x_bow = bow_vec.transform(valid_x)
clf_rg = LogisticRegression(C=1.0, solver="lbfgs", multi_class="multinomial")
clf_rg.fit(train_x_bow, train_y)
predictions = clf_rg.predict_proba(valid_x_bow)
loss_rg = multiclass_logloss(predictions, valid_y)
print("logistic regression loss(BOW)", loss_rg)

# --------- TF-IDF + Naive Bayes
clf_nb = MultinomialNB()
clf_nb.fit(train_x_tfv, train_y)
predictions = clf_nb.predict_proba(valid_x_tfv)
loss_nb = multiclass_logloss(predictions, valid_y)
print("naive bayes loss(TF-IDF)", loss_nb)

# --------- Bow + Naive Bayes
clf_nb = MultinomialNB()
clf_nb.fit(train_x_bow, train_y)
predictions = clf_nb.predict_proba(valid_x_bow)
loss_nb = multiclass_logloss(predictions, valid_y)
print("naive bayes loss(BOW)", loss_nb)

# ------------- SVM , SVM需要花费大量时间，在应用SVM之前，将使用奇异值分解来减少TF-IDF中的特征数量(对于SVM来说，SVD的components的合适调整区间一般为120~200 )
svd = decomposition.TruncatedSVD(n_components=120)
svd.fit(train_x_tfv)
train_x_svd = svd.transform(train_x_tfv)
valid_x_svd = svd.transform(valid_x_tfv)
# 对从SVD获得的数据进行缩放
scaler = preprocessing.StandardScaler()
scaler.fit(list(train_x_svd) + list(valid_x_svd))
train_x_svd_scl = scaler.transform(train_x_svd)
valid_x_svd_scl = scaler.transform(valid_x_svd)
# 应用SVM模型进行文本分类
clf_svm = SVC(C=1.0, probability=True)
clf_svm.fit(train_x_svd_scl, train_y)
predictions = clf_svm.predict_proba(valid_x_svd_scl)
print("SVM loss:", multiclass_logloss(predictions, valid_y))

# ------ xgboost
clf_xgb = xgb.XGBClassifier(max_depth=7, n_estimators=200, colsample_bytree=0.8, subsample=0.8, nthread=10, learning_rate=0.1)
clf_xgb.fit(train_x_tfv.tocsc(), train_y)
predictions = clf_xgb.predict_proba(valid_x_tfv.tocsc())
print("xgboost loss(TF-IDF)", multiclass_logloss(predictions, valid_y))
clf_xgb = xgb.XGBClassifier(max_depth=7, n_estimators=200, colsample_bytree=0.8, subsample=0.8, nthread=10, learning_rate=0.1)
clf_xgb.fit(train_x_bow.tocsc(), train_y)
predictions = clf_xgb.predict_proba(valid_x_bow.tocsc())
print("xgboost loss(BOW)", multiclass_logloss(predictions, valid_y))
clf_xgb = xgb.XGBClassifier(max_depth=7, n_estimators=200, colsample_bytree=0.8, subsample=0.8, nthread=10, learning_rate=0.1)
clf_xgb.fit(train_x_svd_scl, train_y)
predictions = clf_xgb.predict_proba(valid_x_svd_scl)
print("xgboost loss(TF-IDF with SVD Scaler)", multiclass_logloss(predictions, valid_y))

# -------- 网格搜索 (有待研究)
# 网格搜索之前，需要创建一个评分函数
all_scorer = metrics.make_scorer(multiclass_logloss, greater_is_better=False, needs_proba=True)
svd = decomposition.TruncatedSVD()
scl = preprocessing.StandardScaler()
lr_model = LogisticRegression()
clf = pipeline.Pipeline([
    ("svd", svd),
    ("scl", scl),
    ("lr", lr_model)
])
# 需要一个参数网格（A Grid of Parameters）
grid_params = {
    "svd__n_components": [120, 180],
    "lr__C": [0.1, 1.0, 10],
    "lr__penalty": ["l1", "l2"]
}
model = model_selection.GridSearchCV(estimator=clf, param_grid=grid_params, scoring=all_scorer, verbose=10, n_jobs=-1, iid=True, refit=True, cv=2)
model.fit(train_x_tfv, train_y)
print("Best score: %0.3f" % model.best_score_)
print("Best params set:")
best_parameters = model.best_estimator_.get_params()
for param_name in sorted(grid_params.keys()):
    print("\t%s: %r" % (param_name, best_parameters[param_name]))
