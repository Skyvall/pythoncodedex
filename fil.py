import csv

with open("Bestseller - Sheet1.csv", "r") as file:
    reader = csv.DictReader(file)
    max_row = max(reader, key=lambda row: float(row["sales in millions"]))

print(max_row["Book"], max_row["sales in millions"])


with open("bestseller_info.csv", "w", newline="") as file:
    fieldnames = ["Book", "Author", "sales in millions"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({
        "Book": max_row["Book"],
        "Author": max_row["Author"],
        "sales in millions": max_row["sales in millions"]
    })
    print("Max row written to bestseller_info.csv")