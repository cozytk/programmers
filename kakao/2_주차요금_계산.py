import math

def solution(fees, records):
    answer = []
    b_time, b_cost, u_time, u_cost = fees
    db = {}
    for r in records:
        key = r[6:10]
        time = int(r[0:2] + r[3:5])
        time = time // 100 * 60 + time % 100
        IN = True if r[-2:] == 'IN' else False
        if key not in db.keys() and IN:
            db[key] = (0, time, IN)
        elif IN:
            db[key] = (db[key][0], time, IN)
        else:
            db[key] = (db[key][0] + time - db[key][1], time, IN)

    for key, (total, time, IN) in db.items():
        if IN:
            db[key] = (total + 23 * 60 + 59 - time, time, False)
        total = db[key][0]
        if total <= b_time:
            db[key] = b_cost
        else:
            db[key] = b_cost + math.ceil((total - b_time) / u_time) * u_cost


    for _, v in sorted(db.items(), key=lambda x: x[0]):
        answer.append(v)
    return answer