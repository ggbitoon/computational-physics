import numpy as np
import matplotlib.pyplot as plt

def linear(data):
    
    #fit equation is y=mx+b
    x=data['x']
    y=data['y']
    
    n=len(x)

    sumX=0
    sumY=0
    sumX2=0
    sumXY=0
    for i in range(n):
        sumX+=x[i]
        sumY+=y[i]
        sumX2+=x[i]**2
        sumXY+=x[i]*y[i]
    
    
    matA=np.array([[n,sumX],
                   [sumX,sumX2]])
    matB=np.array([[sumY],
                   [sumXY]])
    matX=np.linalg.inv(matA).dot(matB)
    
    b=float(matX[0])
    m=float(matX[1])

    
    yhat=[]
    
    for i in range(n):
        yhat.append(m*x[i]+b)
    
    meanY=sumY/n
    SSR=0
    SST=0
    SSE=0
    for i in range(n):
        SSR+=(yhat[i]-meanY)**2
        SST+=(y[i]-meanY)**2
        SSE+=(y[i]-yhat[i])**2
   
    R_squared=SSR/SST
    
    var=SSE/n-2
    covMat=var*np.linalg.inv(matA)
    errorM=np.sqrt(covMat[1,1])
    errorB=np.sqrt(covMat[0,0])

    plt.title('Linear Regression')
    plt.scatter(x,y,color='b')
    plt.plot(sorted(x),sorted(yhat),'r', label = f'y=({round(m,2)}$\pm${round(errorM,2)})x+({round(b,2)}$\pm${round(errorB,2)})\n'fr'R$^2$={round(R_squared,3)}')
    plt.legend(loc = 'best')
    plt.grid(True)
    plt.show()
    
def quadratic(data):
    
    #fit equation is y=ax^2+bx+c
    x=data['x']
    y=data['y']
        
    n=len(x)
    
    sumX4=0
    sumX3=0
    sumX2=0
    sumX=0
    sumX2Y=0
    sumXY=0
    sumY=0
    for i in range(n):
        sumX4+=x[i]**4
        sumX3+=x[i]**3
        sumX2+=x[i]**2
        sumX+=x[i]
        sumX2Y+=(x[i]**2)*(y[i])
        sumXY+=x[i]*y[i]
        sumY+=y[i]
    
    matA=np.array([[sumX4,sumX3,sumX2],
                   [sumX3,sumX2,sumX],
                   [sumX2,sumX,n]])
    matB=np.array([[sumX2Y],
                   [sumXY],
                   [sumY]])
    matX=np.linalg.inv(matA).dot(matB)

    a=float(matX[0])
    b=float(matX[1])
    c=float(matX[2])
    
    yhat=[]
    for i in range(n):
        yhat.append(a*(x[i]**2)+b*x[i]+c)
    
    meanY=sumY/n
    SSR=0
    SST=0
    SSE=0
    for i in range(n):
        SSR+=(yhat[i]-meanY)**2
        SST+=(y[i]-meanY)**2
        SSE+=(y[i]-yhat[i])**2
    
    R_squared=SSR/SST
    
    var=SSE/n-3
    covMat=var*np.linalg.inv(matA)
    errorA=np.sqrt(covMat[0,0])
    errorB=np.sqrt(covMat[1,1])
    errorC=np.sqrt(covMat[2,2])
    
    plt.title('Quadratic Regression')
    plt.scatter(x,y,color='blue')
    plt.plot(sorted(x),sorted(yhat),'r',label=f'y=({round(a,2)}$\pm${round(errorA,2)})x$^2$+({round(b,2)}$\pm${round(errorB,2)})x+({round(c,2)}$\pm${round(errorC,2)})\n'fr'R$^2$={np.round(R_squared,3)}')
    plt.legend(loc = 'best')
    plt.grid(True)
    plt.show()
    
