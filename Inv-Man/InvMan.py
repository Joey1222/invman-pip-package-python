class Inventory():
    def __init__(self):
        self.inv = {
            'item1': [-0, "air"],
            'item2': [-0, "air"],
            'item3': [-0, "air"],
            'item4': [-0, "air"],
            'item5': [-0, "air"],
        }

    def InvGetItem(self, invitem: str):
        return self.inv.get(invitem)
