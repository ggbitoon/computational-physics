import numpy as np
import matplotlib.pyplot as plt

f=np.linspace(1,25,100)
t=np.linspace(0,10,500)
dt=t[1]-t[0]
def avePeakVoltages(v,r,l,c):
    avePeakV_r=[]
    avePeakV_l=[]
    avePeakV_c=[]
    v_s=[]
    for k in f:
        v_s=[v*np.cos(2*np.pi*k*j) for j in t]
        q_t=[] 
        q_td=[] #first derivative of q
        q_tdd=[] #second derivative of q

        for i in range(len(t)):
            if i==0:
                q1=0
                q2=0
                q_t.append((v_s[i]*dt**2+(2*l+r*dt)*q1-l*q2)/(l+r*dt+dt**2/c)) #working equation
            elif i==1:
                q1=q_t[-1]
                q2=0
                q_t.append((v_s[i]*dt**2+(2*l+r*dt)*q1-l*q2)/(l+r*dt+dt**2/c))
            else:
                q1=q_t[-1]
                q2=q_t[-2]
                q_t.append((v_s[i]*dt**2+(2*l+r*dt)*q1-l*q2)/(l+r*dt+dt**2/c))
      
        #finding the 1st derivative
        for i in range(len(q_t)-1):
            q_td.append((q_t[i+1]-q_t[i])/dt)
        #finding the 2nd derivative
        for i in range(len(q_td)-1):
            q_tdd.append((q_td[i+1]-q_td[i])/dt)
    
        #setup of values
        v_r=[]
        v_l=[]
        v_c=[]
    
        peakV_r=[]
        peakV_l=[]
        peakV_c=[]
    
        #calculating v across r
        for i in range(len(q_td)):
            v_r.append(q_td[i]*r)
        
        #finding peaks of v_r
        for i in range(len(v_r)):
            if i==0 and v_r[i]>v_r[i+1]:
                peakV_r.append(v_r[i])
            elif 0<i<(len(v_r)-1) and v_r[i-1]<v_r[i]>v_r[i+1]:
                peakV_r.append(v_r[i])
            elif i==len(v_r)-1 and v_r[i]>v_r[i-1]:
                peakV_r.append(v_r[i])
     
        #calculating v across l
        for i in range(len(q_tdd)):
            v_l.append(q_tdd[i]*l)
    
        #finding peaks of v_l
        for i in range(len(v_l)):
            if i==0 and v_l[i]>v_l[i+1]:
                peakV_l.append(v_l[i])
            elif 0<i<(len(v_l)-1) and v_l[i-1]<v_l[i]>v_l[i+1]:
                peakV_l.append(v_l[i])
            elif i==len(v_l)-1 and v_l[i]>v_l[i-1]:
                peakV_l.append(v_l[i])
            
        #calculating v across c
        for i in range(len(q_t)):
            v_c.append(q_t[i]/c)

        #finding peaks of v_c
        for i in range(len(v_c)):
            if i==0 and v_c[i]>v_c[i+1]:
                peakV_c.append(v_c[i])
            elif 0<i<(len(v_c)-1) and v_c[i-1]<v_c[i]>v_c[i+1]:
                peakV_c.append(v_c[i])
            elif i==len(v_c)-1 and v_c[i]>v_c[i-1]:
                peakV_c.append(v_c[i])
        
        avePeakV_r.append(sum(peakV_r)/len(peakV_r))
        avePeakV_l.append(sum(peakV_l)/len(peakV_l))
        avePeakV_c.append(sum(peakV_c)/len(peakV_c))
    #average voltage peaks vs frequency plot    
    plt.plot(f,avePeakV_r,'r',label='$V_r$')
    plt.plot(f,avePeakV_l,'g',label='$V_l$')
    plt.plot(f,avePeakV_c,'b',label='$V_c$')
    plt.grid(b=True,axis='both')

    plt.title('Voltage Peaks vs Frequency')
    plt.xlabel('Frequency $f$')
    plt.ylabel('Voltage Peaks')
    plt.legend(loc='upper right')
