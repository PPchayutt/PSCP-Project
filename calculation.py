"""เก็บฟังก์ชันคำนวณทั้งหมด"""

# ฟังก์ชันแปลงอายุของสัตว์
def dog_to_human_age(dog_age):
    """แปลงอายุสุนัข"""
    if dog_age <= 2:
        return dog_age * 10.5
    else:
        return 21 + (dog_age - 2) * 4

def cat_to_human_age(cat_age):
    """แปลงอายุแมว"""
    age_table = {
        0: 0, 1: 15, 2: 24, 3: 28, 4: 32, 5: 36, 6: 40, 7: 44, 8: 48, 9: 52, 10: 56,
        11: 60, 12: 64, 13: 68, 14: 72, 15: 76, 16: 80, 17: 84, 18: 88,
        19: 92, 20: 96, 21: 100, 22: 104, 23: 108, 24: 112, 25: 116
    }
    return age_table.get(cat_age, 116)

def bunny_to_human_age(bunny_age):
    """แปลงอายุกระต่าย"""
    age_table = {
        0: 0, 1: 21, 2: 27, 3: 33, 4: 39, 5: 45, 6: 51, 7: 57, 8: 63, 9: 69,
        10: 75, 11: 81, 12: 87, 13: 93, 14: 99, 15: 105, 16: 110
    }
    return age_table.get(bunny_age, 110)

def hamster_to_human_age(hamster_age):
    """แปลงอายุแฮมสเตอร์"""
    age_table = {
        0: 0,
        1: 41,
        1.5: 52.5,
        2: 63.5,
        2.5: 74.5,
        3: 80
    }
    closest_age = min(age_table.keys(), key=lambda x: abs(x - hamster_age))
    return age_table[closest_age]

def hedgehog_to_human_age(hedgehog_age):
    """แปลงอายุเม่น"""
    age_table = {
        0: 0,
        1.17: 30,
        3: 40,
        3.5: 50,
        3.67: 60,
        4.17: 70,
        5.33: 80,
        6.17: 90,
        7.67: 100
    }
    closest_age = min(age_table.keys(), key=lambda x: abs(x - hedgehog_age))
    return age_table[closest_age]

def squirrel_to_human_age(squirrel_age):
    """แปลงอายุกระรอก"""
    age_table = {
        0: 0, 1: 8.89, 2: 17.78, 3: 26.67, 4: 35.56, 5: 44.45,
        6: 53.34, 7: 62.23, 8: 71.12, 9: 80.01, 10: 88.9,
        11: 97.79, 12: 106.68, 13: 115.57, 14: 124.46, 15: 133.35,
        16: 142.24, 17: 151.13, 18: 160.02, 19: 168.91, 20: 177.8,
        21: 186.69, 22: 195.58, 23: 204.47
    }
    return age_table.get(squirrel_age, 204.47)

# ฟังก์ชันช่วยสำหรับดูช่วงวัยของสัตว์
def get_dog_life_stage(age):
    """คำนวณช่วงวัยสุนัข"""
    if age < 1:
        return "🐕 Puppy (แรกเกิดถึง 1 ปี)\nช่วงวัยเด็ก การเจริญเติบโตและพัฒนาการสูง"
    elif 1 <= age <= 8:
        return "🐕 Adult (1-8 ปี)\nช่วงวัยผู้ใหญ่ แข็งแรงสมบูรณ์"
    else:
        return "🐕 Senior (มากกว่า 8 ปี)\nช่วงวัยชรา ต้องการการดูแลเป็นพิเศษ"

def get_cat_life_stage(age):
    """คำนวณช่วงวัยแมว"""
    stages = {
        (0, 1): "🐱 Kitten (แรกเกิดถึง 1 ปี)\nช่วงวัยเด็ก การเจริญเติบโตและพัฒนาการสูง",
        (1, 2.5): "🐱 Junior (1-2 ปี)\nช่วงวัยรุ่น เต็มไปด้วยพลังและความกระตือรือร้น",
        (3, 6.5): "🐱 Prime (3-6 ปี)\nช่วงวัยผู้ใหญ่ สมบูรณ์แข็งแรงที่สุด",
        (7, 10.5): "🐱 Mature (7-10 ปี)\nช่วงวัยกลางคน เริ่มมีการเปลี่ยนแปลงทางร่างกาย",
        (11, 14.5): "🐱 Senior (11-14 ปี)\nช่วงวัยสูงอายุ ต้องการการดูแลเป็นพิเศษ",
        (15, 100): "🐱 Geriatric (15 ปีขึ้นไป)\nช่วงวัยชรา ต้องการการดูแลอย่างใกล้ชิด"
    }
    for (min_age, max_age), description in stages.items():
        if min_age <= age < max_age:
            return description
    return stages[(15, 100)]  # ถ้าไม่อยู่ในช่วงไหนเลย ให้ถือว่าเป็นวัยชรา
