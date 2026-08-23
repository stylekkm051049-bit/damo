ส่วนที่ 2 — เตรียม class
ระบบประกอบด้วย 4 Class หลัก ได้แก่ Student, Course, Enrollment และ Payment

แต่ละ Class มี Attribute สำหรับเก็บข้อมูล และ Method สำหรับการทำงานของระบบจริง


import random
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

random.seed(11)
print("เตรียม Library เรียบร้อยแล้ว")