def freqVoltages(v,r,l,c):
    freqV_r=[]
    freqV_l=[]
    freqV_c=[]
    v_s=[]
    for k in f:
        v_s=[v*np.cos(2*np.pi*k*j) for j in t]
        q_t=[] 
        q_td=[] #first derivative of q
        q_tdd=[] #second derivative of q

        for i in range(len(t)):
            if i==0:
                q1=0
                q2=0
                q_t.append((v_s[i]*dt**2+(2*l+r*dt)*q1-l*q2)/(l+r*dt+dt**2/c)) #working equation
            elif i==1:
                q1=q_t[-1]
                q2=0
                q_t.append((v_s[i]*dt**2+(2*l+r*dt)*q1-l*q2)/(l+r*dt+dt**2/c))
            else:
                q1=q_t[-1]
                q2=q_t[-2]
                q_t.append((v_s[i]*dt**2+(2*l+r*dt)*q1-l*q2)/(l+r*dt+dt**2/c))
      
        #finding the 1st derivative
        for i in range(len(q_t)-1):
            q_td.append((q_t[i+1]-q_t[i])/dt)
        #finding the 2nd derivative
        for i in range(len(q_td)-1):
            q_tdd.append((q_td[i+1]-q_td[i])/dt)
    
        #setup of values
        v_r=[]
        v_l=[]
        v_c=[]
        
        locPeakV_r=[]
        locPeakV_l=[]
        locPeakV_c=[]
        
        timeV_r=[]
        timeV_l=[]
        timeV_c=[]
        
         #calculating v across r
        for i in range(len(q_td)):
            v_r.append(q_td[i]*r)
        #finding the location of peaks in v_r
        for i in range(len(v_r)):
            if i==0 and v_r[i]>v_r[i+1]:
                locPeakV_r.append(t[i])
            elif 0<i<(len(v_r)-1) and v_r[i-1]<v_r[i]>v_r[i+1]:
                locPeakV_r.append(t[i])
            elif i==len(v_r)-1 and v_r[i]>v_r[i-1]:
                locPeakV_r.append(t[i])
   
        for i in range(len(locPeakV_r)-1):
            timeV_r.append(locPeakV_r[i+1]-locPeakV_r[i])
        
        #calculating v across l
        for i in range(len(q_tdd)):
            v_l.append(q_tdd[i]*l)
    
        #finding the location of peaks in v_l
        for i in range(len(v_l)):
            if i==0 and v_l[i]>v_l[i+1]:
                locPeakV_l.append(t[i])
            elif 0<i<(len(v_l)-1) and v_l[i-1]<v_l[i]>v_l[i+1]:
                locPeakV_l.append(t[i])
            elif i==len(v_l)-1 and v_l[i]>v_l[i-1]:
                locPeakV_l.append(t[i])
            
        for i in range(len(locPeakV_l)-1):
            timeV_l.append(locPeakV_l[i+1]-locPeakV_l[i])    
        
        #calculating v across c
        for i in range(len(q_t)):
            v_c.append(q_t[i]/c)

        #finding the location of peaks in v_c
        for i in range(len(v_c)):
            if i==0 and v_c[i]>v_c[i+1]:
                locPeakV_c.append(t[i])
            elif 0<i<(len(v_c)-1) and v_c[i-1]<v_c[i]>v_c[i+1]:
                locPeakV_c.append(t[i])
            elif i==len(v_c)-1 and v_c[i]>v_c[i-1]:
                locPeakV_c.append(t[i])
            
        for i in range(len(locPeakV_c)-1):
            timeV_c.append(locPeakV_c[i+1]-locPeakV_c[i])  
        
        freqV_r.append(len(timeV_r)/sum(timeV_r))
        freqV_l.append(len(timeV_l)/sum(timeV_l))
        freqV_c.append(len(timeV_c)/sum(timeV_c))
   
    #subplots for frequency in each component vs input frequency        
    fig,(f_r,f_l,f_c)=plt.subplots(1,3,sharey=True)

    f_r.plot(f,freqV_r,'r',label='$f_r$')
    f_r.set_xlabel('Frequency $f$')
    f_r.set_ylabel('Frequency across $r$')
    f_r.legend(loc='upper left')
    f_r.grid(b=True, axis='both')
        
    f_l.plot(f,freqV_l,'g',label='$f_l$') 
    f_l.set_xlabel('Frequency $f$')
    f_l.set_ylabel('Frequency across $l$')
    f_l.legend(loc='upper left')
    f_l.grid(b=True, axis='both')
        
    f_c.plot(f,freqV_c,'b',label='$f_c$')
    f_c.set_xlabel('Frequency $f$')
    f_c.set_ylabel('Frequency across $c$')
    f_c.legend(loc='upper left')
    f_c.grid(b=True, axis='both')
    
    plt.tight_layout()
    
