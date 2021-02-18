import datetime

class Entry:
    def __init__(self, date_str, text):
        self.date = self._parse_date(date_str)
        self.text = text
        
    def _parse_date(self, date_str):
        date_str = date_str.strip()
        day, month, year = map(int, date_str.split("/"))
        year += 2000
        date = datetime.datetime(year, month, day)
        return date

    def people(self):
        return self.get_symbol_names("@")
        
    def tags(self):
        return self.get_symbol_names("#")

    def get_symbol_names(self, symbol):
        names = []
        entry_temp = self.text
        for _ in range(self.text.count(symbol)):
            idx = entry_temp.index(symbol)
            entry_temp = entry_temp[idx+1:]
            
            name = entry_temp.split()[0].split(",")[0].split(".")[0]
            if len(entry_temp.split()[0]) < 2:
                name += entry_temp.split()[1].split(",")[0].split(".")[0]
            
            if not name in names: 
                names.append(name)
        return names

class Diary:
    def __init__(self):
        self.entries = []
        
    def add_entry(self, entry):
        if isinstance(entry, Entry):
            self.entries.append(entry)
        else:
            raise Exception("Has to be of class Entry, not '{}'".format(entry.__class__))
            
    def people(self):
        return self.get_symbol_names("@")
        
    def tags(self):
        return self.get_symbol_names("#")

    def get_symbol_names(self, symbol):
        names = []
        for e in self.entries:
            for n in e.get_symbol_names(symbol):
                if n not in names:
                    names.append(n)
        return names



if __name__ == "__main__":
    pass