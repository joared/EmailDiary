import datetime

class Entry:
    def __init__(self, raw_entry):
        self.date, self.text = self._parse(raw_entry)
        self.people = get_tags_from_entry(self.text, "@")
        self.tags = get_tags_from_entry(self.text, "#")
        
    def _parse(self, raw_entry):
        raw_entry = raw_entry.strip()
        #print("Date string: " + raw_entry[:raw_entry.find("\n")])
        date_string = raw_entry.split()[1]
        day, month, year = map(int, date_string.split("/"))
        year += 2000
        date = datetime.datetime(year, month, day)
        text = raw_entry[raw_entry.index(date_string) + len(date_string):].strip()
        return date, text

class Diary:
    def __init__(self):
        self.entries = []
        
    def add_entry(self, entry):
        if isinstance(entry, Entry):
            self.entries.append(entry)
        elif isinstance(entry, str):
            self.entries.append(Entry(entry))
            
    def get_tags(self, tag_symbol):
        names = []
        for e in self.entries:
            for n in get_tags_from_entry(e.text, tag_symbol):
                if n not in names:
                    names.append(n)
        return names

def get_tags_from_entry(entry, tag_symbol):
    names = []
    entry_temp = entry
    for _ in range(entry.count(tag_symbol)):
        idx = entry_temp.index(tag_symbol)
        entry_temp = entry_temp[idx+1:]
        
        name = entry_temp.split()[0].split(",")[0].split(".")[0]
        if len(entry_temp.split()[0]) < 2:
            name += entry_temp.split()[1].split(",")[0].split(".")[0]
        
        if not name in names: 
            names.append(name)
    return names

if __name__ == "__main__":
    pass