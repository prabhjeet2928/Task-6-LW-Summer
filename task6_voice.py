import pyttsx3 as sp
engine = sp.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 145)


def introduction():
    intro = '''Task 6

Team Task

Task Description

Create a program that perform below mentioned task upon recognizing a particular face. 

1. \nWhen it recognize your face, then -
    Create EC2 instance in the AWS using CLI. 
    Create 5 GB EBS volume and attach it to the instance.
    
2. \nWhen it recognize second face, in my case I using lalita's face, then - 
    It send mail to your mail id by writing this is face of your_name.
3. \nWhen it recognize third face, in my case I using shivkumar's face, then -
    It send whatsapp message to your friend, it can be anything.'''
    print(intro)
    engine.say(intro)
    engine.runAndWait()

def users():
    use = "See the multi-users name"
    print(use)
    engine.say(use)
    engine.runAndWait()

def final_touch1():
    final = '''Now, we will call the function as per given above when I give 'prabhjeet' face, it call the aws_instance() function.

In this aws_instance() function When 'prabhjeet' face comes up 90% or above accuracy then, it launch the ec2 instance for amazon linux, create an extra volume and attach to that new instance as well by input the count, availability zone, key name and disk size.'''
    print(final)
    engine.say(final)
    engine.runAndWait()
def final_touch2():
    final = '''Again, we will call the function as per given above when I give 'lalita' face, it call the send_mail() function.

In send_mail() function when 'lalita' face comes up with 90% or above accuracy then, it send the email through SMTP Protocol by giving an some input of profile name, sender email, receiver email and sender password.'''
    print(final)
    engine.say(final)
    engine.runAndWait()

def final_touch3():
    final = '''Again, we will call the function as per given above when I give 'shivkumar' face, it call the whatsapp_message() function.
    
In this whatsapp_message() function when 'shivkumar'face comes up with 90% or above accuracy then, It use to send the default static message for face detection by inputting your contact name and it also opens the new tab for opening the whatsapp through its microsoft edge webdriver and able to send message by using selenium  module in python.'''
    print(final)
    engine.say(final)
    engine.runAndWait()

def thank_you():
    thank = "THANK YOU FOR WATCHING THIS VIDEO"
    print(thank)
    engine.say(thank)
    engine.runAndWait()
