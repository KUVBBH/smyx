import datetime
import turtle
import os

if not os.path.isdir('结果保存'):
    os.mkdir('结果保存')
    
rhghregu=input('---选择模式---\n1-绘制\n2-坐标\n3-只计算\n\n\n>>>')

if rhghregu == '1' :
    os.system('mode con cols=15 lines=1')
    date_xy=[]
    turtle.screensize(1000,1000)
    turtle.title('鼠标左键选中---鼠标右键取消---按下滚轮键确定')
    turtle.up()
    turtle.goto(-150,260)
    turtle.pencolor('red')
    turtle.write("鼠标左键选中---鼠标右键取消---按下滚轮键确定 ", True,align="center", font=4)
    turtle.pencolor('green')
    turtle.speed(0)
    turtle.delay(0)
    
    turtle.goto(408,408)
    turtle.pd()
    for i in range (0,4) :
        turtle.right(90)
        turtle.fd(800)
    for i in range (0,50) :
        h=turtle.heading()
        if h == 0 :
            turtle.right(90)
            turtle.fd(16)
            turtle.right(90)
            turtle.fd(800)
        if h == 180 :
            turtle.right(-90)
            turtle.fd(16)
            turtle.right(-90)
            turtle.fd(800)
    turtle.right(90)        
    for i in range (0,50) :
        h=turtle.heading()
        if h == 270 :
            turtle.left(-90)
            turtle.fd(16)
            turtle.left(-90)
            turtle.fd(800)
        if h == 90:
            turtle.left(90)
            turtle.fd(16)
            turtle.left(90)
            turtle.fd(800)
    turtle.up()
    turtle.goto(0,0)

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

    def f1(a,b) :
        for i in range(-8,8) :
            if (a+i)%16 == 0 :
                x=a+i
                   

        for i in range(-8,8) :
            if (b+i)%16 == 0 :
                y=b+i


        turtle.goto(x,y)
        turtle.dot(16,'black')
        ab=zb(int(x/4),int(y/4))
        if ab not in date_xy:
            date_xy.append(ab)
     

    def f2(a,b) :
        for i in range(-8,8) :
            if (a+i)%16 == 0 :
                x=a+i
                
          
        for i in range(-8,8) :
            if (b+i)%16 == 0 :
                y=b+i

        
                
        turtle.goto(x,y)
        turtle.dot(16,'white')
        ab=zb(int(x/4),int(y/4))
        if ab  in date_xy:
            date_xy.remove(ab)

    def f3(x,y) :
        global cs1
        cs1=''
        for i in date_xy :
            cs1=cs1+i+'\n'
        with open('666/1.txt','w') as f :
            f.write(cs1)
        turtle.bye()
        os.chdir('666')
        cmd = 'smyx.py'    
        os.system(cmd)

        
    turtle.listen()
    turtle.onscreenclick(f1,btn=1)
    turtle.onscreenclick(f2,btn=3)
    turtle.onscreenclick(f3,btn=2)
    turtle.mainloop()
   
if rhghregu == '2' :
    os.chdir('666')
    cmd = 'smyx2.py'    
    os.system(cmd)
    
if rhghregu == '3' :
    os.chdir('666')
    cmd = 'smyx3.py'    
    os.system(cmd)    

