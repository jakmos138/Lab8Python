import argparse
import sys
import os
import re
import csv
from datetime import datetime

# URL of the dataset
# URL: https://www.kaggle.com/datasets/vishnurajyadav12/movies-dataset-tmdb


class movie:

    def __init__(self, id, title, overview,
                 releaseDate, popularity,
                 voteAverage, voteCount):
        self.id = id
        self.title = title
        self.overview = overview
        self.releaseDate = releaseDate
        self.popularity = popularity
        self.voteAverage = voteAverage
        self.voteCount = voteCount

    def __str__(self):
        return f"""Movie Id: {self.id}
                Title: {self.title}
                Overview: {self.overview}
                Release Date: {self.releaseDate}
                Popularity: {self.popularity}
                Vote Average: {self.voteAverage}
                Vote Count: {self.voteCount}"""


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Python app to analyze CSV dataset and generate report"
    )
    parser.add_argument("dataset", help="Path to the dataset CSV file")
    parser.add_argument(
        "-o",
        "--output",
        help="Name of the Excel file to be generated"
    )
    return parser.parse_args()


def validate_file(filename):
    if not filename.endswith('.csv'):
        sys.exit("Error: The file must have a .csv extension.")
    if not os.path.isfile(filename):
        sys.exit(f"Error: The file {filename} does not exist.")


def validate_output_file(filename):
    if filename and not filename.endswith('.xlsx'):
        sys.exit("Error: The output file must have a .xlsx extension.")


def parse_csv_file(filename):
    movies = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        next(reader)  # Skip the header row
        for row in reader:
            try:
                id = row[0]
                title = row[2]
                overview = row[3]
                release_date = datetime.strptime(row[4], '%Y-%m-%d')
                popularity = row[5]
                vote_average = row[6]
                vote_count = row[7]
                
                entry = movie(id, title, overview, release_date, popularity, vote_average, vote_count)
                movies.append(entry)
            except (IndexError, ValueError) as e:
                print("Error parsing row:", row)
                print("Exception:", e)
    return movies


def run():
    args = parse_arguments()
    validate_file(args.dataset)
    validate_output_file(args.output)
    movies = parse_csv_file(args.dataset)


if __name__ == "__main__":
    run()
