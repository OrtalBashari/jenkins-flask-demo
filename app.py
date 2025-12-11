# app.py
from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    """מציג את דף הבית ומעביר לו נתונים."""
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    return render_template('index.html', time_data=current_time)

def jenkins_test_run():
    """פונקציה קצרה לבדיקת ה-CI שיוצאת מיד."""
    print("--- CI TEST SUCCESS: Flask module loaded successfully ---")
    # אם הקוד מגיע לכאן, זה הצלחה, אז אנחנו יוצאים מיד
    import sys
    sys.exit(0) # קוד יציאה 0 = הצלחה

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)