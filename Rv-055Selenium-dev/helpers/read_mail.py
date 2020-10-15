"""helper functions to parse emails"""
import re
import time
import email
import imaplib
import helpers.settings as settings


def parse_mail(mail_text):
    """function to parse email text"""
    mail_regex = re.compile(r'''
                         .*(new\spassword:).*\n(http.*)\n
                            ''', re.VERBOSE)
    return mail_regex.findall(mail_text)

def read_mail(wait=None):
    """function used to retreave new emails
    wait: int,
    return: str OR None,
    wait optional argument, how long u want to wait for a new email.
    return link from email body, or None if there is no new emails.
    """
    if not wait:
        wait = 10
    user = settings.EMAIL_HOST_USER
    password = settings.EMAIL_HOST_PASSWORD
    imap_url = "imap.gmail.com"
    t_end = time.time() + wait
    with imaplib.IMAP4_SSL(imap_url) as con:
        con.login(user, password)
        text_string = main_loop(con, t_end)
    return parse_mail(text_string)[0]

def main_loop(con, t_end):
    """here we wait for email to appear in inbox
    and return it as a str
    """
    while time.time() < t_end:
        con.noop()
        time.sleep(2)
        con.select("INBOX")
        response, my_emails = con.search(None, "(UNSEEN)")
        if response != "OK":
            print("response: {}".format(response))
            continue
        if not my_emails[0]:
            continue
        mails = my_emails[0].split()
        for mail in reversed(mails):
            response, dat = con.fetch(mail, "(RFC822)")
            if response != "OK":
                print("response: {}".format(response))
                continue
            raw = email.message_from_bytes(dat[0][1])
            if raw["From"] != settings.SERVER_EMAIL:
                continue
            if raw["Subject"] != "Password reset on YouYoda":
                continue
            return raw.as_string()
