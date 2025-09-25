

baselight_file = open("Baselight_export_fall2025.txt", "r")
xytech_file = open("Xytech_fall2025.txt", "r+")

for line in baselight_file:
    eachLine = line.strip().split()
    url =  eachLine[0].strip("/baselightfilesystem1")
    base_frames = {
        "url": url,
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
