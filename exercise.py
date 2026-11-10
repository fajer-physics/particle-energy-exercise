import matplotlib.pyplot as plt


energies_gev = [12.5, 47.3, 85.0, 33.8, 61.2, 95.4, 24.1, 72.6, 55.9, 40.0]

print("Number of values:", len(energies_gev))
print("Minimum energy:", min(energies_gev), "GeV")
print("Maximum energy:", max(energies_gev), "GeV")

threshold_gev = 50.0
selected_loop = []
for energy in energies_gev:
    if energy > threshold_gev:
        selected_loop.append(energy)
print(f"Loop selection (> {threshold_gev} GeV):", selected_loop)



def select_above(data, threshold):
    """Return the values in data that are greater than threshold."""
    result = []
    for x in data:
        if x > threshold:
            result.append(x)
    return result


selected_func = select_above(energies_gev, threshold_gev)
print("Function selection:", selected_func)


new_threshold_gev = 70.0
selected_new = select_above(energies_gev, new_threshold_gev)
print(f"Selected above {new_threshold_gev} GeV:", selected_new)
print("Count at 50 GeV:", len(selected_func), "| Count at 70 GeV:", len(selected_new))


fig, axes = plt.subplots(1, 2, figsize=(11, 4))

axes[0].hist(energies_gev, bins=5, range=(0, 100), edgecolor="black")
axes[0].axvline(threshold_gev, color="red", linestyle="--",
                label=f"Threshold = {threshold_gev:.0f} GeV")
axes[0].set_xlabel("Energy [GeV]")
axes[0].set_ylabel("Entries per bin")
axes[0].set_title("5 bins (width 20 GeV)")
axes[0].legend()

axes[1].hist(energies_gev, bins=20, range=(0, 100), edgecolor="black")
axes[1].axvline(new_threshold_gev, color="red", linestyle="--",
                label=f"Threshold = {new_threshold_gev:.0f} GeV")
axes[1].set_xlabel("Energy [GeV]")
axes[1].set_ylabel("Entries per bin")
axes[1].set_title("20 bins (width 5 GeV)")
axes[1].legend()

fig.suptitle("Ten artificial particle energies")
fig.tight_layout()
fig.savefig("figure.png", dpi=150)
plt.show()

