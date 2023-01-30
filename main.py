"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###

def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1

def test_linear_search():
	""" done. """
	assert linear_search([1,2,3,4,5], 5) == 4
	assert linear_search([1,2,3,4,5], 1) == 0
	assert linear_search([1,2,3,4,5], 6) == -1

def binary_search(mylist, key):
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
  while left <= right:   
    mid = (left+right) // 2

    if mylist[mid] < key:
      left = mid + 1
    elif mylist[mid] > key:
      right = mid - 1
    else:
      return mid
  return -1

def test_binary_search():
  assert binary_search([1,2,3,4,5], 5) == 4
  assert binary_search([1,2,3,4,5], 1) == 0
  assert binary_search([1,2,3,4,5], 2) == 1
  assert binary_search([1,2,3,4,5], 6) == -1
  assert binary_search([1,2,3,4,5], 3) == 2

def time_search(search_fn, mylist, key):
  time_start = time.time() * 1000
  search_fn(mylist, key)
  time_final = time.time() * 1000 - time_start
  return time_final

def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
  compare_list = []
  for i in range(len(sizes)):
    linear = time_search(linear_search, range(0, sizes[i]), -1)
    binary = time_search(binary_search, range(0, sizes[i]), -1)
    tuple = (sizes[i], linear, binary)
    compare_list.append(tuple)
  return compare_list

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'linear', 'binary'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_search():
	res = compare_search(sizes=[10, 100])
	print(res)
	assert res[0][0] == 10
	assert res[1][0] == 100
	assert res[0][1] < 1
	assert res[1][1] < 1

print_results(compare_search(sizes=[10, 100, 1000, 10000, 100000, 1000000]))