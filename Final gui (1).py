import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox 
import math
from math import sin


class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'Venturimeter', width = 25, command = self.new_window)
        self.button1.pack()
        self.button2 = tk.Button(self.frame, text = 'Orificemeter', width = 25, command = self.new_window1)
        self.button2.pack()
        self.frame.pack()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)   
        self.app = ven_position(self.newWindow)
    def new_window1(self):
        self.newWindow1 = tk.Toplevel(self.master)
        self.app = Orifice(self.newWindow1)    
        

class Ven_horizontal:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.geometry("500x500")
     
        self.label=tk.Label(self.frame,text="coefficient of discharge",font=("Ariel",16))
        self.label.pack()
      
        self.v_var=tk.StringVar()
        self.v_cod=tk.Entry(self.frame,width=60,textvariable=self.v_var)
        self.v_cod.pack()
        
        self.label=tk.Label(self.frame,text="diameter of inlet",font=("Ariel",16))
        self.label.pack()
        self.v_var=tk.StringVar()
        self.v_doi=tk.Entry(self.frame,width=60,textvariable=self.v_var)
        self.v_doi.pack()
        
        self.label=tk.Label(self.frame,text="diameter of throat",font=("Ariel",16))
        self.label.pack()
        self.v_var=tk.StringVar()
        self.v_dot=tk.Entry(self.frame,width=60,textvariable=self.v_var)
        self.v_dot.pack()
        
        self.label=tk.Label(self.frame,text="length of venturimeter",font=("Ariel",16))
        self.label.pack()
        self.v_var=tk.StringVar()
        self.v_h=tk.Entry(self.frame,width=60,textvariable=self.v_var)
        self.v_h.pack()
        
        self.label=tk.Label(self.frame,text="pressure at inlet",font=("Ariel",16))
        self.label.pack()
        self.v_var=tk.StringVar()
        self.v_p_inlet=tk.Entry(self.frame,width=60,textvariable=self.v_var)
        self.v_p_inlet.pack()
        
        self.label=tk.Label(self.frame,text="pressure at throat",font=("Ariel",16))
        self.label.pack()
        self.v_var=tk.StringVar()
        self.v_p_throat=tk.Entry(self.frame,width=60,textvariable=self.v_var)
        self.v_p_throat.pack()
        
        self.label=tk.Label(self.frame,text="specific weight of the liquid",font=("Ariel",16))
        self.label.pack()
        self.v_var=tk.StringVar()
        self.v_p_gamma=tk.Entry(self.frame,width=60,textvariable=self.v_var)
        self.v_p_gamma.pack()
        
             
        self.label=tk.Label(self.frame,text="angle of inclinnation",font=("Ariel",16))
        self.label.pack()
        self.v_var=tk.StringVar()
        self.v_p_angle=tk.Entry(self.frame,width=60,textvariable=self.v_var)
        self.v_p_angle.pack()
        
        
        self.label=tk.Label(self.frame,text="discharge",font=("Ariel",16))
        self.label.pack()
        self.v_2=tk.StringVar()
        self.v_2.set("")
        self.v_discharge=tk.Entry(self.frame,width=60,textvariable=self.v_2)
        self.v_discharge.pack()
        
        self.calculate = tk.Button(self.frame, text = 'Calculate', width = 25, command = self.venturi_discharge)
        self.calculate.pack()
        self.frame.pack()
        
    
        

    def venturi_discharge(self):
        
            
        cod=self.v_cod.get()
        cod=float(cod)
        dof_inlet=self.v_doi.get()
        dof_inlet=float(dof_inlet)
        dof_throat=self.v_dot.get()
        dof_throat=float(dof_throat)
        
        areaof_inlet=0.7853*dof_inlet*dof_inlet
        areaof_throat=0.7853*dof_throat*dof_throat
        p1=self.v_p_inlet.get()
        p1=float(p1)
        p2=self.v_p_throat.get()
        p2=float(p2)
        sw=self.v_p_gamma.get()
        sw=float(sw)
        height=self.v_h.get()
        height=float(height)
        angle=self.v_p_angle.get()
        angle=float(angle)
        z=height*(math.sin(angle))
        h=(p1-p2)/sw+z
        a=(2*9.8*h)**0.5
        b=(areaof_inlet*areaof_inlet)-(areaof_throat*areaof_throat)
        c=cod*areaof_throat*areaof_inlet*a
        d=b**0.5
        q=c/d
        self.v_2.set(str(q))
        self.v_discharge.update()
        
            
            

