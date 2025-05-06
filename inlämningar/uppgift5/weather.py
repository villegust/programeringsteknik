import csv

class Temperature:
    def __init__(self,filename):
        self.filename = filename
        self.temp_data = {}

        with open(filename,"r",encoding="utf-8") as csvFile:
            reader = csv.reader(csvFile,delimiter=";")

            for _ in range(8):
                next(reader)

            for count, row in enumerate(reader):
                date = row[0]        # Formaterar datum till: yyyy-mm-dd
                time = row[1][:2]    # Tar bara timmen och skippar mm:ss
                key = f"{date} {time}"
                value = float(row[2].replace(",", "."))  # Byt ut komma till punkt för float
                self.temp_data[key] = value

        self.number_of_datapoints = count
        self.temperature = list(self.temp_data.values())
        self.time=list(self.temp_data.keys())

    def __str__(self):
        """
        Utskriften ger filens namn samt hur många datapunkter den har.
        """
        return f"Filens namn: {self.filename} och den har {len(self.temp_data)} st datapunkter. "

    
    def smoothing(self, hours):
        """
        Smooting över flera timmar
        """
        smooth_data=[]

        for i in range(len(self.temperature)):
            smooth_data.append(sum(self.temperature[max(0, i - hours):min(len(self.temperature), i + hours + 1)]) / (min(len(self.temperature), i + hours + 1) - max(0, i - hours)))
        
        return smooth_data
    
    def max_value(self):
        """
        Funktion som tar fram max-värde samt vilket dautm det inträffade
        """
        max_index = self.temperature.index(max(self.temperature))
    
        # Hämta max-värde och tillhörande tidpunkt
        max_data = self.temperature[max_index]
        max_data_time = self.time[max_index]

        return max_data, max_data_time
    
    def min_value(self):        
        """
        Funktion som tar fram min-värde samt vilket dautm det inträffade
        """
        min_index = self.temperature.index(min(self.temperature))
    
        # Hämta min-värde och tillhörande tidpunkt
        min_data = self.temperature[min_index]
        min_data_time = self.time[min_index]

        return min_data, min_data_time
