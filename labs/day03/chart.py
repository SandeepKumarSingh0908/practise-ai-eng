import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales  = [120, 135, 128, 180, 175, 210]

plt.figure(figsize=(6, 3.5))
plt.bar(months, sales)
plt.title("Monthly sales (units)")
plt.ylabel("Units")
plt.tight_layout()
plt.savefig("chart.png", dpi=100)

with open("chart.csv", "w") as f:
    f.write("month,units\n")
    for m, s in zip(months, sales):
        f.write(f"{m},{s}\n")
print("wrote chart.png and chart.csv")
