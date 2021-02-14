from quickstart import search_message, get_message, get_service, cleantext
from diary import Diary

def get_diary(service, user_id, msg_ids):
    d = Diary()
    for id in enumerate(msg_ids):
        # wtf happened to the ids? (somenumber, id)
        message = get_message(service, user_id, id[1])
        for m in cleantext(message):
            d.add_entry(m)
    
    return d

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

def show_entries(diary):
    for entry in d.entries:
        print("{} - {}".format(entry.date.date(), entry.text[:50].replace("\n", " ")))
        
def show_tags(diary):
    _show_tags(diary, "#")
    
def show_people(diary):
    _show_tags(diary, "@")
        
def _show_tags(diary, tag_symbol):
    for i, n in enumerate(diary.get_tags(tag_symbol)):
        print("{}. {}".format(i+1, n))

def show_entries_by_tag(diary):
    tag = input("Tag: ")
    for entry in diary.entries:
        if tag in entry.people + entry.tags:
            print("{} - {}".format(entry.date.date(), entry.text[:50].replace("\n", " ")))

if __name__ == "__main__":
    """
    search operators: https://support.google.com/mail/answer/7190?hl=sv
    tutorial: https://www.youtube.com/watch?v=njDGaVnz9Z8
    """
    service = get_service()
    user_id = "me"

    #search_string = input("Search string: ")
    search_string = "subject:Mydiary"
    message_ids = search_message(service, user_id, search_string)
    #messages = choose_msg(service, user_id, message_ids)
    d = get_diary(service, user_id, message_ids)
    
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
        

    
