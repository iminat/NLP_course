from sklearn.datasets import load_digits
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# Load the Digits dataset
digits = load_digits()

# Perform hierarchical clustering
clustering = AgglomerativeClustering(n_clusters=6)
clusters = clustering.fit_predict(digits.data)

# Compare clusters with actual categories
for i in range(len(digits.target)):
    print(f"Image {i+1}: Predicted Cluster {clusters[i]}, Actual Category {digits.target[i]}")

# Plot the truncated dendrogram
plt.figure(figsize=(10, 6))
Z = linkage(digits.data, method='ward')
dendrogram(Z, truncate_mode='level', p=6)
plt.xlabel('Samples')
plt.ylabel('Distance')
plt.title('Truncated Dendrogram')
plt.show()