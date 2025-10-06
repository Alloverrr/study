x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
color1=(x1+y1)%2
color2=(x2+y2)%2
same_color=color1==color2
color_name="white" if color1==0 else "black"
print ("YES" if same_color else "NO")
if same_color:
    print(color_name)