ส่วนที่ 4 — จำลองข้อมูลทีละรายการด้วย Loop

# เตรียมพื้นที่เก็บข้อมูล

students = {}
enrollments = []
payments = []

payment_id = 1

print("เตรียมพื้นที่สำหรับสร้างข้อมูลเรียบร้อยแล้ว")

# สร้างนักเรียน 450 คน
# จำลองข้อมูลทีละรายการด้วย Loop
random.seed(11)

students = {}

for i in range(1, 451):

    # สุ่มเพศ
    gender = random.choice(["ชาย", "หญิง"])

    # สุ่มระดับชั้นก่อน
    grade = random.choice(GRADE)

    # กำหนดอายุให้สัมพันธ์กับระดับชั้น
    if grade == "ม.4":
        age = random.randint(15, 16)

    elif grade == "ม.5":
        age = random.randint(16, 17)

    else:  # ม.6
        age = random.randint(17, 18)

    # สร้างรหัสนักเรียน
    student_id = f"STU{i:04d}"

    # สร้างนักเรียน
    student = Student(
        student_id,
        generate_student_name(gender),
        gender,
        age,
        grade,
        random.choice(SCHOOLS),
        generate_phone()
    )

    # เก็บข้อมูล
    students[student_id] = student

print(
    f"จำลองนักเรียนเสร็จแล้วทั้งหมด {len(students)} คน"
)

for course in courses.values():
    course.enrolled_count = 0

print("รีเซ็ตจำนวนที่นั่งของทุกคอร์สเรียบร้อยแล้ว")

# จำลองการลงทะเบียนทีละรายการ
# นักเรียน 1 คน → เลือก 1 คอร์สต่อการลงทะเบียน
enrollments = []

for enrollment_id, student in enumerate( students.values(), start=1):
    course = random.choice(list(courses.values()))
    discount_rate = random.choice([0, 0.05, 0.10])
    enrollment = simulate_registration(
        enrollment_id,
        student,
        course,
        discount_rate )
    enrollments.append(enrollment)

print("สร้างรายการลงทะเบียน:", len(enrollments), "รายการ" )


# สรุปจำนวนที่นั่งของแต่ละคอร์ส
course_status = []
for course in courses.values():
    available = course.available_seats()
    course_status.append({
        "รหัสคอร์ส": course.course_id,
        "ชื่อคอร์ส": course.course_name,
        "จำนวนที่นั่ง": course.capacity,
        "ลงทะเบียนแล้ว": course.enrolled_count,
        "ที่นั่งคงเหลือ": available,
        "สถานะ": "เต็ม" if available == 0 else "ยังมีที่ว่าง"})
course_status_df = pd.DataFrame(course_status)
display(course_status_df)



# จำลองการชำระเงินทีละรายการ
payments = []
payment_id = 1

for enrollment in enrollments:
    # ตรวจสอบว่าลงทะเบียนสำเร็จหรือไม่
    if enrollment.status == "ลงทะเบียนสำเร็จ":
        payment = Payment(
            payment_id,
            enrollment,
            enrollment.enroll_date,
            random.choice(PAYMENT_METHODS))
        # เก็บข้อมูลการชำระเงิน
        payments.append(payment)
        payment_id += 1

print(f"จำลองการชำระเงินเสร็จแล้วทั้งหมด " f"{len(payments)} รายการ")




# สรุปผลการจำลอง
successful = sum( e.status == "ลงทะเบียนสำเร็จ" for e in enrollments )

course_full = sum( e.status == "คอร์สเต็ม" for e in enrollments )

print("\n" + "=" * 60)
print("สรุปผลการจำลองข้อมูล")
print("=" * 60)
print("นักเรียนทั้งหมด       :", len(students))
print("การลงทะเบียนทั้งหมด  :", len(enrollments))
print("ลงทะเบียนสำเร็จ      :", successful)
print("ลงทะเบียนไม่ได้       :", course_full)
print("รายการชำระเงิน       :", len(payments))
print("=" * 60)