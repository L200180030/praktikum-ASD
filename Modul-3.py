###1
##k = [[4,7],[4,4]]
##l = [[5,6],[7,8]]
##m = [[1,3,9,9],[2,"x",4]]
##n = [[3,24],[32,5],[31,5]]
##o = [[2,3,3],[17,2,22]]
##p = [[8,9,20],[1,2,3],[3,4,5]]
####nomor 1a##
##def cekKonsisten(n):
##    x = len(n[0])
##    z = 0
##    for i in range(len(n)):
##        if (len(n[i]) == x):
##           z+=1
##    if(z == len(n)):
##        print("matriks konsisten")
##    else:
##        print("matrik tidak konsisten")
##print("##NOMOR 1a")
##cekKonsisten(k)
##cekKonsisten(l)
##cekKonsisten(m)
##
##def cekInteger(n):
##    x = 0
##    y = 0
##    for i in n:
##        for j in i:
##            y+=1
##            if (str(j).isdigit()==False):
##                print("tidak semua isi matriks adalah angka")
##                break
##            else:
##                x+=1
##    if(x==y):
##        print("semua isi matriks adalah angka")
##        
##cekInteger(k)
##cekInteger(l)
##cekInteger(m)
##
####nomor 1b##
##def cekordo(n):
##    x,y = 0,0
##    for i in range(len(n)):
##        x+=1
##        y = len(n[i])
##    print("mempunyai ordo "+str(x)+"x"+str(y))
##
##print("##NOMOR 1b")
##cekordo(k)
##cekordo(l)
##cekordo(m)
##cekordo(n)
##
####nomor 1c##
##def jumlah(n,m):
##    x,y = 0,0
##    for i in range(len(n)):
##        x+=1
##        y = len(n[i])
##    xy = [[0 for j in range(x)] for i in range(y)]
##    
##    z = 0
##    if(len(n)==len(m)):
##        for i in range(len(n)):
##            if(len(n[i]) == len(m[i])):
##                z+=1
##    if(z==len(n) and z==len(m)):
##        print("ukuran sama")
##        for i in range(len(n)):
##            for j in range(len(n[i])):
##                xy[i][j] = n[i][j] + m[i][j]
##        print(xy)
##    else:
##        print("ukuran beda")
##        
##print("##NOMOR 1c")
##jumlah(k,l)
##jumlah(k,n)
##   
####nomor 1d##     
##def kali(n,m):
##    aa = 0
##    x,y = 0,0
##    for i in range(len(n)):
##        x+=1
##        y = len(n[i])
##    v,w = 0,0
##    for i in range(len(m)):
##        v+=1
##        w = len(m[i])
##        
##    if(y==v):
##        print("bisa dikalikan")
##        vwxy = [[0 for j in range(w)] for i in range(x)]
##        for i in range(len(n)):
##            for j in range(len(m[0])):
##                for k in range(len(m)):
##                    #print(n[i][k], m[k][j])
##                    vwxy[i][j] += n[i][k] * m[k][j]
##        print(vwxy)
##            
##    else:
##        print("tidak memenuhi syarat")
##print("##NOMOR 1d")
##zz = [[1,2,3],[1,2,3]]
##zx = [[1],[2],[3]]
##kali(zz,zx)
##kali(k,l)
##kali(k,o)
##kali(k,zx)
##
####nomor 1e##
##def determinanHitung(A, total=0):
##    x = len(A[0])
##    z = 0
##    for i in range(len(A)):
##        if (len(A[i]) == x):
##           z+=1
##    if(z == len(A)):
##        if(x==len(A)):
##            indices = list(range(len(A)))
##            if len(A) == 2 and len(A[0]) == 2:
##                val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
##                return val
##            for fc in indices: 
##                As = A 
##                As = As[1:] 
##                height = len(As) 
##                for i in range(height): 
##                    As[i] = As[i][0:fc] + As[i][fc+1:] 
##                sign = (-1) ** (fc % 2) 
##                sub_det = determinanHitung(As)
##                total += sign * A[0][fc] * sub_det
##        else:
##            return "tidak bisa dihitung determinannya, karena bukan matrix bujursangkar"
##    else:
##        return "tidak bisa dihitung determinannya, karena bukan matrix bujursangkar"
##    return total
##
##
##q = [[3,1],[2,5]]
##r = [[1,2,1],[3,3,1],[2,1,2]]
##s = [[1,-2,0,0],[3,2,-3,1],[4,0,5,1],[2,3,-1,4]]
##t = [[10,23,45,12,13],[1,2,3,4,5],[1,2,3,4,6],[4,2,3,4,8],[1,4,5,6,10]]
##
##print("##NOMOR 1e")
##print(determinanHitung(q))
##print(determinanHitung(r))
##print(determinanHitung(s))
##print(determinanHitung(t))
##print(determinanHitung(n))
##print(determinanHitung(o))

