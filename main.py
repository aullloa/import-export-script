import csv

baselight_file = open("Baselight_export_fall2025.txt", "r")
xytech_file = open("Xytech_fall2025.txt", "r")
nerd_file = open("Nerd_export_fall2025.csv", "w")

writer = csv.writer(nerd_file)
writer.writerow(["Location", "Frames to Fix"])

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
    frames = list(map(int, eachLine[1:])) # Converting to int to check sequence
    print(frames)

    starting_frame = frames[0]
    ending_frame = frames[0]
    for frame in frames[1:]:
        if frame == ending_frame + 1: # correct sequence
            ending_frame = frame
        else:
            if starting_frame == ending_frame: #single frame with no sequential frame
                row = [new_url, starting_frame]
            else:
                row = [new_url, f"{starting_frame}-{ending_frame}"]
            writer.writerow(row)
            starting_frame = ending_frame = frame #reset trackers

