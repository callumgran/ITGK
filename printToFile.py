albums = [['Beatles', 'And I love her'], ['Beatles', 'All my loving'], ['Traffic', 'John Barleycorn must die'], ['Cream', 'Sunshine of my love'], ['Cream', 'SLWABR']]


def list_to_disk():
    with open("demofile.txt", "a") as f:
        for i in range(len(albums)):
            for j in range(len(albums[i])):
                f.write(albums[i][j])
                if j == 0:
                    f.write(";")
                else:
                    f.write("\n")


open('demofile.txt', 'w').close()
list_to_disk()
with open("demofile.txt", "r") as r:
    print(r.read())
