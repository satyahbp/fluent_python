colors = ['black', 'white']
sizes = ['S', 'M', 'L']

# Doesn't create the full thing in the memory
for tshrirt in (f"{c} {s}" for c in colors for s in sizes):
    print(tshrirt)