def freqRatioVoltages(v,r,l,c):
    
    freqRatioV_r=[]
    freqRatioV_l=[]
    freqRatioV_c=[]
    v_s=[]
    for k in f:
        v_s=[v*np.cos(2*np.pi*k*j) for j in t]
        q_t=[] 
        q_td=[] #first derivative of q
        q_tdd=[] #second derivative of q

        for i in range(len(t)):
            if i==0:
                q1=0
                q2=0
                q_t.append((v_s[i]*dt**2+(2*l+r*dt)*q1-l*q2)/(l+r*dt+dt**2/c)) #working equation
            elif i==1:
                q1=q_t[-1]
                q2=0
                q_t.append((v_s[i]*dt**2+(2*l+r*dt)*q1-l*q2)/(l+r*dt+dt**2/c))
            else:
                q1=q_t[-1]
                q2=q_t[-2]
                q_t.append((v_s[i]*dt**2+(2*l+r*dt)*q1-l*q2)/(l+r*dt+dt**2/c))
      
        #finding the 1st derivative
        for i in range(len(q_t)-1):
            q_td.append((q_t[i+1]-q_t[i])/dt)
        #finding the 2nd derivative
        for i in range(len(q_td)-1):
            q_tdd.append((q_td[i+1]-q_td[i])/dt)
    
        #setup of values
        v_r=[]
        v_l=[]
        v_c=[]
        
        locPeakV_r=[]
        locPeakV_l=[]
        locPeakV_c=[]
        
        timeV_r=[]
        timeV_l=[]
        timeV_c=[]
         #calculating v across r
        for i in range(len(q_td)):
            v_r.append(q_td[i]*r)
        #finding the location of peaks in v_r
        for i in range(len(v_r)):
            if i==0 and v_r[i]>v_r[i+1]:
                locPeakV_r.append(t[i])
            elif 0<i<(len(v_r)-1) and v_r[i-1]<v_r[i]>v_r[i+1]:
                locPeakV_r.append(t[i])
            elif i==len(v_r)-1 and v_r[i]>v_r[i-1]:
                locPeakV_r.append(t[i])
   
        for i in range(len(locPeakV_r)-1):
            timeV_r.append(locPeakV_r[i+1]-locPeakV_r[i])
        
        #calculating v across l
        for i in range(len(q_tdd)):
            v_l.append(q_tdd[i]*l)
    
        #finding the location of peaks in v_l
        for i in range(len(v_l)):
            if i==0 and v_l[i]>v_l[i+1]:
                locPeakV_l.append(t[i])
            elif 0<i<(len(v_l)-1) and v_l[i-1]<v_l[i]>v_l[i+1]:
                locPeakV_l.append(t[i])
            elif i==len(v_l)-1 and v_l[i]>v_l[i-1]:
                locPeakV_l.append(t[i])
            
        for i in range(len(locPeakV_l)-1):
            timeV_l.append(locPeakV_l[i+1]-locPeakV_l[i])    
        
        #calculating v across c
        for i in range(len(q_t)):
            v_c.append(q_t[i]/c)

        #finding location of peaks in v_c
        for i in range(len(v_c)):
            if i==0 and v_c[i]>v_c[i+1]:
                locPeakV_c.append(t[i])
            elif 0<i<(len(v_c)-1) and v_c[i-1]<v_c[i]>v_c[i+1]:
                locPeakV_c.append(t[i])
            elif i==len(v_c)-1 and v_c[i]>v_c[i-1]:
                locPeakV_c.append(t[i])
            
        for i in range(len(locPeakV_c)-1):
            timeV_c.append(locPeakV_c[i+1]-locPeakV_c[i])  

        freqRatioV_r.append(len(timeV_r)/(sum(timeV_r)*k))  
        freqRatioV_l.append(len(timeV_l)/(sum(timeV_l)*k))
        freqRatioV_c.append(len(timeV_c)/(sum(timeV_c)*k)) 
    #subplot of frequency ratio
    fig,(f_r,f_l,f_c)=plt.subplots(1,3,)

    f_r.plot(freqRatioV_r,'r',label='$f_r$:$f$')
    f_r.set_xlabel('nth value of f')
    f_r.set_ylabel('$f_r$ to $f$ ratio')
    f_r.legend(loc='upper left')
    f_r.set_yticks([0,1,2])
    f_r.grid(b=True, axis='both')
    
    f_l.plot(freqRatioV_l,'g',label='$f_l$:$f$') 
    f_l.set_xlabel('nth value of f')
    f_l.set_ylabel('$f_r$ to $f$ ratio')
    f_l.legend(loc='upper left')
    f_l.set_yticks([0,1,2])
    f_l.grid(b=True, axis='both')

    f_c.plot(freqRatioV_c,'b',label='$f_c$:$f$')
    f_c.set_xlabel('nth value of f')
    f_c.set_ylabel('$f_r$ to $f$ ratio')
    f_c.legend(loc='upper left')
    f_c.set_yticks([0,1,2])
    f_c.grid(b=True, axis='both')

    plt.tight_layout()
