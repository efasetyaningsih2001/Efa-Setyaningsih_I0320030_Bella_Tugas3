#List nama teman
list_teman = ['Erysa', 'Dhea', 'Fadhila', 'Tsania', 'Ayu','Hafizh','Rengga','Memed','Cita','Alifiana',]
print("10 nama teman dekat saya: ", list_teman)

#Indeks teman 4,6,dan 7
print("Nama teman saya [4]: ", list_teman[4])
print("Nama teman saya [6]: ", list_teman[6])
print("Nama teman saya [7]: ", list_teman[7])

#Mengganti teman ke 3,5, dan 9
list_teman[3] = 'Udin'
list_teman[4] = 'Akrom'
list_teman[9] = 'Uli'

#Menambahkan 2 teman
list_teman.append('Aji')
list_teman.append('Akrom')

#List teman dengan pengulangan
print(list_teman*4)

#Panjang list teman
print("Semua teman saya adalah : ada",len(list_teman), "orang")
for panjanglist in list_teman:
    print(panjanglist)
