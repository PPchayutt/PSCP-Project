# เก็บฟังก์ชันคำนวณทั้งหมด
def dog_to_human_age(dog_age):
    if dog_age <= 2:
        return dog_age * 10.5
    else:
        return 21 + (dog_age - 2) * 4

def cat_to_human_age(cat_age):
    age_table = {
        0: 0, 1: 15, 2: 24, 3: 28, 4: 32, 5: 36, 6: 40, 7: 44, 8: 48, 9: 52, 10: 56,
        11: 60, 12: 64, 13: 68, 14: 72, 15: 76, 16: 80, 17: 84, 18: 88,
        19: 92, 20: 96, 21: 100, 22: 104, 23: 108, 24: 112, 25: 116
    }
    return age_table.get(cat_age, 116)

def bunny_to_human_age(bunny_age):
    age_table = {
        0: 0, 1: 21, 2: 27, 3: 33, 4: 39, 5: 45, 6: 51, 7: 57, 8: 63, 9: 69,
        10: 75, 11: 81, 12: 87, 13: 93, 14: 99, 15: 105, 16: 110
    }
    return age_table.get(bunny_age, 110)

def hamster_to_human_age(hamster_age):
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
    if age < 1:
        return "🐕 Puppy (แรกเกิดถึง 1 ปี)\nช่วงวัยเด็ก การเจริญเติบโตและพัฒนาการสูง"
    elif 1 <= age <= 8:
        return "🐕 Adult (1-8 ปี)\nช่วงวัยผู้ใหญ่ แข็งแรงสมบูรณ์"
    else:
        return "🐕 Senior (มากกว่า 8 ปี)\nช่วงวัยชรา ต้องการการดูแลเป็นพิเศษ"

def get_cat_life_stage(age):
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
def calculate_hamster_age(self):
        hamster_age = self.spinBox_4.value()
        human_age = hamster_to_human_age(hamster_age)
    
        result = f"""
        <div style='background-color: #FFF8DC; padding: 20px; border-radius: 10px;'>
            <h2 style='color: #B87333;'>🐹 ผลการคำนวณ</h2>
            <p style='font-size: 16px; margin: 10px 0;'>
                <b>อายุแฮมสเตอร์:</b> {hamster_age:.1f} ปี<br>
                <b>เทียบเท่าอายุคน:</b> {human_age:.1f} ปี
            </p>
        </div>
        """
    
        info = f"""
        <div style='background-color: #FFF8DC; padding: 20px; border-radius: 10px;'>
            <h2 style='color: #B87333;'>📊 ข้อมูลเพิ่มเติม</h2>
            <p style='font-size: 16px; margin: 10px 0;'>
                แฮมสเตอร์มีช่วงอายุเฉลี่ย 2-3 ปี<br>
                โดยแบ่งเป็น 4 ช่วงวัย:<br>
                🐹 ช่วงวัยเด็ก (0-3 เดือน)<br>
                🐹 ช่วงวัยรุ่น (3-6 เดือน)<br>
                🐹 ช่วงโตเต็มวัย (6 เดือน - 1 ปี)<br>
                🐹 ช่วงวัยชรา (1 ปีขึ้นไป)
            </p>
        </div>
        """
    
        self.textBrowser_8.setHtml(result)
        self.textBrowser_9.setHtml(info)

def calculate_hedgehog_age(self):
        hedgehog_age = self.spinBox_5.value()
        human_age = hedgehog_to_human_age(hedgehog_age)
    
        result = f"""
        <div style='background-color: #FFF8DC; padding: 20px; border-radius: 10px;'>
            <h2 style='color: #B87333;'>🦔 ผลการคำนวณ</h2>
            <p style='font-size: 16px; margin: 10px 0;'>
                <b>อายุเม่น:</b> {hedgehog_age:.1f} ปี<br>
                <b>เทียบเท่าอายุคน:</b> {human_age:.1f} ปี
            </p>
        </div>
        """

        info = f"""
        <div style='background-color: #FFF8DC; padding: 20px; border-radius: 10px;'>
            <h2 style='color: #B87333;'>📊 ข้อมูลเพิ่มเติม</h2>
            <p style='font-size: 16px; margin: 10px 0;'>
                เม่นมีช่วงชีวิต 4 ระยะ:<br>
                🦔 ช่วงวัยเด็ก (0-6 เดือน)<br>
                🦔 ช่วงวัยรุ่น (6 เดือน - 1 ปี)<br>
                🦔 ช่วงโตเต็มวัย (1-4 ปี)<br>
                🦔 ช่วงวัยชรา (4 ปีขึ้นไป)
            </p>
        </div>
        """

        self.textBrowser_11.setHtml(result)
        self.textBrowser_12.setHtml(info)

def calculate_bunny_age(self):
        bunny_age = self.spinBox_6.value()
        human_age = bunny_to_human_age(bunny_age)
    
        result = f"""
        <div style='background-color: #FFF8DC; padding: 20px; border-radius: 10px;'>
            <h2 style='color: #B87333;'>🐰 ผลการคำนวณ</h2>
            <p style='font-size: 16px; margin: 10px 0;'>
                <b>อายุกระต่าย:</b> {bunny_age:.1f} ปี<br>
                <b>เทียบเท่าอายุคน:</b> {human_age:.1f} ปี
            </p>
        </div>
        """
    
        info = f"""
        <div style='background-color: #FFF8DC; padding: 20px; border-radius: 10px;'>
            <h2 style='color: #B87333;'>📊 ข้อมูลเพิ่มเติม</h2>
            <p style='font-size: 16px; margin: 10px 0;'>
                🐰 กระต่ายสามารถมีอายุยืนได้ถึง 16 ปี<br>
                🐰 ซึ่งเทียบเท่ากับอายุคน 110 ปี
            </p>
        </div>
        """
    
        self.textBrowser_14.setHtml(result)
        self.textBrowser_15.setHtml(info)

def calculate_squirrel_age(self):
        squirrel_age = self.spinBox_7.value()
        human_age = squirrel_to_human_age(squirrel_age)
        result = f"""
        <div style='background-color: #FFF8DC; padding: 20px; border-radius: 10px;'>
            <h2 style='color: #B87333;'>🐿️ ผลการคำนวณ</h2>
            <p style='font-size: 16px; margin: 10px 0;'>
                <b>อายุกระรอก:</b> {squirrel_age:.1f} ปี<br>
                <b>เทียบเท่าอายุคน:</b> {human_age:.1f} ปี
            </p>
        </div>
        """

        info = f"""
        <div style='background-color: #FFF8DC; padding: 20px; border-radius: 10px;'>
            <h2 style='color: #B87333;'>📊 ข้อมูลเพิ่มเติม</h2>
            <p style='font-size: 16px; margin: 10px 0;'>
                🐿️ กระรอกในธรรมชาติมีอายุเฉลี่ย 6-12 ปี<br>
                🐿️ แต่ในการเลี้ยงดูที่ดีสามารถมีอายุได้ถึง 23 ปี<br>
                🐿️ ซึ่งเทียบเท่ากับอายุคนประมาณ 204 ปี
            </p>
        </div>
        """

        self.textBrowser_17.setHtml(result)
        self.textBrowser_18.setHtml(info)