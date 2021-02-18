from quickstart import search_message, get_message, get_service, cleantext
from diary import Diary, Entry

def is_date_token(t):
    ls = t.split()
    if ls and ls[0] not in ("Monday,", "Tuesday,", "Wednesday,", "Thursday,", "Friday,", "Satruday,", "Sunday,"):
        return False

    
    try:
        ls = ls[1].split("/")
        if len(ls) != 3:
            return False
        for v in ls:
            int(v) # try to make it an int
    except:
        return False

    return True

def get_entries(cleaned_text):
    
    
    tokens = cleaned_text.split("\n")
    entries = []
    date_str = ""
    expect_date = True
    for t in tokens:
        if is_date_token(t):
            expect_date = False
            date_str = t.split()[1] #remove 'Monday,'
        elif expect_date:
            print("WARNING: Failed to read mail")
            #raise Exception("First token was not a date: '{}'".format(t))
        else:
            entries.append(Entry(date_str, t))
    return entries

def get_diary(service, user_id, msg_ids):
    d = Diary()
    for id in enumerate(msg_ids):
        # wtf happened to the ids? (somenumber, id)
        message = get_message(service, user_id, id[1])
        for e in get_entries(cleantext(message)):
            d.add_entry(e)
    
    return d

################## Input ###########################
        
def show_tags(diary):
    _show_symbol_names(diary, "#")
    
def show_people(diary):
    _show_symbol_names(diary, "@")
        
def _show_symbol_names(diary, symbol):
    for i, n in enumerate(diary.get_symbol_names(symbol)):
        print("{}. {}".format(i+1, n))

def show_entries(diary):
    for i, entry in enumerate(diary.entries):
        print("{}. {} - {}".format(i+1, entry.date.date(), entry.text[:50].replace("\n", " ")))
    print("{}. Exit".format(len(diary.entries) + 1))
    choice = int(input(": "))
    if choice < len(diary.entries) + 1:
        entry = d.entries[choice-1]
        print("Entry: {}\n\n{}".format(entry.date.date(), entry.text))
        input("\n(Press enter to continue)")

def show_entries_by_tag(diary):
    tag = input("Tag: ")
    for entry in diary.entries:
        if tag in entry.people() + entry.tags():
            print("{} - {}".format(entry.date.date(), entry.text[:50].replace("\n", " ")))

def choose_msg(service, user_id, msg_ids):
    messages = []
    
    for id in enumerate(msg_ids):
        # wtf happened to the ids? (somenumber, id)
        message = get_message(service, user_id, id[1])
        messages_ls = cleantext(message)
        messages.extend(messages_ls)
       
    for i, m in enumerate(messages):
        print("{}. {}".format(i+1, m[:50].strip().replace("\n", " ")))
        
    choice = int(input(": "))
    return messages[choice-1]

if __name__ == "__main__":
    """
    search operators: https://support.google.com/mail/answer/7190?hl=sv
    tutorial: https://www.youtube.com/watch?v=njDGaVnz9Z8
    quickstart: https://developers.google.com/gmail/api/quickstart/python
    """
    service = get_service()
    user_id = "me"

    #search_string = "subject:Document from my reMarkable:" # diary
    search_string = "subject:Mydiarea2" # test diary
    message_ids = search_message(service, user_id, search_string)
    #messages = choose_msg(service, user_id, message_ids)
    d = get_diary(service, user_id, message_ids)
    print("Read {} email and registered {} entries".format(len(message_ids), len(d.entries)))
    choices = [show_people, show_tags, show_entries, show_entries_by_tag]
    l = len(choices)
    while True:
        print("What you wanna do?")
        for i in range(l):
            print("{}. {}".format(i+1, choices[i].__name__))
        print("{}. Exit".format(l+1))
        choice = int(input(": "))
        if choice == l+1:
            break
        elif choice < l+1 and choice >0:
            choices[choice-1](d)
        else:
            print("Invalid choice")
        

    
