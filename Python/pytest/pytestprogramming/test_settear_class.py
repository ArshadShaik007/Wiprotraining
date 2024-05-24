class TestClass:

    def setup_class(cls):
        print("Api connection is opened")
    def teardown_class(cls):
        print("API connection is closed")
    def setup_method(self,method):
        print("open browser")
    def teardown_method(self,method):
        print("close browser")

    def testcase01(self):
        print("testcase 1")

    # test case 2
    def testcase2(self):
        print("testcase 2")

    # test case 3
    def testcase3(self):
        print("testcase 3")