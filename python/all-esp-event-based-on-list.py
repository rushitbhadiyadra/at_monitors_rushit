from datetime import datetime
from fixtures.delay import *
from fixtures.readmail import *
from fixtures.get_old_segment import *
from All_Esp_Event_Based_On_List.delete_old_segment import *
from All_Esp_Event_Based_On_List.create_contact import *
from All_Esp_Event_Based_On_List.delete_mail import *
from All_Esp_Event_Based_On_List.get_old_event import *
from All_Esp_Event_Based_On_List.delete_old_event import *
from All_Esp_Event_Based_On_List.create_segment_event_and_trigger_based_on_list import *
from All_Esp_Event_Based_On_List.create_event import *
from All_Esp_Event_Based_On_List.delete_contact import *
from All_Esp_Event_Based_On_List.event_inactive import *
from All_Esp_Event_Based_On_List.delete_segment import *
from All_Esp_Event_Based_On_List.get_event_inactive import *
from All_Esp_Event_Based_On_List.delete_event import *

# Create contact
createContactData = create_contact()
createContact = createContactData.json()
if createContactData.status_code == 200:
    print("Create contact : Passesd", json.dumps(createContact, indent=4) )
else:
    print("Create contact : Fail", json.dumps(createContact, indent=4) )


# Delete mail
deletemailData = delete_mail()
deleteMail = deletemailData.json()
if deletemailData.status_code == 200:
    print("Delete mail : Passed", json.dumps(deleteMail, indent=4) )
else:
    print("Delete mail : Fail", json.dumps(deleteMail, indent=4) )


# Get old event
getoldevent = get_old_event()
getOldEvent_json = getoldevent.json()
event_len = len(getOldEvent_json['payload'])
old_event_flag = 0
if event_len > 0:
        for old_event in getOldEvent_json['payload']:
            if old_event['name'] == "All ESP Event and trigger based list " +os.environ['connectionId']:
                os.environ['old_event_id_event_list'] = old_event['id']
                print("Get old event : Passed ")
                old_event_flag = 1
else:
    old_event_flag = 0


#  Delete old event
if old_event_flag == 1:
    deleteoldevent = delete_old_event(os.environ['old_event_id_event_list'])
    deleteoldevent_json = deleteoldevent.json()
    if deleteoldevent.status_code == 200:
        print("Delete old event : Passed ")
        del os.environ['old_event_id_event_list']
    else:
        print("Delete old event : Fail ", json.dumps(deleteoldevent_json, indent=4))


delay(20)


# get old segment
segment_flag = 0
getoldseg = get_old_segment()
getOldseg_json = getoldseg.json()
segment_len = len(getOldseg_json['payload'])
if segment_len > 0:
    for old_segment in getOldseg_json['payload']:
        if old_segment['name'] == "All ESP Event & trigger based list " +os.environ['connectionId']:
            os.environ['old_segment_id_event_list'] = old_segment['id']
            print("Get old Segment : Passed ")
            segment_flag = 1 

else:
    segment_flag = 0


# Delete old segment
if segment_flag == 1:
    deleteoldsegment = delete_old_segment(os.environ['old_segment_id_event_list'])
    deleteoldsegmentJSON = deleteoldsegment.json()
    if deleteoldsegment.status_code == 200:
        print("Delete old Segment : Passed ")
        del os.environ['old_segment_id_event_list']
    else:
        print("Delete old Segment : Fail ", json.dumps(deleteoldsegmentJSON, indent=4))


# Create segment event and trigger
create_segment =  create_segment_event_and_trigger()
createsegmentJSON = create_segment.json()
if create_segment.status_code == 200:
    os.environ['all_esps_event_and_trigger_based_list_segment_id'] = str(createsegmentJSON['payload']['id'])
    print("Create segment event : Passes", json.dumps(createsegmentJSON, indent=4) )
else:
    print("Create segment event : Fail", json.dumps(createsegmentJSON, indent=4) )


delay(29)
delay(29)
delay(29)
delay(29)


# create event
unixTimestemp = round(datetime.now().timestamp() + 600)
os.environ['event_list_hours'] = str(datetime.utcfromtimestamp(unixTimestemp).hour)
os.environ['event_list_minutes'] = str(datetime.utcfromtimestamp(unixTimestemp).hour)
createevent = create_event(os.environ['all_esps_event_and_trigger_based_list_segment_id'],os.environ['event_list_hours'], os.environ['event_list_minutes'])
createeventJSON = createevent.json()
if createevent.status_code == 200:
    print("Create event : Passes", json.dumps(createeventJSON, indent=4) )
    os.environ['event_id_event_bsed_on_list'] = str(createeventJSON['payload']['id'])
    del os.environ['event_list_hours']
    del os.environ['event_list_minutes']
else:
    print("Create event : Fail", json.dumps(createeventJSON, indent=4) )

    


# read mail
readmail_flag = 0
usernameReadMail = "ae_rc_event_base_on_list"+os.environ['connectionId']+"@hoohem.com"
subjectReadMail = "ALl Esp Mirror Page-"+os.environ['connectionId']
timeoutReadMail = 12
readmail = read_mail(usernameReadMail,subjectReadMail,timeoutReadMail)
read_mailJSON = readmail.json()
if readmail.status_code == 200:
    if readmail['subject'] == subjectReadMail:
        print('ReadMail 1 Passed: Mail recived')
        readmail_flag = 1 

if readmail_flag == 0:
    readmail = read_mail(usernameReadMail,subjectReadMail,timeoutReadMail)
    read_mailJSON = readmail.json()
    if readmail.status_code == 200:
        if readmail['subject'] == subjectReadMail:
            print('ReadMail 2 Passed: Mail recived')
        else:
            print('Fail : Mail not recived')
    else:
        print("Read mail : Fail ", json.dumps(read_mailJSON, indent=4) )
    
#Delete Contact
deleteContact = delete_contact()
deleteContactJSON = deleteContact.json()
if deleteContact.status_code == 200:
    print("Delete contact : Passed", json.dumps(deleteContactJSON, indent=4) )
else:
    print("Delete contact : Fail")

# Event inactive
eventinactive = event_inactive()
eventinactiveJSON = eventinactive.json()
if eventinactive.status_code == 200:
    print("Event inactive : Passed", json.dumps(eventinactiveJSON, indent=4) )
else:
    print("Event inactive : Fail", json.dumps(eventinactiveJSON, indent=4) )
    

# Delete segment
deletesegment = delete_segment()
deletesegmentJSON = deletesegment.json()
if deletesegment.status_code == 200:
    print("Delete segment : Passed", json.dumps(deletesegmentJSON, indent=4) )
    del os.environ['all_esps_event_and_trigger_based_list_segment_id']
else:
    print("Delete segment : Fail", json.dumps(deletesegmentJSON, indent=4) )



# get inactive event
geteventinactive = get_event_inactive(os.environ['event_id_event_bsed_on_list'])
geteventinactiveJSON = geteventinactive.json()
if geteventinactiveJSON['payload']['segments'] == '':
        print('Test All Esp Event Based On List')
        print("Get event inactive : ", json.dumps(geteventinactiveJSON, indent=4) )


# delete event
deleteevent = delete_event(os.environ['event_id_event_bsed_on_list'])
deleteeventJSON = deleteevent.json()
if deleteevent.status_code == 200:
    print("Delete event : Passed", json.dumps(deleteeventJSON, indent=4) )
    del os.environ['event_id_event_bsed_on_list']
else:
    print("Delete event : Fail", json.dumps(deleteeventJSON, indent=4) )