###2
####nomor 2a##
##def buatNol(n,m=None):
##    if(m==None):
##        m=n
##    print("Membuat matriks 0 dengan ordo "+str(n)+"x"+str(m))
##    print([[0 for x in range(m)] for y in range(n)])
##print("##nomor 2a")
##buatNol(3)
##buatNol(5,3)
##
####nomor 2b
##def buatIdentitas(n):
##    print("Membuat matriks Identitas dengan ordo"+str(n)+"x"+str(n))
##    print([[1 if j==i else 0 for j in range(n)] for i in range(n)])
##
##print("##nomor 2b")
##buatIdentitas(7)
##buatIdentitas(3)

###3
##class Node: 
##    def __init__(self, data): 
##        self.data = data 
##        self.next = None
##class LinkedList: 
##    def __init__(self): 
##        self.head = None
##    def pushAwal(self, new_data): 
##        new_node = Node(new_data) 
##        new_node.next = self.head 
##        self.head = new_node
##    def pushAkhir(self, data):
##        if (self.head == None):
##            self.head = Node(data)
##        else:
##            current = self.head
##            while (current.next != None):
##                current = current.next
##            current.next = Node(data)
##        return self.head
##    def tambah(self,data,pos):
##        node = Node(data)
##        if not self.head:
##            self.head = node
##        elif pos==0:
##            node.next = self.head
##            self.head = node
##        else:
##            prev = None
##            current = self.head
##            current_pos = 0
##            while(current_pos < pos) and current.next:
##                prev = current
##                current = current.next
##                current_pos +=1
##            prev.next = node
##            node.next = current
##        return self.head
##    def hapus(self, position): 
##        if self.head == None: 
##            return 
##        temp = self.head 
##        if position == 0: 
##            self.head = temp.next
##            temp = None
##            return 
##        for i in range(position -1 ): 
##            temp = temp.next
##            if temp is None: 
##                break
##        if temp is None: 
##            return 
##        if temp.next is None: 
##            return 
##        next = temp.next.next
##        temp.next = None
##        temp.next = next 
##    def cari(self, x): 
##        current = self.head 
##        while current != None: 
##            if current.data == x: 
##                return "True"
##            current = current.next
##        return "False"
##    def display(self):
##        current = self.head
##        while current is not None:
##            print(current.data, end = ' ')
##            current = current.next   
##    
##llist = LinkedList() 
##llist.pushAwal(13)
##llist.pushAwal(14)
##llist.pushAwal(15)
##llist.pushAwal(16)
##llist.pushAwal(4)
##llist.pushAwal(18)
##llist.pushAkhir(19)
##llist.hapus(0)
##llist.tambah(2,5)
##print(llist.cari(14))
##print(llist.cari(17))
##llist.display()

#4
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.prev = None
class DoublyLinkedList: 
    def __init__(self): 
        self.head = None
    def menambahAwal(self, new_data):
        print("menambah pada awal", new_data)
        new_node = Node(new_data) 
        new_node.next = self.head 
        if self.head is not None: 
            self.head.prev = new_node 
        self.head = new_node 
    def menambahAkhir(self, new_data):
        print("menambah pada akhir", new_data)
        new_node = Node(new_data) 
        new_node.next = None
        if self.head is None: 
            new_node.prev = None
            self.head = new_node 
            return 
        last = self.head 
        while(last.next is not None): 
            last = last.next
        last.next = new_node 
        new_node.prev = last 
        return
    def printList(self, node): 
        print("\nDari Depan :")
        while(node is not None): 
            print(" % d" %(node.data))
            last = node 
            node = node.next
        print("\nDari Belakang :")
        while(last is not None): 
            print(" % d" %(last.data)) 
            last = last.prev 
llist = DoublyLinkedList() 
llist.menambahAwal(2)  
llist.menambahAwal(1)
llist.menambahAkhir(3)
llist.menambahAkhir(4) 
llist.printList(llist.head)