class Ven_vertical:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.geometry("500x500")
      
        
        self.label=tk.Label(self.frame,text="coefficient of discharge",font=("Ariel",16))
        self.label.pack()
        self.v_var=tk.StringVar()
        self.v_cod=tk.Entry(self.frame,width=60,textvariable=self.v_var)
        self.v_cod.pack()
        
        self.label=tk.Label(self.frame,text="diameter of inlet",font=("Ariel",16))
        self.label.pack()
        self.v_var=tk.StringVar()
        self.v_doi=tk.Entry(self.frame,width=60,textvariable=self.v_var)
        self.v_doi.pack()
        
        self.label=tk.Label(self.frame,text="diameter of throat",font=("Ariel",16))
        self.label.pack()
        self.v_var=tk.StringVar()
        self.v_dot=tk.Entry(self.frame,width=60,textvariable=self.v_var)
        self.v_dot.pack()
        
        self.label=tk.Label(self.frame,text="angle of inclination",font=("Ariel",16))
        self.label.pack()
        self.v_var=tk.StringVar()
        self.v_angle=tk.Entry(self.frame,width=60,textvariable=self.v_var)
        self.v_angle.pack()
        
        self.label=tk.Label(self.frame,text="manometric reading",font=("Ariel",16))
        self.label.pack()
        self.v_var=tk.StringVar()
        self.v_man=tk.Entry(self.frame,width=60,textvariable=self.v_var)
        self.v_man.pack()
        
        self.label=tk.Label(self.frame,text="specific gravity of manometric liquid",font=("Ariel",16))
        self.label.pack()
        self.v_var=tk.StringVar()
        self.v_sm=tk.Entry(self.frame,width=60,textvariable=self.v_var)
        self.v_sm.pack()
        
        self.label=tk.Label(self.frame,text="specific gravity of the flowing liquid",font=("Ariel",16))
        self.label.pack()
        self.v_var=tk.StringVar()
        self.v_s=tk.Entry(self.frame,width=60,textvariable=self.v_var)
        self.v_s.pack()
        
        self.label=tk.Label(self.frame,text="discharge",font=("Ariel",16))
        self.label.pack()
        self.v_2=tk.StringVar()
        self.v_2.set("")
        self.v_discharge=tk.Entry(self.frame,width=60,textvariable=self.v_2)
        self.v_discharge.pack()
        
        self.calculate = tk.Button(self.frame, text = 'Calculate', width = 25, command = self.venturi_discharge1)
        self.calculate.pack()
        self.frame.pack()
        
    
        

    def venturi_discharge1(self):
         
        
        cod=self.v_cod.get()
        cod=float(cod)
        dof_inlet=self.v_doi.get()
        dof_inlet=float(dof_inlet)
        dof_throat=self.v_dot.get()
        dof_throat=float(dof_throat)
        x=self.v_man.get()
        x=float(x)
        s=self.v_s.get()
        s=float(s)
        sm=self.v_sm.get()
        sm=float(sm)
        aoi=0.7853*(dof_inlet)*(dof_inlet)
        aot=0.7853*(dof_throat)*(dof_throat)
        a=sm/s-1
        h=x*a
        p=(2*9.8*h)**0.5
        b=(aoi*aoi)-(aot*aot)
        c=cod*aoi*aot*p
      
        d=b**0.5
        q=c/d
        self.v_2.set(str(q))
        self.v_discharge.update()                
            
class ven_position:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'mechanical gauge ', width = 25, command = self.new_window)
        self.button1.pack()
        self.button2 = tk.Button(self.frame, text = 'manometer', width = 25, command = self.new_window1)
        self.button2.pack()
        
        
        self.frame.pack()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)   
        self.app = Ven_horizontal(self.newWindow)
    def new_window1(self):
        self.newWindow1 = tk.Toplevel(self.master)
        self.app = Ven_vertical(self.newWindow1)    

  
    
    
    
    
    
                
