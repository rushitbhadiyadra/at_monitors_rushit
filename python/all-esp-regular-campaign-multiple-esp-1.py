from fixtures.delay import *
from fixtures.readmail import *
from All_ESP_Regular_Campaign_Multiple_esp_1.create_contact import *
from All_ESP_Regular_Campaign_Multiple_esp_1.rc_send_campaign import *

createContactData = create_contact()
if createContactData.status_code == 200:
    delay(29)
    delay(29)
createCampaignData = rc_send_campaign()     
createCampaign = createCampaignData.json()
delay(29)
delay(29)
delay(29)
os.environ["campaign_id_multiple_esp"] = str(createCampaign["payload"]["id"])
if createCampaignData.status_code == 200:
    ##ReadMail1
    count = 0
    usernameReadMail = "ae_rc_multi_esp_1@hoohem.com"
    subjectReadMail = (
        "All Esp RC Multiple ESP-"
        + os.environ["connectionId"]
        + "-"
        + os.environ["campaign_id_multiple_esp"]
    )
    timeoutReadMail = 6000

    readMailData = read_mail(usernameReadMail, subjectReadMail, timeoutReadMail)
    readMail = readMailData.json()
    if readMailData.status_code == 200:
        count += 1
    # print("Read Mail 1 : ", json.dumps(readMail, indent=4))

    ##ReadMail2
    usernameReadMail = "ae_rc_multi_esp_2@hoohem.com"
    subjectReadMail = (
        "All Esp RC Multiple ESP-"
        + os.environ["connectionId"]
        + "-"
        + os.environ["campaign_id_multiple_esp"]
    )
    timeoutReadMail = 6000

    readMailData = read_mail(usernameReadMail, subjectReadMail, timeoutReadMail)
    readMail = readMailData.json()
    if readMailData.status_code == 200:
        count += 1
    # print("Read Mail 2 : ", json.dumps(readMail, indent=4))

    ##ReadMail3
    usernameReadMail = "ae_rc_multi_esp_1@hoohem.com"
    subjectReadMail = (
        "All Esp RC Multiple ESP-"
        + os.environ["connectionId1"]
        + "-"
        + os.environ["campaign_id_multiple_esp"]
    )
    timeoutReadMail = 6000

    readMailData = read_mail(usernameReadMail, subjectReadMail, timeoutReadMail)
    readMail = readMailData.json()
    if readMailData.status_code == 200:
        count += 1
    # print("Read Mail 3 : ", json.dumps(readMail, indent=4))

    ##ReadMail4
    usernameReadMail = "ae_rc_multi_esp_2@hoohem.com"
    subjectReadMail = (
        "All Esp RC Multiple ESP-"
        + os.environ["connectionId1"]
        + "-"
        + os.environ["campaign_id_multiple_esp"]
    )
    timeoutReadMail = 6000

    readMailData = read_mail(usernameReadMail, subjectReadMail, timeoutReadMail)
    readMail = readMailData.json()
    if readMailData.status_code == 200:
        count += 1
    if count == 2:
        print("Test All ESP multiple esp is working :Passed")
    else:
        print("Test All ESP multiple esp is working :Failed")
    # print("Read Mail 4 : ", json.dumps(readMail, indent=4))
    del os.environ["campaign_id_multiple_esp"]
