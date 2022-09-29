# Menghitung Jarak Fokus Lensa (f)

n = 1.50; # indeks bias medium
R1 = 20; # jari-jari kelengkungan permukaan lensa 1 dalam cm
R2 = 18; # jari-jari kelengkungan permukaan lensa 2 dalam cm

X = (n-1)*(1/R1+1/R2)

f = 1/X # jarak fokus lensa dalam cm
print(f)
