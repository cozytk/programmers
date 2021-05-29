def solution(phone_book):
    hash_book = set(phone_book)
    for h in hash_book:
        temp = ""
        for i in h:
            temp += i
            if (temp in hash_book and temp != h):
                return False
    return True

