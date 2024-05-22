"""Functions used in several files.
"""
import matplotlib.pyplot as plt

def visualize_features(df):
    """_summary_

    Args:
        df (_type_): _description_
    """
    # Number of features
    num_features = df.shape[1]

    # Determine the grid size
    rows = (num_features + 4) // 5
    cols = 5

    # Create the subplots
    fig, axes = plt.subplots(rows, cols, figsize=(20, 4 * rows))
    axes = axes.flatten()

    idx = 0
    # Plot each feature in a subplot
    for idx, col in enumerate(df.columns):
        axes[idx].hist(df[col].dropna(), bins=30)
        axes[idx].set_title(col)

    # Remove empty subplots
    for idx2 in range(idx+1, len(axes)):
        fig.delaxes(axes[idx2])

    plt.tight_layout()
    plt.show()


def visualize_feature(df, column_name):
    """Plots a histogram of the specified column in the given DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.
    column_name (str): The name of the column to plot.
    """
    # Check if the column exists in the DataFrame
    if column_name not in df.columns:
        print(f"Column '{column_name}' does not exist in the DataFrame.")
        return

    # Plot the histogram of the specified column
    plt.figure(figsize=(10, 6))
    plt.hist(df[column_name].dropna(), bins=30, edgecolor='k')
    plt.title(f'Histogram of {column_name}')
    plt.xlabel(column_name)
    plt.ylabel('Frequency')
    plt.show()
