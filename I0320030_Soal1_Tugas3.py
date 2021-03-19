#List nama teman
list_teman = ['Cita', 'Dhea', 'Fadhila', 'Tsania', 'Erysa','Alifiana','Rengga','Memed','Deadila','Hafizh']
print("10 nama teman dekat saya: ", list_teman)

#Indeks teman 4,6,dan 7
print("Nama teman saya [4]: ", list_teman[4])
print("Nama teman saya [6]: ", list_teman[6])
print("Nama teman saya [7]: ", list_teman[7])

#Mengganti teman ke 3,5, dan 9
list_teman[3] = 'Udin'
list_teman[5] = 'Akrom'
list_teman[9] = 'Uli'

#Menambahkan 2 teman
list_teman.append('Aji')
list_teman.append('Desy')
print('list teman saya sekarang: ', list_teman)

#List teman dengan pengulangan
for pengulanganlist in list_teman:
    print(pengulanganlist)

#Panjang list teman
print("Jumlah teman saya adalah : ada",len(list_teman), "orang")
