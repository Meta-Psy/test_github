large_list_with_duplicates = [1, "hello", True, [1, 2, 3], 2.5, 1, "world", False, [4, 5, 6], 3.5, 3, "foo", True, [7, 8, 9], 4.5, 4, "bar", False, [10, 11, 12], 5.5, 5, "baz", True, [13, 14, 15], 6.5, 1, "hello", True, [1, 2, 3], 2.5,1, "world", False, [4, 5, 6], 3.5, 3, "foo", True, [7, 8, 9], 4.5,4, "bar", False, [10, 11, 12], 5.5, 5, "baz", True, [13, 14, 15], 6.5, 6, "hello", False, [16, 17, 18], 7.5, 7, "world", True, [19, 20, 21], 8.5, 8, "foo", False, [22, 23, 24], 9.5, 9, "bar", True, [25, 26, 27], 10.5, 10, "baz", False, [28, 29, 30], 11.5, 6, "hello", False, [16, 17, 18], 7.5, 7, "world", True, [19, 20, 21], 8.5, 8, "foo", False, [22, 23, 24], 9.5, 9, "bar", True, [25, 26, 27], 10.5, 10, "baz", False, [28, 29, 30], 11.5]
without_duplicates = []
duplicates = []

for x in large_list_with_duplicates:
    if x not in without_duplicates:
        without_duplicates.append(x)
    else:
        duplicates.append(x)
print(without_duplicates)
print(duplicates)


