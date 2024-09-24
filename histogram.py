import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pds

def histogram():
    df = pds.read_csv("datasets/dataset_train.csv", index_col="Index")

    houses = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]
    house_data = {
        house: df[df['Hogwarts House'] == house].select_dtypes("number").dropna()
        for house in houses
    }

    sns.set_theme()

    for col in df.select_dtypes("number").columns:
        plt.figure(figsize=(12, 6))
        
        for house in houses:
            sns.histplot(data=house_data[house], x=col, kde=True, label=house)

        plt.title(f"Distrib of {col} by Hogwarts House")
        plt.xlabel(col)
        plt.ylabel("Count")
        plt.legend()
        plt.savefig(f"histogram_{col}.png")
        plt.close() # free memory

if __name__ == "__main__":
    histogram()