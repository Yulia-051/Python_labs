# TODO Найдите количество книг, которое можно разместить на дискете

conversion = 1024
max_memory_kb = 1.4 * conversion ** 2
count_pages = 100
cnt_strPage = 50
cnt_symStr = 25
sym_bytes = 4
print("Количество книг, помещающихся на дискету:",
      round(max_memory_kb / (count_pages * cnt_strPage * cnt_symStr * sym_bytes)))
