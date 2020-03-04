import base64
import logging
import requests
import traceback
from cryptography.fernet import Fernet
from django.conf import settings
from django.template.loader import get_template
from django.utils.html import strip_tags
from martor.utils import markdownify
logger = logging.getLogger("error_logger")

SEPARATOR = "||"


def encrypt(txt: str):
    try:
        # convert integer etc to string first
        txt = str(txt)
        # get the key from settings
        cipher_suite = Fernet(settings.ENCRYPT_KEY) # key should be byte
        # #input should be byte, so convert the text to byte
        encrypted_text = cipher_suite.encrypt(txt.encode('ascii'))
        # encode to urlsafe base64 format
        encrypted_text = base64.urlsafe_b64encode(encrypted_text).decode("ascii") 
        return encrypted_text
    except Exception as e:
        # log the error if any
        logger.error(traceback.format_exc())
        return None

def decrypt(txt: str):
    try:
        # base64 decode
        txt = base64.urlsafe_b64decode(txt)
        cipher_suite = Fernet(settings.ENCRYPT_KEY)
        decoded_text = cipher_suite.decrypt(txt).decode("ascii")     
        return decoded_text
    except Exception as e:
        # log the error
        logger.error(traceback.format_exc())
        return None


def send_email(data):
    try:
        url = "https://api.mailgun.net/v3/mail.qiwihui.com/messages"
        status = requests.post(
            url,
            auth=("api", settings.MAILGUN_API_KEY),
            data={"from": "codeaday <admin@mail.qiwihui.com>",
                  "to": [data["email"]],
                  "subject": data["subject"],
                  "text": data["plain_text"],
                  "html": data["html_text"]}
        )
        logger.info("Mail sent to " + data["email"] + ". status: " + str(status))
        return status.status_code == 200
    except Exception as e:
        logger.error(traceback.format_exc())
        return False


def send_subscription_email(email, subscription_confirmation_url):
    data = dict()
    data["confirmation_url"] = subscription_confirmation_url
    data["subject"] = "每日一题 - 请确认订阅"
    data["email"] = email
    template = get_template("subscription.html")
    data["html_text"] = template.render(data)
    data["plain_text"] = strip_tags(data["html_text"])
    return send_email(data)


def send_problem_email(email, problem, previous_solutions=None, unsubscribe_url=None):
    data = dict()
    problem_order = problem["order"]
    data["subject"] = f"每日一题 [#{problem_order}] " + problem["title"]
    data["email"] = email
    data["problem_content"] = markdownify(problem["content"])
    data["unsubscribe_url"] = unsubscribe_url or ""
    if previous_solutions is not None:
        data["previous_solutions"] = previous_solutions
    template = get_template("problem.html")
    data["html_text"] = template.render(data)
    data["plain_text"] = strip_tags(data["html_text"])
    return send_email(data)


if __name__ == "__main__":
    pass