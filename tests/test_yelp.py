import json
import unittest
import yelp

# intution behind these tests is to save copies of correct output and
# use these tests once changes are made to make sure that it still produces
# correct output

#API_KEY_YELP = 

class TestReturnedDataStructures(unittest.TestCase):

    def test_get_categories(self):

        a = lambda x,y: yelp.get_categories(x, y)
        with open('tests/get_categories.json') as f:
            b = json.load(f)

        self.assertEqual(  a(API_KEY_YELP, 'en_US'), b )

    def test_business_search(self):

        a = lambda u,v,x,y: yelp.business_search(u,v,x,cat = y)
        with open('tests/business_search.json') as f:
            b = json.load(f)

        self.assertEqual( a(API_KEY_YELP, 42.27, -83.73, 'coffee'), b )

    def test_business_details(self):

        a= lambda x,y: yelp.business_details(x,y)
        with open('tests/business_details.json') as f:
            b= json.load(f)

        self.assertEqual( a(API_KEY_YELP,'c0WpyZFR3EoEBKcoY2LZ3Q'), b )


if __name__ == '__main__':
    unittest.main()
