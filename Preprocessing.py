import pandas as pd
import openpyxl
import re
from underthesea import word_tokenize
from underthesea import text_normalize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Đọc dữ liệu và tách cột
df = pd.read_excel('../Final_data_B1.xlsx')

FEATURE_COLS = ['Premise', 'Hypothesis', 'Final_Label', 'Quality_Status']

df = df[FEATURE_COLS]

# Chuẩn hóa văn bản
def Standardize_sent(text):
    # Đưa về chữ thường
    text = text.lower()
    # Xóa dấu chấm cuối câu và khoảng trắng thừa
    text = re.sub(r"\.$", "", text)
    # Xóa khoảng trắng đầu cuối
    text = text.strip()
    # Chuẩn hóa từ
    text = text_normalize(text)
    text = word_tokenize(text, format='text')
    return text
# Áp dụng theo cột
df[FEATURE_COLS[0]] = df[FEATURE_COLS[0]].apply(Standardize_sent)
df[FEATURE_COLS[1]] = df[FEATURE_COLS[1]].apply(Standardize_sent)

# Gộp 2 câu
SENT = ['Premise', 'Hypothesis']

df['Sent_input'] = df[SENT[0]] + ' [SEP] ' + df[SENT[1]]
df = df.drop(SENT, axis= 1)

# Chia tập train, test
mask = df['Quality_Status'].str.contains('Gold', na=False)

test = df[mask]
train = df[~mask]
train = train.sample(frac=1, random_state=42)

# Xem độ lệch các nhãn trong train và test
# sns.countplot(data = train, x = 'Final_Label')
# sns.countplot(data = test, x = 'Final_Label')
# plt.show()

# Xóa các cột thừa trong X_train, X_test, y_train, y_test
target = ['Final_Label', 'Quality_Status']

X_train = train.drop(target, axis=1)
y_train = train[target[0]]
X_test = test.drop(target, axis=1)
y_test = test[target[0]]

# Chuẩn hóa văn bản thành vector
vectorizer = TfidfVectorizer(max_features=500, ngram_range=(1, 2))
X_train_encoded = vectorizer.fit_transform(X_train['Sent_input'])
X_test_encoded = vectorizer.transform(X_test['Sent_input'])

# # Huấn luyện mô hình
# clf = svm.LinearSVC()
# clf.fit(X_train_encoded, y_train)
# y_pred = clf.predict(X_test_encoded)
#
# # Đánh giá qua các độ đo
# print(classification_report(y_test, y_pred))

# # Vẽ ma trận nhầm lẫn
# labels = [0, 1, 2]
#
# cm = confusion_matrix(y_test, y_pred, labels=labels)
#
# plt.figure(figsize=(8, 6))
# sns.heatmap(
#     cm,
#     annot=True,
#     fmt='d',
#     cmap='Blues',
#     xticklabels=labels,
#     yticklabels=labels
# )
# plt.xlabel('Predicted Label')
# plt.ylabel('True Label')
# plt.title('Confusion Matrix')
# plt.show()

# Tối ưu hóa mô hình

param_grid = [{'kernel': ['linear'], 'C': [0.1, 1, 10, 100, 1000]},
              {'kernel': ['rbf'], 'C': [0.1, 1, 10, 100, 1000],'gamma': [1e-1, 1e-2, 1e-3, 1e-4, 'scale']},
              {'kernel': ['poly'], 'C': [0.1, 1, 10, 100],'degree': [2, 3], 'gamma': ['auto', 'scale'],'coef0': [0.0, 1.0]}
              ]

svm_model = svm.SVC()

grid_search = GridSearchCV(svm_model, param_grid, scoring='f1_macro', cv=5, n_jobs=-1, verbose=2)

print("---- Đang tìm tham số tối ưu -----")
grid_search.fit(X_train_encoded, y_train)

print(f"Tham số tốt nhất: {grid_search.best_params_}")
print(f"Độ chính xác tốt nhất trên tập train: {grid_search.best_score_}")

best_svm = grid_search.best_estimator_
best_y_pred = best_svm.predict(X_test_encoded)

print("\nKết quả trên tập test")
print(classification_report(y_test, best_y_pred))