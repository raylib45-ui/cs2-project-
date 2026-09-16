    def calculate_tier1_efficiency(self, player_id, map_name):
        """Tier 1: Core Efficiency (~50% weight)"""
        df = self.historical_data[
            (self.historical_data["player_id"] == player_id) & 
            (self.historical_data["map"] == map_name)
        ]
        if df.empty:
            return None, None, None

        base_kpr = df["kpr"].mean()
        base_adr = df["adr"].mean()
        base_impact = df["impact_rating"].mean()
        return base_kpr, base_adr, base_impact

    def calculate_tier2_volatility(self, player_id, map_name):
        """Tier 2: Role & Volatility (~30% weight)"""
        df = self.historical_data[
            (self.historical_data["player_id"] == player_id) & 
            (self.historical_data["map"] == map_name)
        ]
        if df.empty:
            return 0.5, 0.0

        entry_win_rate = df["opening_duel_win_rate"].mean()
        awp_kpr = df["awp_kills_per_round"].mean()
        return entry_win_rate, awp_kpr
