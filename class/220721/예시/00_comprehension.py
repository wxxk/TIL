# 리스트 컴프리핸션

even_list = [i**2 for i in range(10) if i % 2 == 0]
print(even_list)
print(sum([i**2 for i in range(10) if i % 2 == 0]))