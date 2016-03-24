# _*_ coding:utf-8_*_


print sorted([36, 5, 12, 9, 21])


def reversed_cmp(x, y):
    if x > y:
        return -1
    elif x < y:
        return 1
    else:
        return 0


print sorted([36, 5, 12, 9, 21], reversed_cmp)

print sorted(['bob', 'about', 'Zoo', 'Credit'])


# task
def cmp_ignore_case(s1, s2):
    return cmp(s1.lower(), s2.lower())


print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)
