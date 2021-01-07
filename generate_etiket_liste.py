import os

image_files = []
os.chdir(os.path.join("data", "Etiketsiz_Test"))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg"):
        image_files.append("data/Etiketsiz_Test/" + filename)
os.chdir("..")
with open("etiket_liste.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")