#!/usr/bin/python
from ansible.module_utils.basic import *

class MyClass:

      #def __new__(cls, *args, **kwargs):
        return load_platform_subclass(Service, args, kwargs)  
  
      def __init__(self,module,firstnum=0,secondnum=0):
          self.module             = module
          self.firstnum           = module.params['firstnum']
          self.secondnum          = module.params['secondnum']
          self.changed            = False
      
      def printResults(self):   
          print('Value of First Number is : ', self.firstnum)
          print('Value of Second Number is : ', self.secondnum)
          
      def add(self):
          result = self.firstnum + self.secondnum
          #return self.exit_json(changed=True, msg="The sum is" + result)

def main():
          
     instance1 = MyClass()
     module = AnsibleModule( argument_spec={} )
     res = instance1.printResults()
     response = {"Result" + str(res) : + str(instance1.add() ) }

     #response = os.getuid()
    
     module.exit_json(self.changed=true, meta=response)
     #module.exit_json(**result)
   
if __name__ == "__main__":
     main()
