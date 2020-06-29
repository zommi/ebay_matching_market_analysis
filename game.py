import numpy as np
import pandas as pd

class Game():

    def __init__(self, game):
        self._game = game.copy()
        self._buyers = np.unique(np.array(self._game['anon_byr_id']))
        self._offers = self._game.sort_values('src_cre_date', ascending = True)[['anon_thread_id','anon_byr_id','offr_type_id','status_id','offr_price', 'src_cre_date']]
        self.id_map = {}
        self._n_buyers = len(self._buyers)
        for i in range(self._n_buyers):
            self.id_map[self._buyers[i]] = i

    def get_game(self):
        return self._game.copy()


    def get_buyers(self):
        return self._buyers.copy()

    def get_offers(self):
        return self._offers.copy()

    def map_buyer(self, buyer):
        return self.id_map[buyer]

    def get_buyers_normalized(self):
        return np.array([self.map_buyer(x) for x in self._buyers])

    def get_seller_normalized(self):
        return (self._n_buyers - 1) / 2

    def sold(self):
        return len(np.array(self._game[self._game['status_id'] == 1]['anon_byr_id'])) > 0

    def get_winner(self):
        return self.id_map[np.array(self._game[self._game['status_id'] == 1]['anon_byr_id'])[0]]

    def get_winner_offer(self):
        return np.array(self._game[self._game['status_id'] == 1]['offr_price'])[0]

    def get_n_buyers(self):
        return self._n_buyers
        