import numpy as np
import math


# Please replace "StudentMatriculationNumber" with your actual matric number here and in the filename
def A3_MatricNumber(learning_rate, max_iteration):
    """
    Input type
    :learning_rate type: float
    :num_iters type: int

    Return type
    :a_out type: numpy array of length num_iters
    :f1_out type: numpy array of length num_iters
    :b_out type: numpy array of length num_iters
    :f2_out type: numpy array of length num_iters
    :c_out type: numpy array of length num_iters
    :d_out type: numpy array of length num_iters
    :f3_out type: numpy array of length num_iters
    """
    # your code goes here
    
    a=1
    f1=pow(a,4)
    
    a_out = 0
    f1_out = 0
    
    def h (a_out, f1_out, a) :
      return a_out * a + f1_out
    
    
    def loss (a_out, f1_out, a, f1) :
      return np.average(np.square(f1 - h(a_out, f1_out, a))) / 2
    
    def gradient (a_out, f1_out, a, f1) :
      dm = - np.average((f1 - h(a_out, f1_out, a)) * a)
      db = - np.average(a - h(a_out, f1_out, a))
      return (dm, db)
    
    
    def gradient_descent (a_out, f1_out, a, f1, learning_rate, max_iteration) :
      for i in range(int(max_iteration)) :
        dm, db = gradient (a_out, f1_out, a, f1)
        a_out -= learning_rate * dm
        f1_out -= learning_rate * db
        if i % 10 == 0 :
          print ('iteration : ', i, ' loss : ', loss(a_out, f1_out, a, f1)) 
      return (a_out, f1_out)
  
    a_out, f1_out = gradient_descent (a_out, f1_out, a, f1, learning_rate, max_iteration)
    
    
    b=0.8
    f2=math.cos(b)
    
    b_out = 0
    f2_out = 0
    
    def h (b_out, f2_out, b) :
      return b_out * b + f2_out
    
    
    def loss (b_out, f2_out, b, f2) :
      return np.average(np.square(f2 - h(b_out, f2_out, b))) / 2
    
    def gradient (b_out, f2_out, b, f2) :
      dm = - np.average((f2 - h(b_out, f2_out, b)) * b)
      db = - np.average(f2- h(b_out, f2_out, b))
      return (dm, db)
    
    
    def gradient_descent (b_out, f2_out, b, f2, learning_rate, max_iteration) :
      for i in range(int(max_iteration)) :
        dm, db = gradient (b_out, f2_out, b, f2)
        b_out -= learning_rate * dm
        f2_out -= learning_rate * db
        if i % 10 == 0 :
          print ('iteration : ', i, ' loss : ', loss(b_out, f2_out, b, f2)) 
      return (b_out, f2_out)
  
    b_out, f2_out = gradient_descent (b_out, f2_out, b, f2, learning_rate, max_iteration)
    
    c,d=2,3
    f3=c**2+d**2
    

    c_out = 0
    d_out = 0
    f3_out = 0
    
    def h (c_out, d_out, f3_out, c, d) :
      return (c_out * c+ f3_out)+(d_out * d+ f2_out)
    
    
    def loss (c_out, d_out, f3_out, c,d, f3) :
      return np.average(np.square(f3 - h(c_out, d_out, f3_out, c,d))) / 2
    
    def gradient (c_out,d_out,f3_out, c,d, f3) :
      dc = - np.average((f3 - h(c_out, d_out, f3_out, c,d)) * c) 
      dd = - np.average((f3 - h(c_out, d_out, f3_out, c,d)) * d)
      df = - np.average(f3 - h(c_out, d_out, f3_out, c,d))
      return (dc, dd, df)
    
    
    def gradient_descent (c_out, d_out, f3_out, c,d, f3, learning_rate, max_iteration) :
      for i in range(int(max_iteration)) :
          dc, dd, df = gradient (c_out, d_out, f3_out, c,d, f3)
          c_out -= learning_rate * dc
          d_out -= learning_rate * dd
          f3_out -= learning_rate * df
          if i % 10 == 0 :
              print ('iteration : ', i, ' loss : ', loss(c_out, d_out, f3_out, c,d, f3)) 
      return (c_out, d_out ,f3_out)
    
    
    c_out, d_out, f3_out = gradient_descent (c_out, d_out, f3_out, c,d, f3, learning_rate, max_iteration)



    # return in this order
    return a_out,f1_out,b_out,f2_out,c_out,d_out,f3_out

x=float(input("enter the learning rate : "))
y=float(input("enter the max iterations : "))
a_out,f1_out,b_out,f2_out,c_out,d_out,f3_out=A3_MatricNumber(x,y)

print(f"a_out : {a_out},\nf1_out : {f1_out}, \nb_out : {b_out}, \nf2_out : {f2_out}, \nc_out : {c_out}, \nd_out : {d_out}, \nf3_out : {f3_out}")



















