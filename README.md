<p align="center">
  <img src="https://camo.githubusercontent.com/b16ecdcac9c3d21ec3a49459430f747b46b3a37acc95ee468d87d0ec61ff2392/68747470733a2f2f692e696d6775722e636f6d2f576d4d6e5352742e706e67">
</p>

# [DS102.P12.Group5] - ĐỒ ÁN MÔ HÌNH SUY LUẬN NGÔN NGỮ TỰ NHIÊN (ViSNLI)

## Giới thiệu
Dự án này được thực hiện trong khuôn khổ học phần **“Học máy thống kê” (DS102)**.
Mục tiêu của dự án là xây dựng bộ dữ liệu chuẩn cho bài toán Suy luận ngôn ngữ tự nhiên (NLI) tiếng Việt và huấn luyện các mô hình học máy để phân loại quan hệ giữa các câu (Entailment, Contradiction, Neutral).

Dự án đạt kết quả tốt nhất **84% Accuracy** với mô hình **PhoBERT**.

## Thông tin dự án
* **Trường:** Trường Đại học Công nghệ Thông tin, ĐHQG-HCM
* **Khoa:** Khoa học Máy tính
* **Môn học:** Học máy thống kê (DS102)
* **Giảng viên hướng dẫn:** ThS. Huỳnh Văn Tín
* **Nhóm sinh viên thực hiện:** Nhóm 5

## Danh sách thành viên
| STT | Họ tên | MSSV | Chức vụ |
|:---:|---|:---:|:---:|
| 1 | **Huỳnh Hải Hiền** | **23520457** | **Nhóm trưởng** |
| 2 | **Trần Hoàng Long** | **23520890** | Thành viên |
| 3 | **Vũ Hoàng Hiệp** | **23520467** | Thành viên |
| 4 | **Nguyễn Mạnh Tuấn** | **21522755** | Thành viên |
| 5 | **Trần Bá Cảnh** | **22520144** | Thành viên |

## Công nghệ sử dụng
<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch">
  <img src="https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" alt="HuggingFace">
  <img src="https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-learn">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
</p>

* **Ngôn ngữ:** Python
* **Thư viện chính:** Transformers (PhoBERT), Scikit-learn (SVM, Naive Bayes), Underthesea (Tách từ), Pandas.
* **Môi trường:** Google Colab (GPU T4).

## Kết quả đạt được (Model Performance)

| STT | Mô hình | Loại | Độ chính xác (Accuracy) | Ghi chú |
|:---:|---|:---:|:---:|---|
| 1 | Multinomial Naive Bayes | Machine Learning | **41.78%** | Baseline |
| 2 | SVM (Support Vector Machine) | Machine Learning | **46.48%** | Baseline |
| 3 | **PhoBERT (Fine-tuned)** | **Deep Learning** | **84%** | **Best Model**  |

## Hướng dẫn cài đặt & Chạy demo

Bạn có thể chọn 1 trong 2 cách sau:
### Cách 1: Chạy nhanh trên Google Colab (Khuyên dùng)
Không cần cài đặt, chạy ngay trên trình duyệt.
1. Truy cập [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Vietnam-NLI-Project/vietnam-nli-project/blob/main/notebooks/03_Advanced_PhoBERT.ipynb)
2. Chọn tab **GitHub**.
3. Dán đường link sau vào ô tìm kiếm:
   `https://github.com/Vietnam-NLI-Project/vietnam-nli-project`
4. Chọn file `notebooks/03_Advanced_PhoBERT.ipynb` để xem mô hình tốt nhất (84%).
5. Vào menu **Runtime** -> **Change runtime type** -> Chọn **T4 GPU** để chạy nhanh hơn.

### Cách 2: Chạy trên máy cá nhân (Local Machine)
Dành cho người muốn nghiên cứu sâu code và debug.

**Bước 1: Clone repository**
```bash
git clone https://github.com/Vietnam-NLI-Project/vietnam-nli-project.git
```
**Bước 2: Di chuyển vào thư mục**
```bash
cd vietnam-nli-project
```
**Bước 3: Chạy Notebook**
Mở VS Code hoặc Jupyter Notebook và chạy file: `notebooks/03_Advanced_PhoBERT.ipynb`

## Dữ liệu (Dataset)
Dữ liệu đã được tích hợp sẵn trong GitHub để phục vụ việc chạy mô hình.

Tuy nhiên, để xem mô tả chi tiết và có cái nhìn rõ nhất về dữ liệu, hãy truy cập kho lưu trữ chính thức trên **Kaggle**. Tại đây hỗ trợ:

* **Trực quan hóa (Data Visualization):** Xem biểu đồ phân phối và thống kê dữ liệu ngay trên web.
* **Demo hiệu năng (Inference):** Chạy thử nghiệm Model ngay lập tức (Test nhanh kết quả).
* **Pre-trained Models:** Tải xuống đầy đủ các phiên bản Model (`v1` & `v2`).

**Truy cập ngay:** [**ViSNLI Dataset on Kaggle**](https://www.kaggle.com/datasets/hunhhahin/visnli/data)

---
<p align="center">Made with ❤️ by <b>Group 5 (DS102)</b></p>
