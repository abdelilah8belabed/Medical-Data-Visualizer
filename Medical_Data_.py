
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('medical_examination.csv')


def medical_data_visualizer():
    df = pd.read_csv('medical_examination.csv')
    df['overweight'] = (df["weight"] / (df['height'] / 100) ** 2).apply(lambda x: 1 if x > 25 else 0)
    df['n_gluc'] = df['gluc'].apply(lambda x: 1 if x > 1 else 0)
    df['n_cholesterol'] = df['cholesterol'].apply(lambda x: 1 if x > 1 else 0)

    def draw_cat_plot():  # Categorical Plot
        df_cat = pd.melt(df,  # grouped the data by cardio and convert it in a long format
                         id_vars=['cardio'],
                         value_vars=['smoke', 'alco', 'active', 'overweight', 'n_gluc', 'n_cholesterol'],
                         var_name='variable',
                         value_name='value')
        df_cat = df_cat.groupby(['variable', 'value', 'cardio']).size().reset_index(name="count")
        fig = sns.catplot(data=df_cat, x='variable', y='count', hue='value', col='cardio', kind='bar')
        fig.fig.suptitle('Health Features by Cardio Condition', y=1.03)
        plt.show()

    def draw_heat_map():
        df_headmap = df.drop(columns=['age', 'id'], errors='ignore')
        df_filtered = df_headmap[
            (df['ap_hi'] >= df['ap_lo']) &
            (df['weight'] >= df['weight'].quantile(0.025)) &
            (df['weight'] <= df['weight'].quantile(0.975)) &
            (df['height'] >= df['height'].quantile(0.025)) &
            (df['height'] <= df['height'].quantile(0.975))
            ]

        corr = df_filtered.corr()
        plt.figure(figsize=(12, 10))
        sns.heatmap(corr, annot=True, fmt=".1f", cmap='coolwarm', square=True, cbar_kws={'shrink': .8})
        plt.title("head map ")
        plt.show()

    draw_cat_plot()
    draw_heat_map()


medical_data_visualizer()