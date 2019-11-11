from tkinter import*

def command(d):
   q={'A':1,'B':2,'C':3,'D':4,'E':5,
        'F':8,'G':3,'H':5,'I':1,'J':1,
        'K':2,'L':3,'M':4,'N':5,'O':7,
        'P':8,'Q':1,'R':2,'S':3,'T':4,
        'U':6,'V':6,'W':6,'X':5,'Y':1,'Z':7}
   bl.append(q[d])
   n.append(d)
   na=''
   for u in n:
      na +=u

   nv.set(str(na))
   
def tot():
    t=(sum(bl))
    i =int(t)
    digits = [int(d) for d in list(str(i))]
    fi=sum(digits)
    if (fi==1):
        ai="Your Number is : 1"
        bi="Your Rulling Plannnet is SUN"
        ci="""Attractive personality. Magnetic charm.Superman/superwoman like vitality and physical energy.
              Incredibly active and gregarious. Enjoys outdooractivities and sports.
              Has friends and individualsin powerful positions.
              Good government connections.
              Intelligent, spectacular, flashy and successful.
              A loyal number for love and relationships.""" 
    elif(fi==2):
         ai="Your Number is : 2"
         bi="Your Rulling Plannnet is MOON"
         ci="""Feminine and soft, emotional temperament.
               Fluctuating moods but intuitive, and possibly even clairvoyant abilities.
               Ingenious nature and kind-hearted expression of feelings.Loves family, mother and home life.
               Night owl who probably needs more sleep. Success with the public and/or women generally."""
    elif(fi==3):
         ai="Your Number is : 3"
         bi="Your Rulling Plannnet is JUPITER"
         ci="""Sociable, optimistic number with fortunate destiny.
                Attracts opportunities without too much effort.
                Great sense of timing.
                Religious or spiritual inclinations.
                Naturally drawn to investigate the meaning of life.
                Philosophical insight.
                Enjoys travel and explore the world and different cultures."""
        
    elif(fi==4):
        ai="Your Number is : 4"
        bi="Your Rulling Plannnet is URANUS"
        ci="""Volatile character with many peculiar aspects.
              Likes to experiment and test novel experiences.
              Forward thinking,with many extraordinary friends.
              Gets bored easily so needs plenty of inspiring activities.
              Pioneering, technological and creative.
              Wilful and obstinate at times.
              Unforeseen events in life may be positive or negative."""
    elif(fi==5):
        ai="Your Number is : 5"
        bi="Your Rulling Plannnet is MERCURY"
        ci="""Sharp-wit, quick thinking with great powers of speech. Extremely active life.
              always on the go and lives on nervous energy.
              Youthful outlook and never grows old.
              Looks younger than actual age.
              Young friends and humorous disposition.
              Loves reading and writing. Great communicator."""
    elif(fi==6):
        ai="Your Number is : 6"
        bi="Your Rulling Plannnet is VENUS"
        ci="""Delightful and charming personality.
              Graceful and eye-catching personality who cherishes and nourishes friends.
              Very active social life.
              Musical or creative interests.
              Great money making opportunities as well as numerous love affairs are indicated.
              Career in the public eye is quite likely.
              Loves family but is often troubled other divided loyalties with friends."""
    elif(fi==7):
        ai="Your Number is : 7"
        bi="Your Rulling Plannnet is NEPTUNE"
        ci="""Intuitive, spiritual and self sacrificing nature.
              Easily duped by those who need help.
              Loves to dream of life's possibilities.
              Has healing powers.
              Dreams are revealing and prophetic.
              Loves the water and will have many journeys in life.
              Spiritual aspirations dominate worldly desires."""
    elif(fi==8):
        ai="Your Number is : 8"
        bi="Your Rulling Plannnet is SATURN"
        ci=""""Hard-working, ambitious person with slow yet certain achievements.
               Remarkable concentration and self-sacrifice for a chosen or objective.
               Financially focused but generous when a person's trust is gained.
               Proficient in one's chosen field but is a hard taskmaster.
               Demands perfection and needs to relax and enjoy life more."""
    elif(fi==9):
        ai="Your Number is : 9"
        bi="Your Rulling Plannnet is MARS"
        ci="""Extraordinary physical drive, desires and ambition.
              Sports and outdoor activities are major keys to health.
              Confrontational but likes to work and play really hard.
              Protects and defends family, friends and territory.
              Individual tastes in life but is also self absorbed.
              Needs to listen to others' advice to gain greater success in life."""
    else:
        ai="Some Thing Went Wrong"
        bi="restar the Program"
    w.destroy()
    s=Tk()
    gg="#09384e"
    s.title("your Characteristic")
    s.config(bg=gg)
    Label(s,text="POWER BEHIND YOUR NAME\nby DGcreation ",font='20',fg='white',bg=g,width=80).grid(row=1,columnspan=60)
    Label(s,text=ai,font='5',fg='white',bg=gg).grid(row=2,columnspan=60)
    Label(s,text=bi,font='5',fg='white',bg=gg).grid(row=3,columnspan=60)
    Label(s,text=ci,font='5',fg='white',bg=gg).grid(row=4,columnspan=60)

    def star():
       s.destroy()
       start()
       
       
    er=Button(s,text='Restart',command=star,font='20',width=10,bg='white',activebackground='grey',relief=RAISED,overrelief=RIDGE,fg=g)
    er.grid(row=5,column=0)
    
    s.mainloop()

def re():
   bl.clear()
   n.clear()
   nv.set('')

def start():
      global w,g,gt

      w=Tk()
      w.title("Numerology")
      g="#131328"
      gt="#45bffd"
      w.config(bg=g)

      global n,bl
      n=[]
      ############################
      bl=[]
      btn_list = ['A',  'B',  'C',  'D',  'E',
              'F',  'G',  'H',  'I',  'J',
              'K',  'L',  'M',  'N',  'O',

              'P',  'Q',  'R',  'S',  'T' ,'U','V','W','X','Y','Z']
      r = 15
      c = 0
      b = []
      for b in btn_list:
          Button(w, text=b,bg=gt, width=10,relief=RAISED,overrelief=RIDGE,activebackground='grey', command=lambda j=b: command(j)).grid(row=r, column=c)
          c += 1
          if c > 4:
             c = 0
             r += 1
      ###################################

      Label(w,text='NUMEROLOGY by DGcreation',fg='white',font='10',bg=g).grid(row=2,columnspan=10)
      Label(w,text='----------------------------Power Behind Your Name------------------------------',fg='white',font='30',bg=g).grid(row=1,columnspan=60)
      Label(w,text='Enter ur name>>>>>> ',fg='white',font='5',bg=g).grid(row=3,columnspan=60)
      global nv
      nv=StringVar()
      en=Entry(w,textvariable=nv,width=30,font='20',fg="red")
      en.grid(row=4,columnspan=60)
      e=Button(w,text='Find',command=tot,font='20',width=30,height=2,bg='white',activebackground='grey',relief=RAISED,overrelief=RIDGE,fg=g)
      e.grid(row=24,columnspan=60)
      er=Button(w,text='Restart',command=re,font='20',width=10,bg='white',activebackground='grey',relief=RAISED,overrelief=RIDGE,fg=g)
      er.grid(row=26,column=7)
      w.mainloop()
start()

