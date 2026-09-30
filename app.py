from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# Simple in-memory student data
students = [
    {"id": 1, "name": "Alice Smith", "status": None},
    {"id": 2, "name": "Bob Jones", "status": None},
    {"id": 3, "name": "Charlie Brown", "status": None},
    {"id": 4, "name": "Diana Prince", "status": None},
    {"id": 5, "name": "Evan Wright", "status": None}
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Student Attendance System</title>
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }

    body {
      background-color: #f4f6f9;
      color: #333;
      display: flex;
      justify-content: center;
      padding: 40px 20px;
    }

    .container {
      width: 100%;
      max-width: 600px;
      background: #ffffff;
      padding: 28px;
      border-radius: 12px;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
    }

    h1 {
      font-size: 24px;
      margin-bottom: 20px;
      text-align: center;
      color: #1e293b;
    }

    .summary-cards {
      display: flex;
      gap: 12px;
      margin-bottom: 24px;
    }

    .card {
      flex: 1;
      padding: 16px;
      border-radius: 8px;
      text-align: center;
      background-color: #f8fafc;
      border: 1px solid #e2e8f0;
    }

    .card.present-card {
      background-color: #f0fdf4;
      border-color: #bbf7d0;
      color: #166534;
    }

    .card.absent-card {
      background-color: #fef2f2;
      border-color: #fecaca;
      color: #991b1b;
    }

    .card .count {
      font-size: 28px;
      font-weight: bold;
      margin-top: 4px;
    }

    .card .label {
      font-size: 14px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .student-list {
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    .student-item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 14px 18px;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      background-color: #ffffff;
      transition: background-color 0.2s;
    }

    .student-item:hover {
      background-color: #f8fafc;
    }

    .student-name {
      font-weight: 600;
      font-size: 16px;
      color: #334155;
    }

    .action-buttons {
      display: flex;
      gap: 8px;
    }

    .btn {
      padding: 8px 16px;
      font-size: 14px;
      font-weight: 600;
      border-radius: 6px;
      border: 1px solid transparent;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .btn-present {
      background-color: #ffffff;
      color: #16a34a;
      border-color: #16a34a;
    }

    .btn-present:hover {
      background-color: #f0fdf4;
    }

    .btn-present.active {
      background-color: #16a34a;
      color: #ffffff;
    }

    .btn-absent {
      background-color: #ffffff;
      color: #dc2626;
      border-color: #dc2626;
    }

    .btn-absent:hover {
      background-color: #fef2f2;
    }

    .btn-absent.active {
      background-color: #dc2626;
      color: #ffffff;
    }
  </style>
</head>
<body>

  <div class="container">
    <h1>Student Attendance System</h1>

    <div class="summary-cards">
      <div class="card present-card">
        <div class="label">Present</div>
        <div class="count" id="present-count">0</div>
      </div>
      <div class="card absent-card">
        <div class="label">Absent</div>
        <div class="count" id="absent-count">0</div>
      </div>
    </div>

    <div class="student-list" id="student-list">
      <!-- Student items rendered dynamically -->
    </div>
  </div>

  <script>
    let students = {{ students_json|safe }};

    function updateSummary() {
      const presentCount = students.filter(s => s.status === 'present').length;
      const absentCount = students.filter(s => s.status === 'absent').length;

      document.getElementById('present-count').textContent = presentCount;
      document.getElementById('absent-count').textContent = absentCount;
    }

    function markAttendance(studentId, status) {
      const student = students.find(s => s.id === studentId);
      if (student) {
        student.status = status;
        renderStudents();
        updateSummary();
      }
    }

    function renderStudents() {
      const container = document.getElementById('student-list');
      container.innerHTML = '';

      students.forEach(student => {
        const item = document.createElement('div');
        item.className = 'student-item';

        const nameSpan = document.createElement('span');
        nameSpan.className = 'student-name';
        nameSpan.textContent = student.name;

        const buttonGroup = document.createElement('div');
        buttonGroup.className = 'action-buttons';

        const presentBtn = document.createElement('button');
        presentBtn.className = `btn btn-present ${student.status === 'present' ? 'active' : ''}`;
        presentBtn.textContent = 'Present';
        presentBtn.onclick = () => markAttendance(student.id, 'present');

        const absentBtn = document.createElement('button');
        absentBtn.className = `btn btn-absent ${student.status === 'absent' ? 'active' : ''}`;
        absentBtn.textContent = 'Absent';
        absentBtn.onclick = () => markAttendance(student.id, 'absent');

        buttonGroup.appendChild(presentBtn);
        buttonGroup.appendChild(absentBtn);

        item.appendChild(nameSpan);
        item.appendChild(buttonGroup);

        container.appendChild(item);
      });
    }

    // Initial render
    renderStudents();
    updateSummary();
  </script>
</body>
</html>
"""

@app.route("/")
def home():
    import json
    return render_template_string(HTML_TEMPLATE, students_json=json.dumps(students))

if __name__ == "__main__":
    app.run(port=5000, debug=True)
