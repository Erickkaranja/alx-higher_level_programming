class MyTestCase(unittest.TestCase):

    @unittest.skip("Demonstrating skip")
    def test_nothing(self):
        self.fail("should happen")

    @unittest.skipIf(mylib.__version__ < (1, 3), "not supported in the library\
        version")

    def test_format(self):
        #tests that works for a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires windows")

    def test_windows_support(self):
        #windows specific testing code 
    pass
