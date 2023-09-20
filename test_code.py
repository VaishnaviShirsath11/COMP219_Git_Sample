
import csv

# Define the input CSV file path
file_path = "job_data.csv"

# Create a dictionary to store the job titles and their corresponding sum of salaries and count
job_title_stats = {
    "Data Architect": {"sum_of_salaries": 0, "count": 0},
    "Senior Business Analyst": {"sum_of_salaries": 0, "count": 0},
    "Data Scientist": {"sum_of_salaries": 0, "count": 0},
    "Machine Learning Engineer": {"sum_of_salaries": 0, "count": 0},
}

# Open the CSV file for reading
with open(file_path, 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Iterate through the rows of the CSV file
    for row in reader:
        job_title = row['job_title']
        num_of_salaries = int(row['num_of_salaries'])

        # Check if the job title is in the dictionary
        if job_title in job_title_stats:
            job_title_stats[job_title]['sum_of_salaries'] += num_of_salaries
            job_title_stats[job_title]['count'] += 1

# Compute and print the average num_of_salaries for each job title
for title, stats in job_title_stats.items():
    if stats['count'] > 0:
        average_salary = stats['sum_of_salaries'] / stats['count']
        print(f"Average of num_of_salaries for {title}: {average_salary:.5f}")
    else:
        print(f"Data not found for {title}")

