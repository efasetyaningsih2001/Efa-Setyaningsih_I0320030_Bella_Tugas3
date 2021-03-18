#Membuat dictionary
print('\n','---------------------------------------BIODATA EFA (I0320030)----------------------------------------')
print('\n','-----------------------------------------------------------------------------------------------------','\n')
dictBiodata = {'Nama': 'Efa Setyaningsih',
        'Hobi': ['berenang','menonton film','main game'],
        'SosialMedia':['line:efa_s',
                       'ig:efa_setyaningsih',
                       'facebook:efa setyaningsih'],
        'Lagu Kesukaan':['Ruang rindu','pelukku untuk pelikmu','Brave'],
        'Makanan Favorit':['martabak','nasi goreng','sate ayam']
               }
print(dictBiodata)
print("Nama: ", dictBiodata['Nama'])
print("Hobi: ", dictBiodata['Hobi'])
print("SosialMedia: ", dictBiodata['SosialMedia'])
print("Lagu Kesukaan: ", dictBiodata['Lagu Kesukaan'])
print("Makanan Favorit:",dictBiodata['Makanan Favorit'])
print('\n','-----------------------------------------------------------------------------------------------------','\n')

#Menghilangkan satu hobi yaitu main game
del dictBiodata['Hobi'][2]
del dictBiodata['SosialMedia'][2]
print("Biodata saya setelah menghapus salah satu hobi dan sosial media adalah: ", dictBiodata)
print('\n','-----------------------------------------------------------------------------------------------------','\n')

#Menghilangkan makanan favorit
del dictBiodata['Makanan Favorit'][0:2]
print("Biodata saya setelah menghapus 2 menu makanan favorit adalah: ", dictBiodata)
print('\n','-----------------------------------------------------------------------------------------------------','\n')

#Menambahkan satu Hobi
dictBiodata['Hobi']: 'mendengarkan musik'
print("Biodata saya setelah menambahkan hobi adalah: ", dictBiodata)
print('\n','-----------------------------------------------------------------------------------------------------','\n')

#Biodata Final
print('------------------------------------------- BIODATA AKHIR --------------------------------------------')
print("Nama: ", dictBiodata['Nama'])
print("Hobi: ", dictBiodata['Hobi'])
print("SosialMedia: ", dictBiodata['SosialMedia'])
print("Lagu Kesukaan: ", dictBiodata['Lagu Kesukaan'])
print("Makanan Favorit:",dictBiodata['Makanan Favorit'])