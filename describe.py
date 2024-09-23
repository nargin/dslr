import numpy as np

def mean(data):
	return sum(data) / len(data)

def std(data):
	m = mean(data)
	return (sum([(x - m)**2 for x in data]) / len(data))**0.5

def percentile(data, p):
	data = sorted(data)
	n = len(data)
	i = int(n * p)
	if i == n:
		return data[-1] # Last element xd broken python
	return data[i]

def describe(dataset):
	fields = {}

	# Extract header and data
	header = dataset[0]
	data = dataset[1:]

	# Convert data to numeric values
	numeric_data = [[float(val) if val.replace('.', '').isdigit() else np.nan for val in row] for row in data]

	# Calculate statistics
	valid_columns = []
	for i, field in enumerate(header):
		if field == 'Index':
			continue
		column = [row[i] for row in numeric_data]
		non_nan_values = [x for x in column if not np.isnan(x)]
		
		if len(non_nan_values) > 0:
			fields[field] = {
				'Count': len(column),
				'Mean': mean(non_nan_values),
				'Std': std(non_nan_values),
				'Min': min(non_nan_values),
				'25%': percentile(non_nan_values, 0.25),
				'50%': percentile(non_nan_values, 0.50),
				'75%': percentile(non_nan_values, 0.75),
				'Max': max(non_nan_values)
			}
			valid_columns.append(field)

	# Print the results
	print(f"{'':>8}", end="")
	for field in valid_columns:
		print(f"{field[:14]:>15}", end="")
	print()

	metrics = ['Count', 'Mean', 'Std', 'Min', '25%', '50%', '75%', 'Max']
	for metric in metrics:
		print(f"{metric:>8}", end="")
		for field in valid_columns:
			value = fields[field][metric]
			print(f"{value:15.6f}", end="")
		print()
