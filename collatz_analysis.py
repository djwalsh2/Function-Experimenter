import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys
# pd.set_option('display.max_columns', 999)
# pd.set_option('display.max_rows', 999)

"""
Redirect Standard Output To Text File
"""
file = "master.txt"
sys.stdout = open(file, 'wt')


"""
Open CSV
"""
csv_file = "master.csv"
df = pd.read_csv(csv_file, delimiter=",")

"""
Define Columns To Correlate
"""
primary_prefix = "x0"
secondary_prefix = "x5"
all_prefix = "x"

primary_columns = [col for col in df if col.startswith(primary_prefix)]
secondary_columns = [col for col in df if col.startswith(secondary_prefix)]
all_columns = [col for col in df if col.startswith(all_prefix)]
columns = primary_columns + secondary_columns
#columns = all_columns  # uncomment if we want all columns to be correlated

"""
Print Data Frame
"""
print("Data Frame")
print(df[columns])
print()

"""
Print Correlation Matrix
"""
print("Correlation Matrix")
print(df[columns].corr())
print()

"""
Get Redundant Pairs
"""
def get_redundant_pairs(df):
    '''Get diagonal and lower triangular pairs of correlation matrix'''
    pairs_to_drop = set()
    cols = df.columns
    for i in range(0, df.shape[1]):
        for j in range(0, i+1):
            pairs_to_drop.add((cols[i], cols[j]))
    return pairs_to_drop

def get_top_abs_correlations(df, n=5):
    au_corr = df[columns].corr().abs().unstack()
    labels_to_drop = get_redundant_pairs(df)
    au_corr = au_corr.drop(labels=labels_to_drop).sort_values(ascending=False)
    return au_corr[0:n]

"""
Get Top Absolute Correlations
"""
number_of_correlations = 10
print("Top " + str(number_of_correlations) + " Absolute Correlations")
print(get_top_abs_correlations(df[columns], number_of_correlations))


"""
Generate Seaborn Heatmap
"""
plt.figure(figsize=(15, 15))
plt.title("Correlation Matrix of Bit's Between Iterations", size="24")
corr = df[columns].corr()
sns.heatmap(corr,
            cmap="Purples",
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values)
sns.set_style("ticks", {"font.size": 12,
                        "font.family": "Arial",
                        "xtick.major.size": 4,
                        "ytick.major.size": 4}
              )
sns.set(font_scale=2)
sns.set_context("poster")
plt.show()

