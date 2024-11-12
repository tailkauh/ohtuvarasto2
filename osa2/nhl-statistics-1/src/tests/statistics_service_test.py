import unittest
from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 32, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):
    
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_init(self):
        self.assertEqual(hasattr(self.stats, "_players"), True)

    def test_search_puuttuva_nimi(self):
        self.assertEqual(self.stats.search("!#¤%&/()="), None)

    def test_search_koko_nimi(self):
        self.assertEqual(self.stats.search("Kurri").__str__(), "Kurri EDM 32 + 53 = 85") 