def exponential(data):
    
    #fit equation is y=A*exp(bx); where A=exp(a)
    x=data['x']
    y=data['y']
    
    n=len(x)
    
    sumY=0
    sumXY=0
    sumX2Y=0
    sumYlnY=0
    sumXYlnY=0
    
    for i in range(n):
        sumY+=y[i]
        sumXY+=x[i]*y[i]
        sumX2Y+=x[i]**2*y[i]
        sumYlnY+=y[i]*np.log(y[i])
        sumXYlnY+=x[i]*y[i]*np.log(y[i])
    
        
    
    matA=np.array([[sumY,sumXY],
                  [sumXY,sumX2Y]])
    matB=np.array([[sumYlnY],
                  [sumXYlnY]])
    matX=np.linalg.inv(matA).dot(matB)
    
    a=np.exp(float(matX[0]))
    b=float(matX[1])
    yhat=[]
    
    for i in range(n):
        yhat.append(a*np.exp(b*x[i]))
    
    meanY=sumY/n
    SSR=0
    SST=0
    SSE=0
    for i in range(n):
        SSR+=(yhat[i]-meanY)**2
        SST+=(y[i]-meanY)**2
        SSE+=(y[i]-yhat[i])**2
    
    R_squared=SSR/SST
    
    var=SSE/n-2
    covMat=var*np.linalg.inv(matA)
    errorA=np.sqrt(covMat[0,0])
    errorB=np.sqrt(covMat[1,1])
    
    plt.title('Exponential Regression')
    plt.scatter(x,y,color='blue')
    plt.plot(sorted(x),sorted(yhat),'r',label=f'y=({round(a,2)}$\pm${round(errorA,2)})exp[({round(b,2)}$\pm${round(errorB,2)})x]\n'f'R$^2$={round(R_squared,3)}')
    plt.legend(loc = 'best')
    plt.grid(True)
    plt.show()

def power(data):
    
    #fit equation is y=Ax^b, where A=exp(a)
    x=data['x']
    y=data['y']
    
    n=len(x)
    sumY=0
    sumYlnX=0
    sumYlnX2=0
    sumYlnY=0
    sumYlnXlnY=0
    for i in range(n):
        sumY+=y[i]
        sumYlnX+=y[i]*np.log(x[i])
        sumYlnX2+=y[i]*(np.log(x[i]))**2
        sumYlnY+=y[i]*np.log(y[i])
        sumYlnXlnY+=y[i]*np.log(x[i])*np.log(y[i])
    
   
        
    matA=np.array([[sumY,sumYlnX],
                   [sumYlnX,sumYlnX2]])
    matB=np.array([[sumYlnY],
                   [sumYlnXlnY]])
    matX=np.linalg.inv(matA).dot(matB)
    
    a=float(np.exp(matX[0]))
    b=float(matX[1])
    
    yhat=[]
    for i in range(n):
        yhat.append(a*x[i]**b)
    
    meanY=sumY/n    
    SSR=0
    SST=0
    SSE=0
    for i in range(n):
        SSR+=(yhat[i]-meanY)**2
        SST+=(y[i]-meanY)**2
        SSE+=(y[i]-yhat[i])**2
        
    R_squared=SSR/SST
    
    var=SSE/n-2
    covMat=var*np.linalg.inv(matA)
    errorA=np.sqrt(covMat[0,0])
    errorB=np.sqrt(covMat[1,1])
    
    plt.title('Power Regression')
    plt.scatter(x,y,color='b')
    plt.plot(x,yhat,'r',label=f'y=({round(a,2)}$\pm${round(errorA,2)})x^({round(b,2)}$\pm${round(errorB,2)})\n'f'R$^2$={round(R_squared,3)}')
    plt.legend(loc = 'best')
    plt.grid(True)
    plt.show()

def logarithmic(data):
    
    #fit equation is y=a+b*ln(x)
    x=data['x']
    y=data['y']
    
    n=len(x)
       
    matA=np.array([[n,sum(np.log(x))],
                   [sum(np.log(x)),sum((np.log(x))**2)]])
    matB=np.array([[sum(y)],
                   [sum(np.log(x)*y)]])
    matX=np.linalg.inv(matA).dot(matB)
    
    a=float(matX[0])
    b=float(matX[1])
    
    yhat=[]
    for i in range(n):
        yhat.append(a+b*np.log(x[i]))
    
    meanY=sum(y)/n
    SSR=0
    SST=0
    SSE=0
    for i in range(n):
        SSR+=(yhat[i]-meanY)**2
        SST+=(y[i]-meanY)**2
        SSE+=(y[i]-yhat[i])**2
    
    R_squared=SSR/SST
    
    var=SSE/n-2
    covMat=var*np.linalg.inv(matA)
    errorA=np.sqrt(covMat[0,0])
    errorB=np.sqrt(covMat[1,1])
    
    plt.title('Logarithmic Regression')
    plt.scatter(x,y,color='b')
    plt.plot(sorted(x),sorted(yhat),'r', label = f'y=({round(a,2)}$\pm${round(errorA,2)})+({round(b,2)}$\pm${round(errorB,2)})$\ln $ x\n'f'R$^2$={round(R_squared,3)}')
    plt.legend(loc = 'best')
    plt.grid(True)
    plt.show()