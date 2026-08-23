ส่วนที่ 2 — เตรียม class
ระบบประกอบด้วย 4 Class หลัก ได้แก่ Student, Course, Enrollment และ Payment

แต่ละ Class มี Attribute สำหรับเก็บข้อมูล และ Method สำหรับการทำงานของระบบจริง


import random
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

random.seed(11)
print("เตรียม Library เรียบร้อยแล้ว")

class Student:
    def __init__(self, student_id, name, gender, age, grade, school, phone):
        self.student_id = student_id
        self.name = name
        self.gender = gender
        self.age = age
        self.grade = grade
        self.school = school
        self.phone = phone

    def get_grade(self):
        return self.grade
class Course:
    def __init__(self, course_id, course_name, subject, teacher, price, capacity):
        self.course_id = course_id
        self.course_name = course_name
        self.subject = subject
        self.teacher = teacher
        self.price = price
        self.capacity = capacity
        self.enrolled_count = 0

    def has_seat(self):
        return self.enrolled_count < self.capacity

    def add_student(self):
        if self.has_seat():
            self.enrolled_count += 1
            return True
        return False

    def available_seats(self):
        return self.capacity - self.enrolled_count


class Enrollment:
    def __init__(
        self,
        enrollment_id,
        student,
        course,
        enroll_date,
        discount_rate=0
    ):
        self.enrollment_id = enrollment_id
        self.student = student
        self.course = course
        self.enroll_date = enroll_date
        self.discount_rate = discount_rate
        self.total_tuition = 0
        self.status = "รอตรวจสอบ"

    def calculate_total(self):
        discount = self.course.price * self.discount_rate
        self.total_tuition = round(
            self.course.price - discount,
            2
        )
        return self.total_tuition

    def confirm(self):
        if self.course.add_student():
            self.status = "ลงทะเบียนสำเร็จ"
            self.calculate_total()
            return True

        self.status = "คอร์สเต็ม"
        return False


class Payment:
    def __init__(
        self,
        payment_id,
        enrollment,
        payment_date,
        method
    ):
        self.payment_id = payment_id
        self.enrollment = enrollment
        self.payment_date = payment_date
        self.amount = enrollment.total_tuition
        self.method = method
        self.status = "ชำระเงินแล้ว"

    def record_payment(self):
        return self.status


print("สร้าง Class ทั้ง 4 Class สำเร็จ")