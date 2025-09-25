

baselight_file = open("Baselight_export_fall2025.txt", "r")
xytech_file = open("Xytech_export_fall2025.txt", "r")

for line in baselight_file:
    eachLine = line.strip().split()
    base_frames = {
        "url": eachLine[0],
        "frames": eachLine[1:]
    }
    print(base_frames)

for line in xytech_file:
    if not(line.startswith("/")):
        continue
    else:
        eachLine = line.strip().split()
        url = eachLine[0]
        print(url)


