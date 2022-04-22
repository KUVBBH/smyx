import datetime
import turtle
import time
import os
os.system('mode con cols=15 lines=1')
date_xy=[]
CSZT=''
lj=turtle.textinput("请输入路径：", "例如：\nC\\:a\\1.txt")
lastdate= open (lj,'r')
for line in lastdate.readlines():
        line=line.strip('\n')
        CSZT=CSZT+line+'\n'
        date_xy.append(line)
lastdate.close()
turtle.screensize(999999,999999)
turtle.ht()
turtle.up()
turtle.color('red')
SLEEP=turtle.numinput("刷新间隔", "范围：0.00-1.00\n0最快；1最慢", 0.05,minval=0, maxval=1)
turtle.title('S：保存     Q：退出     Space：暂停3秒')
turtle.write("S：保存     Q：退出     Space：暂停3秒", True,align="center", font=4)
time.sleep(3)
turtle.speed(0)
turtle.delay(0)
turtle.tracer(0)



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
    if xy1  not in date_xy :
        pass
    else :
        gkl+=1
    
    
           
    x_2=x1
    y_2=y1+4
    xy1=zb(x_2,y_2)
    if xy1  not in date_xy :
        pass
    else :
        gkl+=1
    
    x_3=x1+4
    y_3=y1+4
    xy1=zb(x_3,y_3)
    if xy1  not in date_xy :
        pass
    else :
        gkl+=1
    
    x_4=x1-4
    y_4=y1
    xy1=zb(x_4,y_4)
    if xy1  not in date_xy :
        pass
    else :
        gkl+=1
        
  
    x_5=x1+4
    y_5=y1
    xy1=zb(x_5,y_5)
    if xy1  not in date_xy :
        pass
    else :
        gkl+=1
    
        
    x_6=x1-4
    y_6=y1-4
    xy1=zb(x_6,y_6)
    if xy1  not in date_xy :
        pass
    else :
        gkl+=1
    
       
    x_7=x1
    y_7=y1-4
    xy1=zb(x_7,y_7)
    if xy1  not in date_xy :
        pass
    else :
        gkl+=1
        
    x_8=x1+4
    y_8=y1-4
    xy1=zb(x_8,y_8)
    if xy1  not in date_xy :
        pass
    else :
        gkl+=1
        
    if  gkl == 3 :
        if a not in pen_b :
            pen_b.append(a)

def zb5(a):
    z=zb2(a)
    x1=z[0]
    y1=z[1]
    turtle.goto(x1,y1)
    turtle.dot(4,'black')   

def ft():
    a=os.path.abspath(os.path.dirname(os.getcwd()))
    os.chdir(a)
    TTT= (datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
    if not os.path.isdir('结果保存/'+TTT):
            os.mkdir('结果保存/'+TTT)
    BBZ=turtle.textinput("提示", "结果保存在---结果保存/"+TTT+"目录下---\n备注：")  
    a=turtle.getscreen()
    a.getcanvas().postscript(file='结果保存/'+TTT+'/最终结果.eps')
    
    B=''
    for i in  date_xy :
        C=str(i)+'\n'
        B+=C
    with open('结果保存/'+TTT+'/最终结果.txt','w') as f :
        f.write(B)

    with open('结果保存/'+TTT+'/开始状态.txt','w') as f :
        f.write(CSZT)

    BBZB='总共进行了'+str(NNN)+'步\n备注：'+BBZ

    with open('结果保存/'+TTT+'/备注.txt','w') as f :
        f.write(BBZB)

def ft1():
    time.sleep(3)

def ft2():
    turtle.bye()
    

x_y8=[]
pen_b=[]
NNN=0
while 1:
    for i in date_xy :
        zb3(i)
   
    for i in x_y8 :
        zb4(i)
    x_y8=[]
    date_xy=[]

    turtle.clear()
    
    for i in pen_b :
        date_xy.append(i)     
        zb5(i)
    pen_b=[]
    

    NNN+=1
    
    WERTY=0
    turtle.update()
    time.sleep(SLEEP)
    turtle.onkey(ft, "S")
    turtle.onkey(ft, "s")
    turtle.onkey(ft1, "space")
    turtle.onkey(ft2, "Q")
    turtle.onkey(ft2, "q")
    turtle.listen()
turtle.mainloop()
        


    
