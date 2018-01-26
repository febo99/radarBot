#-*- coding: utf-8 -*-
#! /usr/bin/env python3
import time
import email
import imaplib
import tweepy
from kode import *
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

while True:
    stevilka = ""
    kraj = ""
    streznik = "imap.gmail.com"
    mail = imaplib.IMAP4_SSL(streznik,993)
    mail.login("radarmalecnik@gmail.com",gesloMail)
    mail.select('INBOX')
    type, data = mail.search(None,'(UNSEEN)')
    preveriPosto = mail.search(None,'UNSEEN')
    preveriPosto = len(preveriPosto[1][0].split())

    if(preveriPosto == 0):
        pass
    else:
        vsi_id = data[0].split()
        zadnji = int(vsi_id[-1])
        typ, data = mail.fetch(str(zadnji),"(RFC822)")
        for odgovor in data:
            if isinstance(odgovor, tuple):
                sporocilo = email.message_from_bytes(odgovor[1])
                izpis = str(sporocilo['subject'])
                for k in range(0,izpis.find("-")):
                    if(izpis[k] == " "):
                        kraj += "+"
                    else:
                        kraj += izpis[k]

                
                api.update_status(izpis+" https://www.google.si/maps/place/"+kraj)
                
        time.sleep(5)