class Calculator :

    def __init__(self,input_field,result_label):
        self.result_label = result_label
        self.input_field = input_field


    def miles_to_km(self,miles):
        return round(miles * 1.60934, 2)


    def convert(self):
        mile = float(self.input_field.get())
        kilometers = self.miles_to_km(mile)
        self.result_label.config(text=str(kilometers))