class Orifice:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.button1 = tk.Button(self.frame, text = 'mechanical gauge ', width = 25, command = self.new_window)
        self.button1.pack()
        self.button2 = tk.Button(self.frame, text = 'manometer', width = 25, command = self.new_window1)
        self.button2.pack()
        
        
        self.frame.pack()

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)   
        self.app = ori_horizontal(self.newWindow)
    def new_window1(self):
        self.newWindow1 = tk.Toplevel(self.master)
        self.app = ori_vertical(self.newWindow1)    

class ori_vertical:
    def __init__(self,master):
        
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.geometry("500x500")
      
        
        self.label=tk.Label(self.frame,text="coefficient of discharge",font=("Ariel",16))
        self.label.pack()
        self.v_var=tk.StringVar()
        self.v_cod=tk.Entry(self.frame,width=60,textvariable=self.v_var)
        self.v_cod.pack()
        
        self.label=tk.Label(self.frame,text="diameter of inlet",font=("Ariel",16))
        self.label.pack()
        self.v_var=tk.StringVar()
        self.v_doi=tk.Entry(self.frame,width=60,textvariable=self.v_var)
        self.v_doi.pack()
        
        self.label=tk.Label(self.frame,text="diameter of vena contracta",font=("Ariel",16))
        self.label.pack()
        self.v_var=tk.StringVar()
        self.v_dot=tk.Entry(self.frame,width=60,textvariable=self.v_var)
        self.v_dot.pack()
        
        self.label=tk.Label(self.frame,text="angle of inclination",font=("Ariel",16))
        self.label.pack()
        self.v_var=tk.StringVar()
        self.v_angle=tk.Entry(self.frame,width=60,textvariable=self.v_var)
        self.v_angle.pack()
        
        self.label=tk.Label(self.frame,text="manometric reading",font=("Ariel",16))
        self.label.pack()
        self.v_var=tk.StringVar()
        self.v_man=tk.Entry(self.frame,width=60,textvariable=self.v_var)
        self.v_man.pack()
        
        self.label=tk.Label(self.frame,text="specific gravity of manometric liquid",font=("Ariel",16))
        self.label.pack()
        self.v_var=tk.StringVar()
        self.v_sm=tk.Entry(self.frame,width=60,textvariable=self.v_var)
        self.v_sm.pack()
        
        self.label=tk.Label(self.frame,text="specific gravity of the flowing liquid",font=("Ariel",16))
        self.label.pack()
        self.v_var=tk.StringVar()
        self.v_s=tk.Entry(self.frame,width=60,textvariable=self.v_var)
        self.v_s.pack()
        
        self.label=tk.Label(self.frame,text="discharge",font=("Ariel",16))
        self.label.pack()
        self.v_2=tk.StringVar()
        self.v_2.set("")
        self.v_discharge=tk.Entry(self.frame,width=60,textvariable=self.v_2)
        self.v_discharge.pack()
        
        self.calculate = tk.Button(self.frame, text = 'Calculate', width = 25, command = self.orifice_discharge1)
        self.calculate.pack()
        self.frame.pack()
        
        
    def orifice_discharge1(self):
        cod=self.v_cod.get()
        cod=float(cod)
        dof_inlet=self.v_doi.get()
        dof_inlet=float(dof_inlet)
        dof_throat=self.v_dot.get()
        dof_throat=float(dof_throat)
        x=self.v_man.get()
        x=float(x)
        s=self.v_s.get()
        s=float(s)
        sm=self.v_sm.get()
        sm=float(sm)
        aoi=0.7853*(dof_inlet)*(dof_inlet)
        aot=0.7853*(dof_throat)*(dof_throat)
        a=sm/s-1
        h=x*a
        p=(2*9.8*h)**0.5
        b=(aoi*aoi)-(aot*aot)
        c=cod*aoi*aot*p
      
        d=b**0.5
        q=c/d
        self.v_2.set(str(q))
        self.v_discharge.update()  
