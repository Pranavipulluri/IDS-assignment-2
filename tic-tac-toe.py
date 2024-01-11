#!/usr/bin/env python
# coding: utf-8

# In[ ]:


row_1=[' ',' ',' ']
row_2=[' ',' ',' ']
row_3=[' ',' ',' ']
def display(row_1,row_2,row_3):
    print("   |   |   ")
    print(f" {row_1[0]} | {row_1[1]} | {row_1[2]} ")
    print("-----------")
    print("   |   |   ")
    print(f" {row_2[0]} | {row_2[1]} | {row_2[2]} ")
    print("-----------")
    print("   |   |   ")
    print(f" {row_3[0]} | {row_3[1]} | {row_3[2]} ")
display(row_1, row_2, row_3)
def game_on():
    choice=['Y','N']
    opt=' '
    while opt not in choice:
        opt=input("do u want to start game(Y or N):")
        if opt not in choice:
            print('wrong input enter Y or N')
    return opt
def XorY():
    print('lets start game')
    choices=['X','O']
    opts=' '
    while opts not in choices:
        opts=input("choose X or O:")
        if opts not in choices:
            print('wrong input enter X or O')
    return opts
def index():
    print("1|2|3\n-----\n4|5|6\n-----\n7|8|9")
    print("above is the model and these are the respective index positions")
    option='wrong'
    while option not in position:
        option=input("choose an index position (1-9):")
        if option not in position:
            print('wrong input enter index position (1-9)')
    return int(option)
def update(pick):
    if pick<=3:
        pick-=1
        row_1[pick]=opts
    elif pick<=6:
        pick-=4
        row_2[pick]=opts
    else:
        pick-=7
        row_3[pick]=opts
    display(row_1,row_2,row_3)
def update_comp(pick):
    if pick<=3:
        pick-=1
        row_1[pick]=optc
    elif pick<=6:
        pick-=4
        row_2[pick]=optc
    else:
        pick-=7
        row_3[pick]=optc
    display(row_1,row_2,row_3)
import random
def computer():
    x=random.randint(1,10)
    return x
opt=game_on()
if opt=='Y':
  won=''
  optc=''
  opts=XorY()
  if opts=='X':
      optc='O'
  else:
      optc='X'
  post=['1','2','3','4','5','6','7','8','9']
  position=['1','2','3','4','5','6','7','8','9']
  while won=='' and position!=[]:
      pick=index()
      position.remove(post[pick-1])
      update(pick)
      print('now pranavi computer output is:')
      x=computer()
      while str(x) not in position:
          x=computer()
      update_comp(x)
      position.remove(post[x-1])
      if (row_1[0]==row_1[1]==row_1[2]==opts) or (row_2[0]==row_2[1]==row_2[2]==opts) or (row_3[0]==row_3[1]==row_3[2]==opts) or (row_1[0]==row_2[0]==row_3[0]==opts) or (row_1[1]==row_2[1]==row_3[1]==opts) or (row_1[2]==row_2[2]==row_3[2]==opts) or (row_1[0]==row_2[1]==row_3[2]==opts) or (row_3[0]==row_2[1]==row_1[2]==opts):
          print("you won!!")
          print("FACT:pranavi computer is not as inteligent as pranavi so u won")
          won='you'
      elif (row_1[0]==row_1[1]==row_1[2]==optc) or (row_2[0]==row_2[1]==row_2[2]==optc) or (row_3[0]==row_3[1]==row_3[2]==optc) or (row_1[0]==row_2[0]==row_3[0]==optc) or (row_1[1]==row_2[1]==row_3[1]==optc) or (row_1[2]==row_2[2]==row_3[2]==optc) or (row_1[0]==row_2[1]==row_3[2]==optc) or (row_3[0]==row_2[1]==row_1[2]==optc):
          print("you loose!")
          won='computer'
else:
    print('ending the game')


# In[ ]:




