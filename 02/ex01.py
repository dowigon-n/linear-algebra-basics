# y = ax + b 일차 방정식 결정하기
from matplotlib import pyplot as plt

data_x = [2, 6]
data_y = [81, 91]

# 기울기 a 는  y값의 증가량 / x값의 증가량

#기울기
a = (data_y[1] - data_y[0]) / (data_x[1] - data_x[0])           # x변량, y변량
#b = data_y[1] - a * data_x[1]
b = data_y[0] - a * data_x[0]

# 결과

print(f'직선 y= {a}x + {b}')

# 그래프
fig, splt = plt.subplots()



# cf

x = [2, 4, 6, 8]
y1 = [81, 93, 91, 97]
y2 = [a * i + b for i in x]
splt.scatter(x, y1)
splt.plot(x, y2, 'r-')

plt.show()
