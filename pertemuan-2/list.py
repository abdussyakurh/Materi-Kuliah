
# mengimpor modul sys
import sys

# membuat list
colors: list [str] = ["merah"]
print(colors)
print(sys.getsizeof(colors))

# menambah elemen
colors.append("kuning")
print(colors)
print(sys.getsizeof(colors))

colors.append("putih")
print(colors)
print(sys.getsizeof(colors))

colors.append("jingga")
print(colors)
print(sys.getsizeof(colors))

colors.append("hijau")
print(colors)
print(sys.getsizeof(colors))

colors.append("biru")
print(colors)
print(sys.getsizeof(colors))

colors.append("ungu")
print(colors)
print(sys.getsizeof(colors))

colors.append("hitam")
print(colors)
print(sys.getsizeof(colors))

colors.append("putih")
print(colors)
print(sys.getsizeof(colors))

# menghapus elemen terakhir
colors.pop()
print(colors)
print(sys.getsizeof(colors))

# menghapus elemen berdasarkan nilai
colors.remove("merah")
print(colors)
print(sys.getsizeof(colors))

# mengurutkan list
colors.sort()
print(colors)
print(sys.getsizeof(colors))

# mengurutkan list berdasarkan panjang elemen
'''colors.sort(key=len)
print(colors)
print(sys.getsizeof(colors))'''

# membalik urutan list
colors.reverse()
print(colors)
print(sys.getsizeof(colors))


number: list[float] = [3.9, 2.71, 3.9, 3.71, 3.7, 3.9,]
print(sum(number[0:5])/len(number))
print(len(number))
print(sys.getsizeof(number))
print(number)

# membuat salinan list
backup = number.copy()
print(backup)
print(sys.getsizeof(backup))
