#!/usr/bin/python3
# open source | bebas recode
# created by krypton
# kamis, 23 april 2020
# v 0.0.1 (beta)
#changelog v.0.0.1 : add fitur barcode reader
#changelog v.0.0.2 : add fiture barcode creater
from pyqrcode import QRCode 
import os
from PIL import Image
from pyzbar.pyzbar import decode
import pyqrcode
import png
p = '\x1b[0m'
m = '\x1b[91m'
h = '\x1b[92m'
k = '\x1b[93m'
b = '\x1b[94m'
u = '\x1b[95m'
barcode = '''
%s _______ %s _______ %s ______    %s_______ %s _______ %s ______   %s_______ 
%s|  _    |%s|   _   |%s|    _ |  %s|       |%s|       |%s|      | %s|       |
%s| |_|   |%s|  |_|  |%s|   | ||  %s|       |%s|   _   |%s|  _    |%s|    ___|
%s|       |%s|       |%s|   |_||_ %s|       |%s|  | |  |%s| | |   |%s|   |___ 
%s|  _   | %s|       |%s|    __  |%s|      _|%s|  |_|  |%s| |_|   |%s|    ___|
%s| |_|   |%s|   _   |%s|   |  | |%s|     |_ %s|       |%s|       |%s|   |___ 
%s|_______|%s|__| |__|%s|___|  |_|%s|_______|%s|_______|%s|______| %s|_______|
%s
'''%( m,k,h,u,b,m,k,m,k,h,u,b,m,k,m,k,h,u,b,m,k,m,k,h,u,b,m,k,m,k,h,u,b,m,k,m,k,h,u,b,m,k,m,k,h,u,b,m,k,p)
generator = '''

%s _______  %s______     %s _______  %s______  %s  _______  %s_______  %s_______ %s _______  %s______   
%s|       |%s|    _ |    %s|       |%s|    _ |  %s|       |%s|   _   |%s|       |%s|       |%s|    _ |  
%s|   _   |%s|   | ||    %s|       |%s|   | ||  %s|    ___|%s|  |_|  |%s|_     _|%s|   _   |%s|   | ||  
%s|  | |  |%s|   |_||_   %s|       |%s|   |_||_ %s|   |___ %s|       |  %s|   |  %s|  | |  |%s|   |_||_ 
%s|  |_|  |%s|    __  |  %s|      _|%s|    __  |%s|    ___|%s|       |  %s|   |  %s|  |_|  |%s|    __  |
%s|      | %s|   |  | |  %s|     |_ %s|   |  | |%s|   |___ %s|   _   |  %s|   |  %s|       |%s|   |  | |
%s|____||_|%s|___|  |_|  %s|_______|%s|___|  |_|%s|_______|%s|__| |__|  %s|___|  %s|_______|%s|___|  |_|
%s'''%( m,k,h,u,b,m,k,h,u,m,k,h,u,b,m,k,h,u,m,k,h,u,b,m,k,h,u,m,k,h,u,b,m,k,h,u,m,k,h,u,b,m,k,h,u,m,k,h,u,b,m,k,h,u,m,k,h,u,b,m,k,h,u,p)
logo = '''
%s _______ %s ______     %s______   %s _______  %s_______ %s ______  %s _______ %s ______   
%s|       |%s|    _ |   %s|    _ |  %s|       |%s|   _   |%s|      | %s|       |%s|    _ |  
%s|   _   |%s|   | ||   %s|   | ||  %s|    ___|%s|  |_|  |%s|  _    |%s|    ___|%s|   | ||  
%s|  | |  |%s|   |_||_  %s|   |_||_ %s|   |___ %s|       |%s| | |   |%s|   |___ %s|   |_||_ 
%s|  |_|  |%s|    __  | %s|    __  |%s|    ___|%s|       |%s| |_|   |%s|    ___|%s|    __  |
%s|      | %s|   |  | | %s|   |  | |%s|   |___ %s|   _   |%s|       |%s|   |___ %s|   |  | |
%s|____||_|%s|___|  |_| %s|___|  |_|%s|_______|%s|__| |__|%s|______| %s|_______|%s|___|  |_|
%s'''%(  m,k,h,u,b,m,k,h,m,k,h,u,b,m,k,h,m,k,h,u,b,m,k,h,m,k,h,u,b,m,k,h,m,k,h,u,b,m,k,h,m,k,h,u,b,m,k,h,m,k,h,u,b,m,k,h,p )
def baca(file):
	hasil=decode(Image.open(file))[0][0].decode('utf-8')
	return hasil
def Buat():
	print(generator)
	teks= input('text      : ')
	sv  = input('simpan di : ')
	bar = pyqrcode.create(teks)
	print('%sformat\n 1. png\n 2.svg%s'%(k,p))
	tipe = input ('%sformat : %s'%(h,p))
	while True:
		if tipe in ['1','01']:
			bar.png('%s.png'%(sv), scale = 6 )
			print('save : %s.%s.png',(os.getcwd()[0],sv))
			break
		elif type in ['2','02']:
			bar.svg('%s.svg'%(sv), scale = 8)
			print('save : %s.%s.svg',(os.getcwd()[0],sv))
			break
		else:
			print('%s[%s*%s]%s Yang Anda Pilih  tidak Ada%s'%(m,k,m,k,p))
def Main():
	os.system('clear')
	print(logo)
	while True:
		qr = input(' %s[%s?%s]%s f%si%sl%se %s : '%(h,k,h,m,k,h,u,p))
		if qr in os.listdir('.'):
			try:
				print(' %s[%s+%s]%s hasil%s : %s'%(k,b,k,h,p,baca(qr)))
				break
			except:
				print(' %s[%s!%s]%s Tidak Terbaca%s'%(k,m,k,m,p))
		else:
			print('%s[%s*%s]%s File tidak Ada%s'%(m,k,m,k,p))

def menu():
	print('%s 1. buat barcode\n 2. baca barcode'%(k))
	while True:
		pilih = input(' %s[%s?%s]%s pilih : %s'%(h,k,h,b,p))
		if pilih in ['01','1']:
			Buat()
			break
		elif pilih in ['2','02']:
			Main()
			break
		else:
			print('%s[%s!%s]%s pilihan anda tidak ada%s'%(k,m,k,m,p))
if __name__ == '__main__':
	os.system('clear')
	print(barcode)
	print(menu())
