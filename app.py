from flask import Flask, render_template, jsonify, request

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

@app.route('/api/sum', methods=['GET'])
def sum_numbers():
    """
    API tính tổng 2 số.
    Gọi: /api/sum?a=5&b=7  →  Trả về 12
    """
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        return jsonify({
            'a': a,
            'b': b,
            'sum': a + b
        })
    except ValueError:
        return jsonify({'error': 'Vui lòng truyền số hợp lệ'}), 400

if __name__ == '__main__':
    # Chạy ứng dụng trong development mode
    app.run(debug=True, host='0.0.0.0', port=5000)
