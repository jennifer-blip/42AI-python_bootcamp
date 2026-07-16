import time

def ft_progress(lst) :
	total = len(lst)
	bar_size = 20
	start = time.perf_counter()
	for i, elem in enumerate(lst) :
		progress = (i + 1)/total
		percent = progress * 100
		elapsed = time.perf_counter() - start
		eta = elapsed / progress - elapsed
		filled = int(progress * bar_size)
		bar = "=" * filled + ">" + " " * (bar_size - filled - 1)
		print (f"\r ETA : {eta:.1f}s [{bar}] | {percent:.1f}% | elapsed time : {elapsed:.1f}s", end="")
		yield elem



listy = range(1000)
ret = 0
for elem in ft_progress(listy):
	ret += (elem + 3) % 5
	time.sleep(0.01)
print()
print(ret)

listy = range(3333)
ret = 0
for elem in ft_progress(listy):
	ret += elem
	time.sleep(0.005)
print()
print(ret)