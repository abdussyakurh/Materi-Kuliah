#membuat struktur data dictionary
userLogin = {"name": "Budi", "age": 20, "Role": "Super Admin"}
print(type(userLogin))

#mengakses elemen pada dictionary
print(f"Nama Akun : {userLogin['name']}")
print(f"Umur Akun : {userLogin['age']}")
print(f"Role Akun : {userLogin['Role']}")

#akses seluruh data
print(userLogin.items())
print(userLogin.keys())
print(userLogin.values())

#menambah data kedalam dictionary
userLogin["email"] = "example@gmail.com"
print(userLogin)

#menghapus data pada dictionary
userLogin.pop("email")
print(userLogin)

#mengubah data pada dictionary big-O O(1)
userLogin["Role"] = "User"
print(userLogin)

#Nested Dictionary
dbUser= {"user1": {"name": "Bambang", "age": 32, "Role": "Super Admin"},
        "user2": {"name": "Andi", "age": 21, "Role": "User"},
        "user3": {"name": "Caca", "age": 26, "Role": "Admin"}}

print(dbUser)

#akses value base key
print(dbUser["user1"])
print(dbUser["user2"]["age"])
print(dbUser["user3"]["Role"])

#melakukan pencarian data pada dictionary Big-O O(n)
findword = input("Masukkan kata yang ingin dicari: ")
if findword in dbUser:
    print("Data ditemukan")
else:
    print("Data tidak ditemukan")