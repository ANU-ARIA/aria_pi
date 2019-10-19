class socket():
    def __init__(self):
        print("")
    
    def Send_to_MES(self, sMessage):
        print("")

    def Rec_from_MES(self, rMessage):    
        print("")

class connection_MES():
    def __init__(self, getReceived_data_count):
        self. getReceived_data_count = getReceived_data_count

    def isConnected(self):
        print("")
    def connect(self):
        print("")
    def disConnect(self):
        print("")
    def pop_item(self):
        print("")

class Rpi_data():

    def __init__(self, cur_lot_id, cur_barcode, product_state, fail_reason, work_start_time, cur_temp, cur_humidity):
        self.cur_lot_id = cur_lot_id
        self.cur_barcode = cur_barcode
        self.product_state = product_state
        self.fail_reason = fail_reason
        self.work_start_time = work_start_time
        self.cur_temp = cur_temp
        self.cur_humidity = cur_humidity

    



