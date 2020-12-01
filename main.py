my_file = open("Advent1.txt", "r")
content = my_file.read()
star_list = content.split("\n")
my_file.close()

for x in star_list:
    star1 = int(x)
    for y in star_list:
        star2 = int(y)
        for z in star_list:
            star3=int(z)
            if star1 + star2+star3 ==2020:
                print("thing one: {0}, thing two: {1}, thing three: {2}".format(star1, star2, star3))
                break
