import csv

baselight_file = open("Baselight_export_fall2025.txt", "r")
xytech_file = open("Xytech_fall2025.txt", "r")
nerd_file = open("Nerd_export_fall2025.csv", "w")
writer = csv.writer(nerd_file)

baselight_lines = baselight_file.readlines()
xytech_lines = xytech_file.readlines()

for b_line in baselight_lines:
    eachLine = b_line.strip().split()
    url = eachLine[0].strip("/baselightfilesystem1")
    print(url)
    for x_line in xytech_lines:
        if not (x_line.startswith("/")):
            continue
        else:
            if (x_line.__contains__(url)):
                new_url = x_line
                break
    print(new_url)
    writer.writerow([new_url, ", ".join(eachLine[1:])])

