import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
 
sample_data = {
    'name': ['John', 'Alia', 'Ananya', 'Steve', 'Ben'],
    'age': [24, 22, 23, 25, 28],  
    'communication_skill_score': [85, 70, 75, 90, 90],
    'quantitative_skill_score': [80, 90, 80, 75, 70]
}
 
df = pd.DataFrame(sample_data)
 
df.cov(numeric_only=True)


# Calculate the covariance matrix
cov_matrix = df.cov(numeric_only=True)

# Create a heatmap to visualize the covariance matrix
plt.figure(figsize=(10, 8))
sns.heatmap(cov_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Covariance Matrix Heatmap')
plt.show()