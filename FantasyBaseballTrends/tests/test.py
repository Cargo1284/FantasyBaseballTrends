import FantasyBaseballTrends as fbt
import unittest
from pandas.testing import assert_frame_equal
import pandas as pd
from selenium import webdriver


class TestFunctions(unittest.TestCase):
    # make a setup
    def setUp(self):
        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        # options.page_load_strategy = 'eager'
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://www.baseball-reference.com/")

    # test to see if the projected stats exist and returns data Frame
    def test_get2023Season(self):
        self.assertEqual(
            type(fbt.get2023Season(self.driver, "Aaron Judge")),
            pd.DataFrame,
        )
    
    def test_getCareer(self):
        self.assertEqual(
            type(fbt.getCareer(self.driver, "Aaron Judge")),
            pd.DataFrame,
        )
    
    def test_getPostseasonStats(self):
            self.assertEqual(
                type(fbt.getPostseasonStats(self.driver, "Aaron Judge")),
                pd.DataFrame,
            )

    # test to see if last game stats exist
    def test_getLastGame(self):
        self.assertEqual(
            type(fbt.getLastGame(self.driver, "Aaron Judge")), pd.DataFrame
        )

    # assert that only one row is returned
    def test_getLastGameShape(self):
        self.assertEqual(
            fbt.getLastGame(self.driver, "Mike Trout").shape[0], 1
        )

    # test to see if Rhp Current stats exist
    def test_getRhpCurrent(self):
        self.assertEqual(
            type(fbt.getVsRhpCurrent(self.driver, "Aaron Judge")), pd.DataFrame
        )

    # test to see if Lhp Current stats exist
    def test_getLhpCurrent(self):
        self.assertEqual(
            type(fbt.getVsLhpCurrent(self.driver, "Aaron Judge")), pd.DataFrame
        )

    # test to see if carreer splits log exists
    def test_getCareerSplits(self):
        self.assertEqual(
            type(fbt.getCareerSplits(self.driver, "Aaron Judge")), pd.DataFrame
        )

    def test_intget2023Season(self):
        testFrame = pd.read_csv(
            'FantasyBaseballTrends/tests/AaronJudgeSeason.csv', index_col=0
        )
        assert_frame_equal(
            fbt.get2023Season(self.driver, "Aaron Judge"), testFrame
        )

    def test_intgetLastGame(self):
        testFrame = pd.read_csv(
            'FantasyBaseballTrends/tests/JudgeLastGame.csv',
            index_col=0,
            dtype=str,
        )
        assert_frame_equal(
            fbt.getLastGame(self.driver, "Aaron Judge"),
            testFrame,
            check_dtype=False,
        )

    def test_intgetPostseason(self):
        testFrame = pd.read_csv(
            'FantasyBaseballTrends/tests/AaronJudgePostseason.csv', index_col=0
        )
        assert_frame_equal(
            fbt.getPostseasonStats(self.driver, "Aaron Judge"), testFrame
        )
    
    def test_intgetCareer(self):
        testFrame = pd.read_csv(
            'FantasyBaseballTrends/tests/AaronJudgeCareer.csv', index_col=0
        )
        assert_frame_equal(
            fbt.getCareer(self.driver, "Aaron Judge"), testFrame
        )

    def test_intgetRhpCurrent(self):
        testFrame = pd.read_csv(
            'FantasyBaseballTrends/tests/JudgeRhpCurrent.csv', index_col=0
        )
        assert_frame_equal(
            fbt.getVsRhpCurrent(self.driver, "Aaron Judge"), testFrame
        )

    def test_intgetLhpCurrent(self):
        testFrame = pd.read_csv(
            'FantasyBaseballTrends/tests/JudgeLhpCurrent.csv', index_col=0
        )
        assert_frame_equal(
            fbt.getVsLhpCurrent(self.driver, "Aaron Judge"), testFrame
        )

    def test_intgetCarrerSplits(self):
        testFrame = pd.read_csv(
            'FantasyBaseballTrends/tests/JudgeCareerSplits.csv', index_col=0
        )
        assert_frame_equal(
            fbt.getCareerSplits(self.driver, "Aaron Judge"), testFrame
        )

    def test_intgetLastxGames1(self):
        testFrame = pd.read_csv(
            'FantasyBaseballTrends/tests/JudgeLast5.csv',
            index_col=0,
            dtype=str,
        )
        assert_frame_equal(
            fbt.getLastxGames(self.driver, "Aaron Judge", 5),
            testFrame,
            check_dtype=False,
        )

    def test_intgetLastxGames2(self):
        testFrame = pd.read_csv(
            'FantasyBaseballTrends/tests/JudgeLast10.csv',
            index_col=0,
            dtype=str,
        )
        assert_frame_equal(
            fbt.getLastxGames(self.driver, "Aaron Judge", 10),
            testFrame,
            check_dtype=False,
        )

    def test_intgetAvgOverLastxGames(self):
        testFrame = pd.read_csv(
            'FantasyBaseballTrends/tests/JudgeLast10Avg.csv',
            index_col=0,
            dtype=str,
        )
        assert_frame_equal(
            fbt.getAvgOverLastxGames(self.driver, "Aaron Judge", 10),
            testFrame,
            check_dtype=False,
        )

    # make a teardown
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
