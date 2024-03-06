from collections import deque
import collections

# 初始化双向队列
deque: deque[int] = collections.deque()
# 元素入队
deque.append(2)  # 添加至队尾
deque.append(5)
deque.append(4)
deque.appendleft(3)  # 添加至队首
deque.appendleft(1)
# 访问元素
front: int = deque[0]  # 队首元素
rear: int = deque[-1]  # 队尾元素
# 元素出队
pop_front: int = deque.popleft()  # 队首元素出队
pop_rear: int = deque.pop()  # 队尾元素出队
# 获取双向队列的长度
size: int = len(deque)
# 判断双向队列是否为空
is_empty: bool = len(deque) == 0
