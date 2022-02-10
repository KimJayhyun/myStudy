from sklearn.datasets import load_iris

irisData = load_iris()


# load_iris() 함수가 리턴하는 객체는 Bunch 클래스 객체
# Dictionary 와 유사한 객체 

print(irisData.keys())

i = 0 
for data in irisData['data']:
    print(data) 
    i += 1

    if i> 10:
        break

print(irisData['feature_names'])

