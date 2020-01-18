"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        
        """
        for employee in employees:
            if employee.id == id:
                imp = employee.importance
                for lead in employee.subordinates:
                    
                    for i in range(0,len(employees)):
                        if employees[i].id == lead:
                            imp = imp + employees[i].importance
                            for sub in employees[i].subordinates:
                                imp =imp + self.getImportance(employees,sub)
                    
        return imp
