class Limpieza:
    
    def __init__ (self):
       
        self.limpio=''
        import os
        import time 
        if os.name == "posix":
            var = "clear"        
        elif os.name == "ce" or os.name == "nt" or os.name == "dos":
            var = "cls"
        time.sleep(1)
        os.system(var)
    def clean(self):
        self.limpio
limpieza1= Limpieza()
    