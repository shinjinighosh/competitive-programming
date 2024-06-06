"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        id_dict = {employees[idx].id: idx for idx in range(len(employees))}
        
        def get_total(start_id):
            emp_idx = id_dict[start_id]
            res = employees[emp_idx].importance

            for sub in employees[emp_idx].subordinates:
                res += get_total(sub)
            
            return res

        return get_total(id)
