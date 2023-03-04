import FantasyBaseballTrends as fbt
import unittest
from unittest.mock import patch, MagicMock
from pandas.testing import assert_frame_equal
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestFunctions(unittest.TestCase):

    #make a setup
    def setUp(self):

        options = webdriver.ChromeOptions()
        #options.add_argument('headless')
        # options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://www.baseball-reference.com/")

        

    #test to see if the projected stats exist and returns data Frame
    def test_get2023Projected(self):
            self.assertEqual(type(fbt.get2023Projected(self.driver, "Aaron Judge")), pd.DataFrame)

    #test to see if last game stats exist
    def test_getLastGame(self):
        self.assertEqual(type(fbt.getLastGame(self.driver, "Aaron Judge")), pd.DataFrame)

    #assert that only one row is returned 
    def test_getLastGameShape(self):
        self.assertEqual(fbt.getLastGame(self.driver, "Mike Trout").shape[0], 1)

    #test to see if Rhp Current stats exist
    def test_getRhpCurrent(self):
        self.assertEqual(type(fbt.getVsRhpCurrent(self.driver, "Aaron Judge")), pd.DataFrame)

    #test to see if Lhp Current stats exist
    def test_getLhpCurrent(self):
        self.assertEqual(type(fbt.getVsLhpCurrent(self.driver, "Aaron Judge")), pd.DataFrame)

    #test to see if carreer splits log exists 
    def test_getCareerSplits(self):
        self.assertEqual(type(fbt.getCareerSplits(self.driver, "Aaron Judge")), pd.DataFrame)


    def test_intget2023Projected(self):
        testFrame = pd.read_csv('./testingFiles/AaronJudgeProj.csv', index_col=0)
        assert_frame_equal(fbt.get2023Projected(self.driver, "Aaron Judge"), testFrame)

    def test_intgetLastGame(self):
        testFrame = pd.read_csv('./testingFiles/JudgeLastGame.csv', index_col=0, dtype=str)
        assert_frame_equal(fbt.getLastGame(self.driver, "Aaron Judge"), testFrame, check_dtype=False)
    
    def test_intgetRhpCurrent(self):
        testFrame = pd.read_csv('./testingFiles/JudgeRhpCurrent.csv', index_col=0)
        assert_frame_equal(fbt.getVsRhpCurrent(self.driver, "Aaron Judge"), testFrame)

    def test_intgetLhpCurrent(self):
        testFrame = pd.read_csv('./testingFiles/JudgeLhpCurrent.csv', index_col=0)
        assert_frame_equal(fbt.getVsLhpCurrent(self.driver, "Aaron Judge"), testFrame)
    
    def test_intgetCarrerSplits(self):
        testFrame = pd.read_csv('./testingFiles/JudgeCareerSplits.csv', index_col=0)
        assert_frame_equal(fbt.getCareerSplits(self.driver, "Aaron Judge"), testFrame)

    def test_intgetLastxGames1(self):
        testFrame = pd.read_csv('./testingFiles/JudgeLast5.csv', index_col=0, dtype = str)
        assert_frame_equal(fbt.getLastxGames(self.driver, "Aaron Judge", 5), testFrame, check_dtype=False)

    def test_intgetLastxGames2(self):
        testFrame = pd.read_csv('./testingFiles/JudgeLast10.csv', index_col=0, dtype = str)
        assert_frame_equal(fbt.getLastxGames(self.driver, "Aaron Judge", 10), testFrame, check_dtype=False)

    #make a teardown 
    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()
