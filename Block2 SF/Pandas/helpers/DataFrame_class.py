import statistics
  
class DataFrame():  
    def __init__(self, column, fill_value=0):  
        # Инициализируем атрибуты  
        self.column = column 
        self.fill_value = fill_value  
        # Заполним пропуски  
        self.fill_missed()  
        # Конвертируем все элементы в числа  
        self.to_float()  
          
    def fill_missed(self): #does it means with self - we mentioned any attribute in init function?
        for i,value in enumerate(self.column):  #why we`ve used "enumerate", cause "list indices must be integers 
            #or slices, not NoneType"
            if value is None or value == '':  
                self.column[i] = self.fill_value  
                  
    def to_float(self):  
        self.column = [float(value) for value in self.column]  
      
    def median(self):  
        return statistics.median(self.column)  #why apply median function to statistics?
      
    def mean(self):  
        return statistics.mean(self.column)  
      
    def deviation(self):  
        return statistics.stdev(self.column)