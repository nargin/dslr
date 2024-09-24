import csv
from describe import describe
from histogram import histogram

def open_csv(file_path):
	with open(file_path, "r") as csvfile:
		csvreader = csv.reader(csvfile)
		data = [row for row in csvreader]
	return data

if __name__ == "__main__":
    try :
        pass
        dataset = open_csv("datasets/dataset_train.csv")
        # describe(dataset=dataset)
    except Exception as e:
        print(e)

    histogram()