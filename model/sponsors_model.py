from utility.common import common


class sponsors_model:
    def __init__(self):
        common.conn_setup(self)

    def sponsors_list_model(self):
        return "Sponsors Model"
