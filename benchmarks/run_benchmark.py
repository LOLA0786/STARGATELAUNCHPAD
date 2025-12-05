import time, csv

models = ["Stargate", "Grok-4"]
prompts = ["Hello"]

rows = []
for m in models:
    for p in prompts:
        start = time.time()
        time.sleep(0.3)
        rows.append([m, p, time.time() - start])

with open("results.csv", "w") as f:
    csv.writer(f).writerows(rows)

print("results.csv saved")
