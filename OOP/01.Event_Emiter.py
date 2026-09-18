class Event():
    #your code here
    def __init__(self):
        self.callbacks = []
        pass 
    def subscribe(self,fn):
        self.callbacks.append(fn)
    def unsubscribe(self,fn):
        self.callbacks.remove(fn)
    def emit(self,*args):
        for fn in self.callbacks:
            fn(*args)
