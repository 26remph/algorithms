def merge(array, lf, mid, rg):

	left = array[lf: mid]
	right = array[mid: rg]

	result = [None] * len(array)
	l, r, k = 0, 0, 0

	while l < len(left) and r < len(right):
		if left[l] <= right[r]:
			result[k] = left[l]
			l += 1
		else:
			result[k] = right[r]
			r += 1
		k += 1

	while l < len(left):
		result[k] = left[l]
		l += 1
		k += 1
	while r < len(right):
		result[k] = right[r]
		r += 1
		k += 1

	return result


def merge_sort(array, lf, rg):
	array = array[lf: rg]

	if len(array) == 1:
		return array

	left = merge_sort(array[0: len(array) // 2], lf, rg)
	right = merge_sort(array[len(array) // 2: len(array)], lf, rg)

	return merge(left + right, 0, len(left), len(array))


def test():
	a = [1, 4, 9, 2, 10, 11]
	b = merge(a, 0, 3, 6)
	expected = [1, 2, 4, 9, 10, 11]
	assert b == expected
	c = [1, 4, 2, 10, 1, 2]
	c = merge_sort(c, 0 , 6)
	# c = merge_sort(c, 0 , 5)
	# print('c', c)
	expected = [1, 1, 2, 2, 4, 10]
	# expected = [1, 1, 2, 4, 10]
	assert c == expected

test()