data = [file.strip() for file in open('input.txt')]

results = []
for reindeer in ('\n'.join(data)).split('\n\n'):
    q = 0
    for x in reindeer.split('\n'):
        q += int(x)
    results.append(q)
results = sorted(results)
print("first answer", results[-1])
print("second answer", results[-1]+results[-2]+results[-3])
    
        