class Asset:
    def __init__(self, asset_type, asset_name):
        self.asset_type = asset_type
        self.asset_name = asset_name

    def __str__(self):
        return f"{self.asset_type}: {self.asset_name}"
