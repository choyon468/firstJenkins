import unittest
import people_management as EmployeesClass

class Test(unittest.TestCase):
    employees = EmployeesClass.Employees()
    user_id = []
    user_name = []

    def test_0_set_name(self):
        print("Start set_name test\n")
        for i in range(4):
            name = 'name' + str(i)
            self.user_name.append(name)
            user_id = self.employees.set_name(name)
            self.user_id.append(user_id)
            self.assertIsNotNone(user_id)

    def test_1_get_name(self):
        print('Start get_name test\n')
        length = len(self.user_id)
        for i in range(length):
            # if i < length:            redundant because i is never greater than length
            self.assertEqual(self.user_name[i], self.employees.get_name(self.user_id[i]))
            # else:                     No need for else block since if statement is redundant and it never reaches else block
        print('Testing for get_name with invalid user id\n')
        self.assertEqual('There is no such user', self.employees.get_name(length)) 
            
if __name__ == "__main__":
    unittest.main()