class ori_horizontal:
    def __init__(self,master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.geometry("500x500")
     
        self.label=tk.Label(self.frame,text="coefficient of discharge",font=("Ariel",16))
        self.label.pack()
      
      
      
        self.v_var=tk.StringVar()
        self.v_cod=tk.Entry(self.frame,width=60,textvariable=self.v_var)
        self.v_cod.pack()
        
        self.label=tk.Label(self.frame,text="diameter of inlet",font=("Ariel",16))
        self.label.pack()
        self.v_var=tk.StringVar()
        self.v_doi=tk.Entry(self.frame,width=60,textvariable=self.v_var)
        self.v_doi.pack()
        
        self.label=tk.Label(self.frame,text="diameter of vena contracta",font=("Ariel",16))
        self.label.pack()
        self.v_var=tk.StringVar()
        self.v_dot=tk.Entry(self.frame,width=60,textvariable=self.v_var)
        self.v_dot.pack()
        
        self.label=tk.Label(self.frame,text="length of orifice meter",font=("Ariel",16))
        self.label.pack()
        self.v_var=tk.StringVar()
        self.v_h=tk.Entry(self.frame,width=60,textvariable=self.v_var)
        self.v_h.pack()
        
        self.label=tk.Label(self.frame,text="pressure at inlet",font=("Ariel",16))
        self.label.pack()
        self.v_var=tk.StringVar()
        self.v_p_inlet=tk.Entry(self.frame,width=60,textvariable=self.v_var)
        self.v_p_inlet.pack()
        
        self.label=tk.Label(self.frame,text="pressure at throat",font=("Ariel",16))
        self.label.pack()
        self.v_var=tk.StringVar()
        self.v_p_throat=tk.Entry(self.frame,width=60,textvariable=self.v_var)
        self.v_p_throat.pack()
        
        self.label=tk.Label(self.frame,text="specific weight of the liquid",font=("Ariel",16))
        self.label.pack()
        self.v_var=tk.StringVar()
        self.v_p_gamma=tk.Entry(self.frame,width=60,textvariable=self.v_var)
        self.v_p_gamma.pack()
        
             
        self.label=tk.Label(self.frame,text="angle of inclinnation",font=("Ariel",16))
        self.label.pack()
        self.v_var=tk.StringVar()
        self.v_p_angle=tk.Entry(self.frame,width=60,textvariable=self.v_var)
        self.v_p_angle.pack()
        
        
        self.label=tk.Label(self.frame,text="discharge",font=("Ariel",16))
        self.label.pack()
        self.v_2=tk.StringVar()
        self.v_2.set("")
        self.v_discharge=tk.Entry(self.frame,width=60,textvariable=self.v_2)
        self.v_discharge.pack()
        
        self.calculate = tk.Button(self.frame, text = 'Calculate', width = 25, command = self.orifice_discharge)
        self.calculate.pack()
        self.frame.pack()
    def orifice_discharge(self):
        cod=self.v_cod.get()
        cod=float(cod)
        dof_inlet=self.v_doi.get()
        dof_inlet=float(dof_inlet)
        dof_throat=self.v_dot.get()
        dof_throat=float(dof_throat)
        
        areaof_inlet=0.7853*dof_inlet*dof_inlet
        areaof_throat=0.7853*dof_throat*dof_throat
        p1=self.v_p_inlet.get()
        p1=float(p1)
        p2=self.v_p_throat.get()
        p2=float(p2)
        sw=self.v_p_gamma.get()
        sw=float(sw)
        height=self.v_h.get()
        height=float(height)
        height=float(height)
        angle=self.v_p_angle.get()
        angle=float(angle)
        z=height*(math.sin(angle))
        h=(p1-p2)/sw+z
        a=(2*9.8*h)**0.5
        b=(areaof_inlet*areaof_inlet)-(areaof_throat*areaof_throat)
        c=cod*areaof_throat*areaof_inlet*a
        d=b**0.5
        q=c/d
        self.v_2.set(str(q))
        self.v_discharge.update()
        
                        
def main(): 
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()

if __name__ == '__main__':
    main()