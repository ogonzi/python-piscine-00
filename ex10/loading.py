import time
import sys

def ft_progress(lst):
	start_time = time.time()
	iter_time = 0

	for i, item in enumerate(lst, 1):
		if (i == 1):
			iter_time = time.time() - start_time
		
		remaining_items = len(lst) - i
		percentage_done = i / len(lst)
		bar_filled = int(percentage_done * 25)
		bar_empty = 25 - bar_filled

		elapsed_time = time.time() - start_time
		eta = remaining_items * iter_time

		print(f"\rETA: {eta:5.2f}s [{percentage_done:>4.0%}] [{'=' * bar_filled}>{' ' * bar_empty}] {i}/{len(lst)} | elapsed time {elapsed_time:.2f}s", end="")

		yield item

def main():
	listy = range(1000)
	ret = 0
	for elem in ft_progress(listy):
		ret += (elem + 3) % 5
		time.sleep(0.01)
	print()
	print(ret)

if __name__ == "__main__":
	main()
