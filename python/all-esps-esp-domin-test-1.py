from fixtures.delay import *
from fixtures.readmail import *
from All_Esps_Esp_Domin_Test_1.create_contact import *
from All_Esps_Esp_Domin_Test_1.rc_send_campaign import *

createContactData = create_contact()
if createContactData.status_code == 200:
    delay(29)
    delay(29)
createCampaignData = rc_send_campaign()     
createCampaign = createCampaignData.json()
os.environ["campaign_id_esp_domin_test"] = str(createCampaign["payload"]["id"])
if createCampaignData.status_code == 200:
    ##ReadMail1
    usernameReadMail = "ae_isp_domin@hoohem.com"
    subjectReadMail = (
        "AB-Split Multiple ESP Test-"
        + os.environ["connectionId"]
        + "-"
        + os.environ["campaign_id_esp_domin_test"]
    )
    timeoutReadMail = 1200000

    readMailData = read_mail(usernameReadMail, subjectReadMail, timeoutReadMail)
    readMail = readMailData.json()
    if readMail["subject"] == subjectReadMail:
        print("Test All Esps Esp Domin :Passed")
    else:
        print("Test All Esps Esp Domin :Failed")
    # print("Read Mail 1 : ", json.dumps(readMail, indent=4))

    ##ReadMail2
    usernameReadMail = "ongageqa.t443@gmail.com"
    subjectReadMail = (
        "AB-Split Multiple ESP Test-"
        + os.environ["connectionId1"]
        + "-"
        + os.environ["campaign_id_esp_domin_test"]
    )
    timeoutReadMail = 1200000

    readMailData = read_mail(usernameReadMail, subjectReadMail, timeoutReadMail)
    readMail = readMailData.json()
    if readMail["subject"] == subjectReadMail:
        print("Test All Esps Esp Domin :Passed")
    else:
        print("Test All Esps Esp Domin :Failed")
    # print("Read Mail 2 : ", json.dumps(readMail, indent=4))
    del os.environ["campaign_id_esp_domin_test"]
