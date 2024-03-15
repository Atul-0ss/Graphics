import turtle as tr 
from tkinter import simpledialog,messagebox
import random

def rect(pos,size):
    tr.up()
    tr.goto(pos)
    tr.down()

    tr.begin_fill()
    for _ in range(2):
        tr.forward(size[0])
        tr.right(90)
        tr.forward(size[1])
        tr.right(90)
    tr.end_fill()
    tr.down()


def move(pos):
    tr.up()
    tr.goto(pos[0],pos[1])
    tr.down()


def randamizeDot(n=20,show=False):
    position=[(random.randint(50,800),random.randint(50,600)) for _ in range(n)]

    if show:
        for pos in position:
            move(pos)
            tr.begin_fill()
            tr.circle(1)
            tr.end_fill()
    
    return position


def graph(position,minDis=200):
    size=len(position)
    gmatrix=[[] for i in range(size)]

    for node in range(size):
        gmatrix[node].append(position[node])
        for i in range(size):
            if abs(position[node][0]-position[i][0]) <= minDis and abs(position[node][1]-position[i][1]) <= minDis:
                gmatrix[node].append(position[i])
    return gmatrix


def drawGraph(gmatrix):
    relation=[]
    for row in gmatrix:
        tr.up()
        tr.goto(row[0])
        tr.down()
        edges=0
        for i in range(1,len(row)):
            # line(row[0],row[i])
            tr.goto(row[i][0],row[i][1])
            edges+=1
        relation.append((row[0],edges))
    return relation


def update_coordinates(x,y):
    tr.title("Coordinates: ({}, {})".format(x, y))


#**************************************************************
def GRAPHart():
    n=simpledialog.askinteger("vertices","Enter no of vertices: ")
    minDis=simpledialog.askfloat("minDis","Enter minimum distance to join 2 vertices: ")

    instances = randamizeDot(n,True)
    Graph = graph(instances,minDis)
    relation=drawGraph(Graph)

    print(relation)
    messagebox.showinfo("Graph Result{{vertex},edges}",relation)
    # print(instances,"\n\n")
    # print(Graph)
    tr.done()
#***************************************************************

def main():
    window = tr.Screen()
    window.setup(800,600)
    window.setworldcoordinates(0,800,600,0)
    tr.onscreenclick(update_coordinates)
    window.title("My Turtle Window")
    window.bgcolor("white")
    tr.colormode(255)
    tr.speed(0)

    GRAPHart()

    # Keep the window open until it's manually closed
    window.mainloop()


if __name__=="__main__":
    main()
