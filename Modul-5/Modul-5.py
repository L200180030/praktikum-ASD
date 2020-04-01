class Mahasiswa(object):
    def __init__(self,nama,nim,kota,us):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = us

class MhsTIF (Mahasiswa):  
    def katakanPy(self):
        print('Python is cool.')
        
listan = [MhsTIF ('Bagus',175,'Surakarta', 130000),
MhsTIF('Doni',36,'Surabaya', 890000),
MhsTIF('Dono',29,'Klaten', 123000),
MhsTIF('Diaz',30,'Kudus', 230000),
MhsTIF('Sony',35,'Sleman', 22000),
MhsTIF('Yoga',31,'Magelang', 980000),
MhsTIF('Agus',34,'Semarang', 267000),
MhsTIF('Tita',28,'Surakarta', 212000),
MhsTIF('Subagyo',25,'Wonogiri', 975000),
MhsTIF('Tono',27,'Bekasi', 21000),
MhsTIF('Justin',226,'Rembang', 125000)]

#1
def urutkannim(l):
    n = len(l)
    for i in range (n -1) :
        for k in range (n-i-1) :
            if l[k].nim > l[k+1].nim :
                swap(l,k,k+1)

def checknimdong (l):
    for i in l :
        print (i.nim)

def swap (a, p, q) :
    tmp = a[p]
    a[p] = a[q]
    a[q] = tmp

#2
def mengurutkan(A,B):
    C = A+B
    n = len(C)
    for i in range(1,n):
        nilai=C[i]
        pos=i
        while pos > 0 and nilai < C[pos-1]:
            C[pos]=c[pos-1]
            pos=pos-1
        C[pos] = nilai
    return C
A = [21,23,25,27,29]
B = [31,33,35,37]

#3
from time import time as detak
from random import shuffle as kocok
def swap(A,p,q):
    tmp = A[p]
    A[p]= A[q]
    A[q]= tmp

def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i :
            swap(A, i, indexKecil)

def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos -1]
            pos = pos -1
        A[pos] = nilai
        
def cariPosisiYangTerkecil(A,darisini, sampaisini):
    posisiYangTerkecil = darisini
    for i in range (darisini+1, sampaisini):
        if A[i] < A[posisiYangTerkecil]:
            posisiYangTerkecil = i
    return posisiYangTerkecil

k = []
for i in range(1, 6001):
    k.append(i)
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak(); bubbleSort(u_bub);ak=detak();print('bubble: %g detik' %(ak-aw));
aw = detak(); selectionSort(u_sel);ak=detak();print('selection: %g detik' %(ak-aw));
aw = detak(); insertionSort(u_ins);ak=detak();print('insertion: %g detik' %(ak-aw));

#latihan
def swap(A,p,q):
    tmp=A[p]
    A[p]=A[q]
    A[q]=tmp

#latihan halaman 48
def cariPosisiTerkecil(A, dariSini, sampaiSini):
    posisiTerkecil=dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[i] < A[posisiTerkecil]:
            posisiTerkecil=i
    return posisiTerkecil

#latihan halaman 50
def bubbleSort(a):
    n=len(a)
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                swap(a,j,j+1)

#latihan halaman 52
def selectionSort(a):
    n=len(a)
    for i in range(n-1):
        indexKecil=cariPosisiTerkecil(a,i,n)
        if indexKecil != i:
            swap(a,i,indexKecil)

#latihan halaman 53
def insertionSort(A):
    n=len(A)
    for i in range(1,n):
        nilai=A[i]
        pos=i
        while pos > 0 and nilai < A[pos-1]:
            A[pos]= A[pos-1]
            pos=pos-1
        A[pos] = nilai
