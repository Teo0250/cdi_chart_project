import sys
import pandas as pd
import seaborn as sns

def generate_chart(png_file_name):

    df = pd.read_csv('./taxa-cdi.csv')

    chart = sns.lineplot(x=df['hora'], y=df['taxa'])
    _ = chart.set_xticklabels(labels=df['hora'], rotation=120)
    chart.get_figure().savefig(f"{png_file_name}.png")

if __name__ == "__main__":
    generate_chart(sys.argv[1])