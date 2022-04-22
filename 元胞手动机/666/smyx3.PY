import os
def zb(a,b):
    if a >= 0 :
        z='0'+str(a).zfill(6)
    else:
        z='1'+str(abs(a)).zfill(6)
    if b >= 0 :
        x='0'+str(b).zfill(6)
    else:
        x='1'+str(abs(b)).zfill(6)
    v=z+x
    return(v)


def zb2(a):
    g=a[0:1]
    h=a[1:7]
    j=a[7:8]
    k=a[8:14]
    if int(g) > 0 :
        x1=0-int(h)
    else :
        x1=int(h)
    if int(j) > 0 :
        y1=0-int(k)
    else :
        y1=int(k)
    v=[]
    v.append(x1)
    v.append(y1)
    return(v)


def zb3(a):
    z=zb2(a)
    x1=z[0]
    y1=z[1]
    gkl=0
    
    x_1=x1-4
    y_1=y1+4
    xy1=zb(x_1,y_1)
    if xy1 not in date_xy :
        x_y8.append(xy1)
    else :
        gkl+=1
    
           
    x_2=x1
    y_2=y1+4
    xy1=zb(x_2,y_2)
    if xy1 not in date_xy :
        x_y8.append(xy1)
    else :
        gkl+=1
    
    x_3=x1+4
    y_3=y1+4
    xy1=zb(x_3,y_3)
    if xy1 not in date_xy :
        x_y8.append(xy1)
    else :
        gkl+=1
    
    x_4=x1-4
    y_4=y1
    xy1=zb(x_4,y_4)
    if xy1 not in date_xy :
        x_y8.append(xy1)
    else :
        gkl+=1
        
  
    x_5=x1+4
    y_5=y1
    xy1=zb(x_5,y_5)
    if xy1 not in date_xy :
        x_y8.append(xy1)
    else :
        gkl+=1
    
        
    x_6=x1-4
    y_6=y1-4
    xy1=zb(x_6,y_6)
    if xy1 not in date_xy :
        x_y8.append(xy1)
    else :
        gkl+=1
    
       
    x_7=x1
    y_7=y1-4
    xy1=zb(x_7,y_7)
    if xy1 not in date_xy :
        x_y8.append(xy1)
    else :
        gkl+=1
       
        
    x_8=x1+4
    y_8=y1-4
    xy1=zb(x_8,y_8)
    if xy1 not in date_xy :
        x_y8.append(xy1)
    else :
        gkl+=1
        
    if  gkl !=2 and gkl != 3 :
         pass
    else :
         pen_b.append(a)

        
        
def zb4(a):
    z=zb2(a)
    x1=z[0]
    y1=z[1]
    gkl=0
    
    x_1=x1-4
    y_1=y1+4
    xy1=zb(x_1,y_1)
    if xy1  in date_xy : 
        gkl+=1
    
    
           
    x_2=x1
    y_2=y1+4
    xy1=zb(x_2,y_2)
    if xy1   in date_xy :
   
        gkl+=1
    
    x_3=x1+4
    y_3=y1+4
    xy1=zb(x_3,y_3)
    if xy1 in date_xy :
     
        gkl+=1
    
    x_4=x1-4
    y_4=y1
    xy1=zb(x_4,y_4)
    if xy1   in date_xy :
    
        gkl+=1
        
  
    x_5=x1+4
    y_5=y1
    xy1=zb(x_5,y_5)
    if xy1  in date_xy :
     
        gkl+=1
    
        
    x_6=x1-4
    y_6=y1-4
    xy1=zb(x_6,y_6)
    if xy1   in date_xy :
    
        gkl+=1
    
       
    x_7=x1
    y_7=y1-4
    xy1=zb(x_7,y_7)
    if xy1   in date_xy :
      
        gkl+=1
        
    x_8=x1+4
    y_8=y1-4
    xy1=zb(x_8,y_8)
    if xy1   in date_xy :
     
        gkl+=1
        
    if  gkl == 3 :
        if a not in pen_b :
            pen_b.append(a)

date_xy=[]
x_y8=[]
pen_b=[]
NNN=0
JGIGGI=input('文件路径:')
lj=''
for i in JGIGGI :
    if i == '"':
        pass
    else:
        lj=lj+i
        
fghhj=input('次数:')
MM=input('完成后的命名:')

lastdate= open (lj,'r')
for line in lastdate.readlines():
        line=line.strip('\n')
        date_xy.append(line)
lastdate.close()

while NNN != int(fghhj):
    for i in date_xy :
        zb3(i)
   
    for i in x_y8 :
        zb4(i)
    x_y8=[]
    date_xy=[]
    
    for i in pen_b :
        date_xy.append(i)
        
    pen_b=[]
    NNN+=1
    print(NNN)
a=os.path.abspath(os.path.dirname(os.getcwd()))
os.chdir(a)    
name='结果保存/'+MM+'----'+fghhj+'次的结果.txt'
hjjjiii=''    
for i in date_xy :
    hjjjiii=hjjjiii+i+'\n'
with open(name, 'w') as new:
    new.write(hjjjiii)
    
    
 
          
