class Department:
    def __init__(self, name):
        self.name = name
        self.allocated_assets = []

    def allocate_asset(self, asset):
        self.allocated_assets.append(asset)
        print(f"{asset} allocated to {self.name}.")
