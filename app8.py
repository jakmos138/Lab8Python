import argparse
import sys
import os
import re

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
    entries = []
    with open(filename, encoding="utf-8") as file:
        # Regular expression pattern to capture groups and omit quotes
        pattern = re.compile(r'''((?:[^,"']|"[^"]*"|'[^']*')+)''')

        # Find all matches using the pattern
        for line in file.readlines()[1:-1]:
            matches = pattern.findall(line)
            # Strip spaces and quotes from matches
            matches = [match.strip(' "') for match in matches]
            try:
                entry = movie(
                    id=matches[1],
                    title=matches[2],
                    overview=matches[3],
                    releaseDate=matches[4],
                    popularity=matches[5],
                    voteAverage=matches[6],
                    voteCount=matches[7]
                )
                entries.append(entry)
            except IndexError:
                print("Error parsing line:", line)
                entries.append(None)

    return entries


def run():
    args = parse_arguments()
    validate_file(args.dataset)
    validate_output_file(args.output)
    movies = parse_csv_file(args.dataset)


if __name__ == "__main__":
    run()
