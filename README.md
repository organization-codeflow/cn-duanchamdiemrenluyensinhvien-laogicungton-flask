# cn-duanchamdiemrenluyensinhvien-laogicungton-flask
## 📋 Hướng dẫn Đánh giá Code Tự động cho Sinh viên

### 🎯 Mục tiêu
Repository này đã được thiết lập để tự động đánh giá chất lượng code thông qua GitHub Actions và SonarCloud khi bạn push code lên nhánh **master**.

---

## 🚀 Quy trình Submit Code để Đánh giá

### Bước 1: Clone Repository
```bash
git clone https://github.com/organization-codeflow/cn-duanchamdiemrenluyensinhvien-laogicungton-flask.git
cd cn-duanchamdiemrenluyensinhvien-laogicungton-flask
```

### Bước 2: Phát triển trên nhánh riêng
```bash
# Tạo nhánh mới cho feature
git checkout -b feature/your-feature-name

# Làm việc trên code của bạn
# ... code your implementation ...

# Commit changes
git add .
git commit -m "feat: implement your feature"
```

### Bước 3: Push lên nhánh master để kích hoạt đánh giá
```bash
# Chuyển về nhánh master
git checkout master

# Merge feature branch vào master
git merge feature/your-feature-name

# Push lên remote master - SẼ KÍCH HOẠT ĐÁNH GIÁ TỰ ĐỘNG
git push origin master
```

⚠️ **LƯU Ý QUAN TRỌNG**: Chỉ push lên nhánh **master** khi bạn muốn code được đánh giá chính thức!

---

## 📊 Xem Kết quả Đánh giá

### 1. GitHub Actions
- Vào tab **Actions** trong repository
- Xem chi tiết từng bước workflow
- Kiểm tra log nếu có lỗi

### 2. SonarCloud Dashboard
- Truy cập: https://sonarcloud.io/project/overview?id=cn-duanchamdiemrenluyensinhvien-laogicungton-flask
- Xem các metrics:
  - **Quality Gate**: PASS/FAIL
  - **Bugs**: Số lỗi code
  - **Vulnerabilities**: Lỗ hổng bảo mật
  - **Code Smells**: Code không tối ưu
  - **Coverage**: Phần trăm code được test
  - **Duplications**: Code trùng lặp

---

## 🏃‍♂️ Hướng dẫn Chạy Ứng dụng Flask

### Cài đặt Dependencies
```bash
# Cài đặt Python packages
pip install -r requirements.txt
```

### Chạy Ứng dụng
```bash
# Chạy Flask development server
python app.py
```

Ứng dụng sẽ chạy tại: http://localhost:5000

### API Endpoints
- **GET /** - Trang chủ với giao diện web
- **GET /api/health** - Kiểm tra sức khỏe ứng dụng
- **GET /api/info** - Thông tin ứng dụng

---
