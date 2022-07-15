def merge(arr, lf, mid, rg):
	# -------- foregin code -------
	# y = arr[lf: mid]
	# z = arr[mid: rg]
	# k = lf
	# while (len(y) > 0) and (len(z) > 0):
	# 	if y[0] > z[0]:
	# 		arr[k] = z.pop(0)
	# 	else:
	# 		arr[k] = y.pop(0)
	# 	k += 1
	#
	# for i in range(len(z)):
	# 	arr[k + i] = z[i]
	# for i in range(len(y)):
	# 	arr[k + i] = y[i]
	# return arr[lf:rg]
	# --------- end ----------

	# --------- my code ------
	left = arr[lf: mid]
	right = arr[mid: rg]

	# result = [None] * len(arr)
	l, r, k = 0, 0, lf
	print('lf, mid, rg:', lf, mid, rg)
	while l < len(left) and r < len(right):
		if left[l] <= right[r]:
			arr[k] = left[l]
			# result[k] = left[l]
			l += 1
		else:
			arr[k] = right[r]
			# result[k] = right[r]
			r += 1
		k += 1

	while l < len(left):
		arr[k] = left[l]
		# result[k] = left[l]
		l += 1
		k += 1
	while r < len(right):
		# result[k] = right[r]
		arr[k] = right[r]
		r += 1
		k += 1

	return arr[lf:rg]
	# ---------- end my -----------

def merge_sort(arr, lf, rg):

	# ------- work code -----------
	# if len(arr[lf:rg]) < 2:
	# 	return arr[lf:rg]
	# mid = lf + (rg - lf) // 2
	# merge_sort(arr, lf, mid)
	# merge_sort(arr, mid, rg)
	# return merge(arr, lf, mid, rg)
	# ------- end work code -----------


	# array = array[lf: rg]
	print(arr, id(arr))
	# if len(arr[lf:rg]) == 1:
	if len(arr[lf:rg]) == 1:
		return arr[lf:rg]

	# mid = lf + (rg - lf)//2
	mid = lf + len(arr[lf:rg]) // 2
	# print('m, m1:', mid, mid_1)
	# print('lf, rg:', lf, rg)

	# print('mid', mid)
	# left = merge_sort(arr, lf, mid)
	merge_sort(arr, lf, mid)
	# left = merge_sort(arr[0: len(arr) // 2], lf, rg)
	# print('left', left)
	# right = merge_sort(arr, mid, rg)
	merge_sort(arr, mid, rg)
	# right = merge_sort(arr[len(arr) // 2: len(arr)], lf, rg)
	# print('l,r:', left, right)

	return merge(arr, lf, mid, rg)

def test():
	a = [1, 4, 9, 2, 10, 11]
	b = merge(a, 0, 3, 6)
	expected = [1, 2, 4, 9, 10, 11]
	assert b == expected

	c = [1, 4, 2, 10, 1, 2]
	print(c, id(c))
	merge_sort(c, 0, 6)
	print(c, id(c))
	expected = [1, 1, 2, 2, 4, 10]
	assert c == expected


if __name__ == '__main__':
	test()
