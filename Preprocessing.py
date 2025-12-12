import pandas as pd
import openpyxl
import re
from underthesea import word_tokenize
from underthesea import text_normalize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import classification_report

# Đọc dữ liệu và tách cột
df = pd.read_excel('../Final_data_B1.xlsx')

FEATURE_COLS = ['Premise', 'Hypothesis', 'Final_Label', 'Quality_Status']

df = df[FEATURE_COLS]

# Chuẩn hóa văn bản
def Standardize_sent(text):
    # Đưa về chữ thường
    text = text.lower()
    # Xóa dấu chấm cuối câu và khoảng trắng thừa
    text = re.sub(r"\.(?=\s|$)", "", text)
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

df['Sent_input'] = df[SENT[0]] + ' ' + df[SENT[1]]
df = df.drop(SENT, axis= 1)

# Chia tập train, test
mask = df['Quality_Status'].str.contains('Gold', na=False)

train = df[mask]
test = df[~mask]

target = ['Final_Label', 'Quality_Status']

X_train = train.drop(target, axis=1)
y_train = train[target[0]]
X_test = test.drop(target, axis=1)
y_test = test[target[0]]

# Chuẩn hóa văn bản thành vector
vectorizer = TfidfVectorizer()
X_train_encoded = vectorizer.fit_transform(X_train['Sent_input'])
X_test_encoded = vectorizer.transform(X_test['Sent_input'])

# Huấn luyện mô hình
clf = svm.LinearSVC()
clf.fit(X_train_encoded, y_train)
y_pred = clf.predict(X_test_encoded)

print(classification_report(y_test, y_pred))