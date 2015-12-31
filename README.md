# SMS Automation in Python

This was one of my most difficult projects to accomplish as the there seem to be a lack of documentation readily available for newbs about this.

Upon checking Reddit, I stumbled upon the term “SMS Gateway”.What it does is it allows computers to send or receive Short Message Services (SMS) to or from a telecommunications network. Globe used to offer this for free while using Gmail back in 2011 but suddenly removed the service with no notification whatsoever. Smart, however, has one with the address #@mysmart.mymobile.ph. I have never personally checked if this is still working as two of my cellphones are subscribed to Globe.

*To my non-filipino readers, there is currently only two major mobile network provider in the Philippines, namely, Globe, and Smart Telecom.*

Spending more hours on research, I stumbled upon a Filipino third party SMS Gateway named Semaphore. All you have to do basically is send an HTTP request with all the required parameters (including number to send, and message) and they automatically sends your message to the specified recipient. I can only assume that they have a modem or server with a sim card that is connected to Globe and sends your messages from there.

What is good about knowing their services is that I learned how HTTP requests modules work. Apparently you can do URL requests with urllib in conjuction with urrlib2 modules or for the more streamlined URL request module, you could use Requests.

I quickly found out however that the services of Semaphore is still a bit faulty. It could not recognize me as someone that can pay even though I have already provided it with my credentials and other needed details.

While browsing for days, I noticed that my GSM modem from Globe is receiving SMS spam. It quickly dawned on me that if this device can receive, then it could also send messages.

Further research on GSM modem revealed that I could utilize its SMS capabilities once I know from what port it is connecting and also learn the Hayes Commands which is basically the language for communicating to modems.

The script is simple but I had to learn a thing or two from the Hayes Commands. These are basically the standard commands that the user sends to a modem to work. “AT+CMGF=1″ to turn the format to basic text, “AT+CMGS=” for the message body, and “AT+CMGL=” to read text messages. You also have to allow the modem to pause for a second for every command is it is not that fast on processing what it actually needed for it to do. Other info can be found on the comments inside the script.

###Required Readings
* To know the port path and commands needed to communicate to the server, read [this blog.](https://myraspberryandme.wordpress.com/2013/09/13/short-message-texting-sms-with-huawei-e220/)
* Baud rate is usually 115200 but you can read get a find a more specific config for your port by read [this.](http://linux.die.net/man/8/setserial)
