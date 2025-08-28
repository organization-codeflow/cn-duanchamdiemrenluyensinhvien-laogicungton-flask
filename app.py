from flask import Flask, render_template, jsonify

# Tạo Flask application
app = Flask(__name__)

# Cấu hình cơ bản
app.config['SECRET_KEY'] = 'your-secret-key-here'

@app.route('/')
def home():
    """Trang chủ"""
    return render_template('index.html')

@app.route('/api/health')
def health_check():
    """API kiểm tra sức khỏe của ứng dụng"""
    return jsonify({
        'status': 'healthy',
        'message': 'Flask application is running successfully!'
    })

@app.route('/api/info')
def app_info():
    """API thông tin ứng dụng"""
    return jsonify({
        'name': 'Flask Simple App',
        'version': '1.0.0',
        'description': 'Dự án Flask đơn giản nhất'
    })

if __name__ == '__main__':
    # Chạy ứng dụng trong development mode
    app.run(debug=True, host='0.0.0.0', port=5000)
