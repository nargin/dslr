import csv
from describe import describe

def open_csv(file_path):
	with open(file_path, "r") as csvfile:
		csvreader = csv.reader(csvfile)
		data = [row for row in csvreader]
	return data

if __name__ == "__main__":
    try :
        dataset = open_csv("datasets/dataset_test.csv")
        describe(dataset=dataset)
    except Exception as e:
        print(e)
        print("Error while reading the file. Please check the file path and try again.")
