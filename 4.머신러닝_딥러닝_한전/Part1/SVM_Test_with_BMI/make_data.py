import random
import os

def bmi_func(height, weight):
    bmi = weight / (height / 100) ** 2
    if bmi < 18.5: return "저체중"
    elif bmi > 25 : return "비만"
    else : return "정상"
    
csvPath = os.getcwd()
csvPath += '\\머신러닝_딥러닝\\Part1\\SVM_Test_with_BMI\\bmi.csv'

fp = open(csvPath, 'w', encoding='utf-8')

fp.write("height,weight,label\n")

# 데이터 생성하기

cnt = {"저체중" : 0, "정상" : 0, "비만" : 0}

for i in range(10000):
    h = random.randint(120, 200)
    w = random.randint(35, 90)
    bmi = bmi_func(h, w)

    cnt[bmi] += 1
    fp.write("{},{},{}\n".format(h,w,bmi))

fp.close()

print(cnt)
