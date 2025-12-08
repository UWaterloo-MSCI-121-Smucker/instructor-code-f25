# working versions of unique

def unique(alist):
    if len(alist) <= 1:
        return alist.copy()
    result = list()
    for elt in alist:
        found = False
        for i in range(len(result)):
            if elt == result[i]:
                found = True
        if not found:
            result.append(elt)
    return result


def contains( alist, test_elt):
    for elt in alist:
        if test_elt == elt:
            return True
    return False

def unique(alist):
    if len(alist) <= 1:
        return alist.copy()
    result = list()
    for elt in alist:
        if not contains(result, elt):
            result.append(elt)
    return result


def unique(alist):
    if len(alist) <= 1:
        return alist.copy()
    result = list()
    for elt in alist:
        if elt not in result:
            result.append(elt)
    return result


def unique(alist):
    if len(alist) <= 1:
        return alist.copy()
    result = list()
    slist = sorted(alist)
    prev = slist[0]
    result.append(prev)
    for i in range(1,len(slist)):
        curr = slist[i]
        if curr != prev:
            result.append(curr)
        prev = curr
    return result


def unique(alist):
    result = alist.copy()
    i = 0
    while i < len(result):
        j = i + 1
        while j < len(result):
            if result[j] == result[i]:
                result.pop(j)
            else:
                j += 1
        i += 1
    return result


def unique(alist):
    result = alist.copy()
    for i in range(len(result)):
        j = len(result) - 1
        while j > i:
            if result[j] == result[i]:
                result.pop(j)
            j -= 1
    return result
