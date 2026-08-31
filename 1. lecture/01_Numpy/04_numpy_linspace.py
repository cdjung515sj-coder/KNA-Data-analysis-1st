import numpy as np

# np.linspace(시작, 끝, 개수)
# 개수 중심 균등 분할
# 시작과 끝 구간을 지정한 개수만큼 정확히 나뉨
# 간격은 알아서 계산하도록 함

# 0부터 1까지 5개로 균등 분할
div_five = np.linspace(0, 1, 5)  # [0.   0.25 0.5  0.75 1.  ]
print(div_five)
