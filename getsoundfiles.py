from os import listdir
from os.path import isfile,join
def getsoundfiles(tring):
   onlyfiles=[f for f in listdir("./"+tring) if isfile(join("./"+tring,f))]
   return onlyfiles

x=getsoundfiles("test")

