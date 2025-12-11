import pandas as pd
import openpyxl
import re
from underthesea import word_tokenize
from underthesea import text_normalize

# Đọc dữ liệu và tách cột
df = pd.read_excel('Final_data_B1.xlsx')

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

print(df)