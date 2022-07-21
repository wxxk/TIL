with open('./data/00.txt', 'w', encoding='utf-8') as f:
        f.write('1회차 이상욱\n')
        f.write('Hello, python!\n')
        
        for i in range(1, 6):
            f.write (f'{i}일차 파이썬 공부 중\n')