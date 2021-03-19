#Membuat dictionary
print('\n', '---------------------------------------BIODATA EFA (I0320030)---------------------------------------')
dictBiodata = {'Nama': 'Efa Setyaningsih',
        'Hobi': ['berenang', 'menonton film', 'main game'],
        'SosialMedia':['line:efa_s',
                       'ig:efa_setyaningsih',
                       'facebook:efa setyaningsih'],
        'Lagu Kesukaan':['Ruang rindu', 'pelukku untuk pelikmu', 'Brave'],
        'Makanan Favorit':['martabak', 'nasi goreng', 'sate ayam']
               }
print(dictBiodata)
print('\n', '-----------------------------------------------------------------------------------------------------', '\n')

#Mengganti satu hobi dan sosial media
dictBiodata['Hobi'][2] = 'bersepeda'
dictBiodata['SosialMedia'][2] = 'WA:087836227881'
print("Biodata saya setelah mengganti salah satu hobi dan sosial media adalah: ", dictBiodata)
print('\n', '-----------------------------------------------------------------------------------------------------', '\n')

#Menghilangkan makanan favorit
del dictBiodata['Makanan Favorit'][0:2]
print("Biodata saya setelah menghapus 2 menu makanan favorit adalah: ", dictBiodata)
print('\n', '-----------------------------------------------------------------------------------------------------', '\n')

#Menambahkan satu Hobi
dictBiodata['Hobi'].append('mendengarkan musik')
print("Biodata saya setelah ditambah dengan 1 hobi adalah: ", dictBiodata)

