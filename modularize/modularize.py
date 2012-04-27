'''
Created on Apr 26, 2012

@author: cjh
'''
class Module:
    def __init__(self, name, depends, test_depends):
       self.name = name
       self.depends = depends
       self.test_depends = test_depends
    def __str__(self):
        return name
        
parameter_names = [COMPILE_DEPENDS, TEST_DEPENDS, DEPENDS, DESCRIPTION, IMPLEMENTS, DEFAULT, GROUPS]

class ModuleCmakeParser:
   def __init__(self):
     """"""
   def parse(self, module_cmake):
      with open(module_cmake) as f:
        module_string = f.read()
        
       parameter_string = re.match(r".*vtk_module\(.*\).*").group(1)
       parameters = re.compile("(\s)").split(parameters)
       
       it = iter(parameters)
       parameter_list = {}
       for parameter in it:
          if parameter in parameter_names:
             
             if current_parameter != None:
                parameter_list[current_parameter] = parameter_values
          else:
               parameter_value.append(parameter)
