# matplotlib : 과학계산용 그래프 라이브러리
# (선 그래프, 히스토그램, 산점도 등을 지원)

# 그래프를 그리기위해서는 matplotlib의 pyplot 모듈을 이용한다.

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6, 0.1)

y = np.sin(x)

plt.plot(x, y)
plt.show()