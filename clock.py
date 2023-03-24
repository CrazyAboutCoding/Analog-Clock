from turtle import*
setup(500,500) #Setting screen configuration
bgcolor("black")#Screen color
pensize(5) #Size of the turtle object
shape("classic") #Shape of turtle object:"classic" is arrow
pencolor("white")
n=0 #value for numbers in clock
goto(0,0) #To bring turtle object to centre
left(90)
for i in range(12): #Loop for the numbers in clock
    n=n+1 #Increment in value
    penup() #Making turtle object invisible
    goto(0,0)
    right(30) #Turning angle towards right
    forward(100)
    pendown() #Making turtle object visible
    forward(20)
    penup()
    forward(20)
    write(str(n), align="center", font=("Arial", 12, "normal")) #To write the clock numbers
    if n==12: #To bring the turtle object back to centre
        goto(0,0)
