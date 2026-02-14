from flask import Flask, render_template, request, jsonify
import string
import random

app = Flask(__name__)

def generate_password_logic(length, min_lowercase, min_uppercase, min_digits, min_special):
    """Generate a secure random password based on requirements."""
    
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = '!@#$%^&*()_+-=[]{}|;:,.<>?'
    
    # Validate that requirements don't exceed length
    total_required = min_lowercase + min_uppercase + min_digits + min_special
    if total_required > length:
        return None, "Total minimum requirements exceed password length"
    
    password_chars = []
    
    # Add required characters
    for _ in range(min_lowercase):
        password_chars.append(random.choice(lowercase))
    for _ in range(min_uppercase):
        password_chars.append(random.choice(uppercase))
    for _ in range(min_digits):
        password_chars.append(random.choice(digits))
    for _ in range(min_special):
        password_chars.append(random.choice(special))
    
    # Fill the rest randomly from all character types
    all_characters = lowercase + uppercase + digits + special
    remaining = length - len(password_chars)
    for _ in range(remaining):
        password_chars.append(random.choice(all_characters))
    
    # Shuffle to avoid predictable patterns
    random.shuffle(password_chars)
    
    # Convert to string
    password = ''.join(password_chars)
    
    # Calculate stats
    stats = {
        'length': len(password),
        'lowercase': sum(1 for c in password if c in lowercase),
        'uppercase': sum(1 for c in password if c in uppercase),
        'digits': sum(1 for c in password if c in digits),
        'special': sum(1 for c in password if c in special)
    }
    
    return password, stats

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        length = int(data.get('length', 16))
        min_lowercase = int(data.get('min_lowercase', 1))
        min_uppercase = int(data.get('min_uppercase', 1))
        min_digits = int(data.get('min_digits', 1))
        min_special = int(data.get('min_special', 1))
        
        password, stats = generate_password_logic(
            length, min_lowercase, min_uppercase, min_digits, min_special
        )
        
        if password is None:
            return jsonify({'error': stats}), 400
        
        return jsonify({'password': password, 'stats': stats})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("\n🔐 Password Generator Web GUI")
    print("=" * 50)
    print("Starting server...")
    print("Open your browser and go to: http://127.0.0.1:5000")
    print("Press CTRL+C to stop the server")
    print("=" * 50 + "\n")
    app.run(debug=True, port=5000)
