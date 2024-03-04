import pandas as pd
import matplotlib.pyplot as plt

from io import StringIO
from wordcloud import WordCloud


def get_color(value, high_threshold = 95, low_threshold = 40):
    if value > high_threshold:
        return 'red'
    if value > low_threshold:
        return 'orange'

    return 'blue'


def plot_counts(value_counts, high_threshold, low_threshold):
    sorted_counts = value_counts.sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    bars = plt.bar(sorted_counts.index, sorted_counts)
    plt.xlabel('Columns')
    plt.ylabel('Counts')
    plt.title('Counts in Each Column')
    plt.xticks(rotation=90)
    plt.grid(which='both', linestyle='--', linewidth=0.5, zorder=0)

    for bar in bars:
        yval = bar.get_height()
        color = get_color(yval, high_threshold, low_threshold)
        plt.text(bar.get_x() + bar.get_width() / 2, yval, f"{round(yval, 2)}", va='bottom', color=color)

    plt.show()


def plot_null_counts(df, high_threshold, low_threshold):
    null_counts = df.isnull().sum()
    null_counts = null_counts[null_counts > 0]
    null_percentages = null_counts / df.shape[0] * 100
    sorted_null_percentages = null_percentages.sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    bars = plt.bar(sorted_null_percentages.index, sorted_null_percentages)
    plt.xlabel('Columns')
    plt.ylabel('Percentage of Nulls')
    plt.title('Percentage of Nulls in Each Column')
    plt.xticks(rotation=90)
    plt.grid(which='both', linestyle='--', linewidth=0.5, zorder=0)

    for bar in bars:
        yval = bar.get_height()
        color = get_color(yval, high_threshold, low_threshold)
        plt.text(bar.get_x() + bar.get_width() / 2, yval, f"{round(yval, 2)}%", va='bottom', color=color)

    plt.show()


def plot_with_capped_limit(df, column, quantiles, ylabel, plot_type='box'):
    if plot_type not in ['box', 'hist']:
        raise ValueError('plot_type should be one of "box" or "hist"')

    if not quantiles:
        getattr(df[column].plot, plot_type)()
        plt.title('Original')
        plt.ylabel(ylabel)

        if plot_type == 'hist':
            df[column].plot.density()

        plt.grid(which='both', linestyle='--', linewidth=0.5, zorder=0)
        plt.tight_layout()
        plt.show()
        return

    _, axs = plt.subplots(1, len(quantiles) + 1, figsize=(5 * (len(quantiles) + 1), 5))

    getattr(df[column].plot, plot_type)(ax=axs[0])
    axs[0].set_title('Original')
    axs[0].set_ylabel(ylabel)

    if plot_type == 'hist':
        df[column].plot.density(ax=axs[0])

    for i, quantile in enumerate(quantiles, start=1):
        cap = df[column].quantile(quantile)
        capped_data = df[column].where(df[column] <= cap, cap)
        getattr(capped_data.plot, plot_type)(ax=axs[i])

        if plot_type == 'hist':
            capped_data.plot.density(ax=axs[i])

        axs[i].set_title(f'Capped at {quantile} quantile')

    plt.grid(which='both', linestyle='--', linewidth=0.5, zorder=0)
    plt.tight_layout()
    plt.show()


def plot_stacked_bar_from_combinations(df, columns):
    value_counts = df[columns].value_counts()
    counts_df = value_counts.reset_index()
    counts_df.columns = columns + ['Count']

    counts_df['Label'] = counts_df[columns].apply(lambda row: ', '.join(row.index[row].tolist()), axis=1)

    plt.figure(figsize=(10, 6))
    bottom_pos = pd.Series([0] * counts_df.shape[0])
    for col in columns:
        counts = counts_df['Count'].where(counts_df[col]).fillna(0)
        plt.bar(counts_df['Label'], counts, bottom=bottom_pos, label=col)
        bottom_pos += counts

    plt.xlabel('OS Combination')
    plt.ylabel('Count')
    plt.title('Stacked Bar Chart of Value Counts for Combinations')
    plt.xticks(rotation=45)

    plt.grid(which='both', linestyle='--', linewidth=0.5, zorder=0)

    plt.legend()
    plt.tight_layout()
    plt.show()


def generate_text_cloud(df, column):
    si = StringIO()
    df[column].apply(lambda x: si.write(str(x)))
    string_cloud = si.getvalue()
    si.close()

    return string_cloud


def plot_word_cloud(df, column):
    text_cloud = generate_text_cloud(df, column)

    wordcloud = WordCloud(
        background_color="white",
        max_words=len(text_cloud),
        max_font_size=40,
        relative_scaling=.5
    ).generate(text_cloud)

    plt.figure()
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

