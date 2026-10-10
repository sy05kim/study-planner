from flask import Flask, request, jsonify

app = Flask(__name__)

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return response


@app.route("/", methods=["GET"])
def home():
    return "AI Study Planner API is running!"


@app.route("/generate", methods=["POST", "OPTIONS"])
def generate_plan():
    if request.method == "OPTIONS":
        return "", 204

    data = request.get_json()

    subject = data.get("subject", "학습")
    goal = data.get("goal", "기초 이해")
    days = data.get("days", 7)
    level = data.get("level", "초급")

    try:
        days = int(days)
    except:
        days = 7

    plan = []

    for day in range(1, days + 1):
        plan.append({
            "day": day,
            "title": f"{subject} {day}일차 학습",
            "tasks": [
                f"{subject} 핵심 개념 공부하기",
                f"{level} 수준에 맞는 예제 풀기",
                f"{goal} 목표와 연결해서 정리하기",
                "오늘 배운 내용 3줄 요약하기"
            ]
        })

    return jsonify({
        "message": "학습 계획이 생성되었습니다.",
        "plan": plan
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)