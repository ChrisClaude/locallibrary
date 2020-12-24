from django.test import TestCase


class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        # This method is called once at the beginning of the test run for class-level setup. You'd use this to create
        # objects that aren't going to be modified or changed in any of the test methods.
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        #  This method is called before every test function to set up any objects that may be modified
        #  by the test (every test function will get a "fresh" version of these objects).
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)