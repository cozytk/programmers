def solution(new_id):
    new_id = new_id.lower()
    tmp = ''
    for n in new_id:
        if n.islower() or n.isdigit() or n == '-' or n == '_' or n == '.':
            tmp += n
    new_id = tmp
    i = 0
    tmp = ''
    while i < len(new_id):
        if new_id[i] == '.':
            while i < len(new_id) and new_id[i] == '.':
                i += 1
            tmp += '.'
        else:
            tmp += new_id[i]
            i += 1
    new_id = tmp
    if new_id.startswith('.'):
        new_id = new_id[1:]
    if new_id.endswith('.'):
        new_id = new_id[:-1]
    if new_id == '':
        new_id = 'a'
    if len(new_id) > 15:
        new_id = new_id[:15]
    if new_id.endswith('.'):
        new_id = new_id[:-1]
    if len(new_id) == 1:
        new_id = new_id * 3
    if len(new_id) == 2:
        new_id = new_id + new_id[1]
    answer = new_id
    return answer