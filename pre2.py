import torch
import numpy as np
import pandas as pd
from transformers import AutoTokenizer, AutoModel
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from pyvi import ViTokenizer
from tqdm import tqdm

# 1. ĐỌC DỮ LIỆU
df = pd.read_excel('Final_data_B1.xlsx')

def clean_text(text):
    return ViTokenizer.tokenize(str(text).lower())

df['P_clean'] = df['Premise'].apply(clean_text)
df['H_clean'] = df['Hypothesis'].apply(clean_text)

# 2. TRÍCH XUẤT TF-IDF (CHỈ LẤY 300 TỪ QUAN TRỌNG NHẤT)
tfidf = TfidfVectorizer(max_features=300, ngram_range=(1, 1))
X_tfidf = tfidf.fit_transform(df['P_clean'] + " " + df['H_clean']).toarray()

# 3. TRÍCH XUẤT PHOBERT (DÙNG ĐỊNH DẠNG CẶP CÂU CHUẨN)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tokenizer = AutoTokenizer.from_pretrained("vinai/phobert-base")
phobert = AutoModel.from_pretrained("vinai/phobert-base").to(device)
phobert.eval()

@torch.no_grad()
def get_bert_features(p_list, h_list, batch_size=16):
    all_feats = []
    for i in tqdm(range(0, len(p_list), batch_size), desc="BERT Features"):
        # QUAN TRỌNG: Truyền 2 tham số riêng biệt để PhoBERT hiểu quan hệ cặp câu
        enc = tokenizer(p_list[i:i+batch_size], h_list[i:i+batch_size], 
                        padding=True, truncation=True, max_length=128, return_tensors="pt").to(device)
        outputs = phobert(**enc)
        all_feats.append(outputs.last_hidden_state[:, 0, :].cpu().numpy())
    return np.vstack(all_feats)

X_bert = get_bert_features(df['P_clean'].tolist(), df['H_clean'].tolist())

# 4. KẾT HỢP VÀ CHIA TẬP DỮ LIỆU
X_all = np.hstack([X_bert, X_tfidf])
train_idx = df[df['Dataset_Group'] == 'TRAIN'].index
test_idx = df[df['Dataset_Group'] == 'TEST'].index

X_train, X_test = X_all[train_idx], X_all[test_idx]
y_train, y_test = df.loc[train_idx, 'Final_Label'], df.loc[test_idx, 'Final_Label']

# 5. MÔ HÌNH LOGISTIC REGRESSION (MẠNH VÀ ỔN ĐỊNH HƠN SVM/RF KHI DỮ LIỆU ÍT)
# C=0.01 để ép mô hình không được "học vẹt"
model = LogisticRegression(C=0.1, max_iter=1000, solver='lbfgs', multi_class='multinomial')

print("\n--- Đang huấn luyện mô hình ---")
model.fit(X_train, y_train)

# Kiểm tra độ chính xác trên tập TRAIN để xem có bị Overfit không
train_acc = model.score(X_train, y_train)
test_acc = model.score(X_test, y_test)

print(f"Độ chính xác trên tập TRAIN: {train_acc:.2f}")
print(f"Độ chính xác trên tập TEST: {test_acc:.2f}")

# 6. ĐÁNH GIÁ CHI TIẾT
y_pred = model.predict(X_test)
print("\nKẾT QUẢ CUỐI CÙNG:")
print(classification_report(y_test, y_pred, target_names=['Entailment (0)', 'Neutral (1)', 'Contradiction (2)']))