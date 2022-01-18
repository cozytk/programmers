import math

def solution(fees, records):
    answer = []
    db = {}
    b_time, b_cost, u_time, u_cost = fees
    for r in records:
        time, key, IO = r.split()
        h, m = time.split(':')
        time = h * 60 + m
        if key not in db.keys() and IO == 'IN':
            db[key] = (0, time, IO)
        elif IO == 'IN':
            db[key] = (db[key][0], time, IO)
        else:
            db[key] = (db[key][0] + time - db[key][1], time, IO)

    for key, (total, time, IO) in db.items():
        if IO == 'IN':
            db[key] = (total + 23 * 60 + 59 - time, time, False)
        total = db[key][0]
        if total <= b_time:
            db[key] = b_cost
        else:
            db[key] = b_cost + math.ceil((total - b_time) / u_time) * u_cost


    for _, v in sorted(db.items(), key=lambda x: x[0]):
        answer.append(v)
    return answer