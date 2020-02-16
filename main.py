import time
import random


codes = [31, 32, 33, 34, 35, 36, 37, 91, 92, 93, 94, 95, 96, 97]
a = ord('А')  # Здесь русская А
print()


def sss(i):
    time.sleep(0.3)
    res = f'{chr(155)}{random.choice(codes)}m{chr(i)}'
    return res


for i in range(a, a + 32):
    res = sss(i)
    print(res, end=' ', flush=True)
print('\x1b[0m')
