import csv
from sklearn.ensemble import IsolationForest

data = []

with open('/home/tsub/ais-2026/lab1_CS/data/ssh_attempts.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        minute = int(row['minute'])
        ssh_failures = int(row['ssh_failures'])
        data.append((minute, ssh_failures))

values = [[row[1]] for row in data]

model = IsolationForest(random_state=42, contamination=0.10)
model.fit(values)

results = model.predict(values)

print("Anomaly detection for SSH failures per minute")
print()

anomaly_count = 0

for (minute, ssh_failures), result in zip(data, results):
    status = "ANOMALY" if result == -1 else "normal"
    print(f"Minute {minute}: {ssh_failures} failed SSH attempts -> {status}")
    if result == -1:
        anomaly_count += 1

print()
print("Summary:")
print(f"Minutes analyzed: {len(data)}")
print(f"Anomalies found: {anomaly_count}")

if anomaly_count > 0:
    print("Conclusion: The script found unusual behavior in the data.")
else:
    print("Conclusion: No clear anomalies were found in the data.")
