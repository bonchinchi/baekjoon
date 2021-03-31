d = str(input())
if d.islower() and len(d)>=3 and len(d)<=99:
    output=[d[start:start+int(len(d)/3)] for start in range(0, len(d), int(len(d)/3))]
    print(max(set(output), key=output.count))