#print("Merhaba, Django girls!")
if 3>2:
	print( "Calışıyor!")


def hi():
    print('Merhaba!')
    print('Nasılsın?')
hi()
def hi(name):
    print('Selam ' + name + '!')

hi("Seda")
def hi(name):
    print('Selam ' + name + '!')

girls = ['Seda', 'Gül', 'Pınar', 'Ayşe', 'Sen']
for name in girls:
    hi(name)
    print('Sıradaki')
    for i in range (1,6):
    	print(i)
    	
    	mysite/settings.py
