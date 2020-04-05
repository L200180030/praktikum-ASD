#Latihan Halaman 56
def gabungkanDuaListUrut(A,B):
    la=len(A); lb=len(B)
    C=list()
    i=0; j=0

    while i < la and j < lb:
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(A[i])
            j += 1
    while i < la:
        C.append(A[i])
        j += 1
    while j < lb:
        C.append(B[j])
        j += 1
    return C

#Latihan Halaman 59
def mergeSort(A):
    if len(A) > 1:
        mid=len(A)//2
        separuhKiri=A[:mid]
        separuhKanan=A[mid:]

        mergeSort(separuhKiri)
        mergeSort(separuhKanan)

        i=0;j=0;k=0
        while i < len(separuhKiri) and j < len(separuhKanan):
            if separuhKiri[i] < separuhKanan[j]:
                A[k]=separuhKiri[i]
                i=i+1
            else:
                A[k]=separuhKanan[j]
                j=j+1
            k=k+1

        while i < len(separuhKiri):
            A[k]=separuhKiri[i]
            i=i+1
            k=k+1
        while j < len(separuhKanan):
            A[k]=separuhKanan[j]
            j=j+1
            k=k+1

#Latihan Halaman 62-63
def quickSort(A):
    quickSortBantu(A,0,len(A)-1)
def quickSortBantu(A, awal, akhir):
    if awal < akhir:
        titikBelah=partisi(A,awal,akhir)
        quickSortBantu(A,awal,titikBelah-1)
        quickSortBantu(A,titikBelah+1,akhir)
def partisi(A, awal,akhir):
    nilaiPivot=A[awal]

    penandaKiri=awal+1
    penandaKanan=akhir

    selesai=False
    while not selesai:

        while penandaKiri <= penandaKanan and A[penandaKiri] <= nilaiPivot:
            penandaKiri=penandaKiri+1
        while A[penandaKanan] >= nilaiPivot and penandaKanan >= penandaKiri:
            penandaKanan=penandaKanan-1
        if penandaKanan < penandaKiri:
            selesai=True
        else:
            temp=A[penandaKiri]
            A[penandaKiri]=A[penandaKanan]
            A[penandaKanan]=temp
    temp=A[awal]
    A[awal]=A[penandaKanan]
    A[penandaKanan]=temp

    return penandaKanan
