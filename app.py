from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# تحميل بيانات ملف CSV
data = pd.read_csv("sheet11.csv")  # ضع اسم ملفك هنا

@app.route("/")
def home():
    return render_template("search.html")


@app.route("/search", methods=["POST"])
def search():
    roll_number = request.form["roll_number"]  # قراءة رقم الجلوس من المستخدم
    result = data[data["رقم الجلوس"] == int(roll_number)]

    if not result.empty:
        name = result['اسم الطالب'].values[0]
        location = result['المكان'].values[0]
        return f"اسم الطالب: {name}<br>مكان اللجنة: {location}"
    else:
        return "رقم الجلوس غير موجود."


if __name__ == "__main__":
    app.run(debug=True)
