const form = document.getElementById("plannerForm");
const resultDiv = document.getElementById("result");

form.addEventListener("submit", async function (e) {
  e.preventDefault();

  const subject = document.getElementById("subject").value;
  const goal = document.getElementById("goal").value;
  const days = document.getElementById("days").value;
  const level = document.getElementById("level").value;

  resultDiv.innerHTML = "학습 계획을 생성 중입니다...";

  try {
    const response = await fetch("http://127.0.0.1:5000/generate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        subject: subject,
        goal: goal,
        days: days,
        level: level,
      }),
    });

    const data = await response.json();

    resultDiv.innerHTML = `
      <h2>생성된 학습 계획</h2>
      <pre>${data.plan}</pre>
    `;
  } catch (error) {
    resultDiv.innerHTML = "오류가 발생했습니다. 백엔드 서버를 확인해주세요.";
    console.error(error);
  }
});