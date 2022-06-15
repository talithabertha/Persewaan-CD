genre_baru = str(input("Input genre baru :  "))
list1 = genre_baru.split()
real_genre = ""
for e in list1:
    real_genre = real_genre + e.capitalize() + " "
print(real_genre)