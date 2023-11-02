#membuka file txt
f = open("demofile.txt", "w")

for i in range(0,9):
  nama = str(input("nama ; "))
  f.write(nama + '\n')
f.close()

f = open("demofile.txt", "r")
print(f.read())
f.close()