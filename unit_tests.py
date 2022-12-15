import unittest

from lab_python_fp.process_data import f1
from lab_python_fp.unique import Unique

# testing f1 from process_data.py
class Test_Process_Data_F1(unittest.TestCase):
    def setUp(self):
        self.data = [
            {"job-name" : "street-photographer"}, 
            {"job-name" : "developer"} ,
            {"job-name" : "developer"}, 
            {"job-name" : "tatoo-master"}
        ]
        self.supposed_result = [
            "developer",
            "street-photographer",
            "tatoo-master"
        ] 

    def test(self):
        res = f1(self.data)
        self.assertEqual(res, self.supposed_result)

# testing Unique from unique.py
class Test_Unique(unittest.TestCase):
    def test_same_object(self):
        data = ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']
        res = list(Unique(data))
        supposed_res = ['a']
        self.assertEqual(res, supposed_res)

    def test_base(self):
        data = [1, 1, 1, 1, 1, 2, 2, 1, 1, 2, 3, 'A', 3, 'a', '1567', 1567, 'yooo']
        res = list(Unique(data))
        supposed_res = [1, 2, 3, 'A', 'a', '1567', 1567, 'yooo']
        self.assertEqual(res, supposed_res)

    def test_ignore_case(self):
        data = ['aBC', 'ABc', 'aBc', 'abc', 'ABC']
        res = list(Unique(data, ignore_case=True))
        supposed_res = ['aBC']
        self.assertEqual(res, supposed_res)

if __name__ == '__main__':
    unittest.main()
