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
            type(fbt.get2023Season(self.driver, "Yadier Molina")),
            pd.DataFrame,
        )

    def test_getCareer(self):
        self.assertEqual(
            type(fbt.getCareer(self.driver, "Yadier Molina")),
            pd.DataFrame,
        )

    def test_getPostseasonStats(self):
        self.assertEqual(
            type(fbt.getPostseasonStats(self.driver, "Yadier Molina")),
            pd.DataFrame,
        )

    # test to see if last game stats exist
    def test_getLastGame(self):
        self.assertEqual(
            type(fbt.getLastGame(self.driver, "Yadier Molina")), pd.DataFrame
        )

    # assert that only one row is returned
    def test_getLastGameShape(self):
        self.assertEqual(
            fbt.getLastGame(self.driver, "Yadier Molina").shape[0], 1
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
            'FantasyBaseballTrends/tests/MolinaSeason.csv', index_col=0
        )
        assert_frame_equal(
            fbt.get2023Season(self.driver, "Yadier Molina"),
            testFrame,
            check_dtype=False,
        )

    def test_intgetLastGame(self):
        testFrame = pd.read_csv(
            'FantasyBaseballTrends/tests/MolinaLastGame.csv',
            index_col=0,
            dtype=str,
        )
        testFrame = testFrame.astype(str)
        actualFrame = fbt.getLastGame(self.driver, "Yadier Molina")
        actualFrame = actualFrame.astype(str)
        assert_frame_equal(actualFrame, testFrame, check_dtype=False)

    def test_intgetPostseason(self):
        testFrame = pd.read_csv(
            'FantasyBaseballTrends/tests/MolinaPostseason.csv', index_col=0
        )
        testFrame = testFrame.astype(str)
        actualFrame = fbt.getPostseasonStats(self.driver, "Yadier Molina")
        actualFrame = actualFrame.astype(str)
        assert_frame_equal(actualFrame, testFrame, check_dtype=False)

    def test_intgetCareer(self):
        testFrame = pd.read_csv(
            'FantasyBaseballTrends/tests/MolinaCareer.csv', index_col=0
        )
        assert_frame_equal(
            fbt.getCareer(self.driver, "Yadier Molina"),
            testFrame,
            check_dtype=False,
        )

    def test_intgetRhpCurrent(self):
        testFrame = pd.read_csv(
            'FantasyBaseballTrends/tests/MolinaRhpCurrent.csv', index_col=0
        )
        assert_frame_equal(
            fbt.getVsRhpCurrent(self.driver, "Yadier Molina"), testFrame
        )

    def test_intgetLhpCurrent(self):
        testFrame = pd.read_csv(
            'FantasyBaseballTrends/tests/MolinaLhpCurrent.csv', index_col=0
        )
        assert_frame_equal(
            fbt.getVsLhpCurrent(self.driver, "Yadier Molina"), testFrame
        )

    def test_intgetCarrerSplits(self):
        testFrame = pd.read_csv(
            'FantasyBaseballTrends/tests/MolinaCarrerSplits.csv', index_col=0
        )
        assert_frame_equal(
            fbt.getCareerSplits(self.driver, "Yadier Molina"), testFrame
        )

    def test_intgetLastxGames1(self):
        testFrame = pd.read_csv(
            'FantasyBaseballTrends/tests/MolinaLast5.csv',
            index_col=0,
            dtype=str,
        )
        testFrame = testFrame.astype(str)
        actualFrame = fbt.getLastxGames(self.driver, "Yadier Molina", 5)
        actualFrame = actualFrame.astype(str)
        assert_frame_equal(
            actualFrame,
            testFrame,
            check_dtype=False,
        )

    def test_intgetLastxGames2(self):
        testFrame = pd.read_csv(
            'FantasyBaseballTrends/tests/MolinaLast10.csv',
            index_col=0,
            dtype=str,
        )
        testFrame = testFrame.astype(str)
        actualFrame = fbt.getLastxGames(self.driver, "Yadier Molina", 10)
        actualFrame = actualFrame.astype(str)
        assert_frame_equal(
            actualFrame,
            testFrame,
            check_dtype=False,
        )

    def test_intgetAvgOverLastxGames(self):
        self.assertEqual(
            type(fbt.getAvgOverLastxGames(self.driver, "Aaron Judge", 10)),
            pd.DataFrame,
        )

    # make a teardown
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
