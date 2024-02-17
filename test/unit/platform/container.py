import unittest
from src.core.application.crudContainer import create, delete
class TestPlatformCrud(unittest.TestCase):
    def test_create_container_success(self):
        res=create(image="debian", command="echo hi", name="milad") 
        self.assertEqual("created", res['status'] if isinstance(res, dict) else res.status)

    def test_create_container_fail(self):
        res=create(image="unkown", command="echo hi2")        
        self.assertEqual("failed", res['status'] if isinstance(res, dict) else res.status)

    def test_delete_platform(self):
        res=delete("milad")
        self.assertEqual(None, res)

if __name__ == '__main__':
    unittest.main()