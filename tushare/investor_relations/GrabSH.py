import urllib.request
import pandas as pd
from bs4 import BeautifulSoup  # BS processes unicode much better

__max_page_number = 100


def __grab_from_sh(url_string, stock_code):

    global __max_page_number

    page_no = 1
    qa_item_count = 0
    qa_list = []

    while True:
        # Notes:
        # 1. There seems to be currently no way of knowing how many pages there are except for enumerating until error.
        # 2. There is only month and day but no year data available.
        #
        print("Processing page {0}...".format(str(page_no)))

        request = urllib.request.Request(url_string.format(stock_code[(3 if stock_code[2] == "0" else 2):], str(page_no)))

        #
        # Set up request header for AJAX/XMLHttp request
        #
        request.add_header('Content-Type', 'application/json; charset=utf-8')
        request.add_header('X-Requested-With', 'XMLHttpRequest')
        request.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0")

        response = urllib.request.urlopen(request)
        html_doc = response.read().decode()

        if html_doc.find("暂时没有") != -1:
            break
        if page_no > __max_page_number:  # Put some boundaries here in case rules change....
            print("Page number exceeds {}".format(__max_page_number))
            print("There is either something wrong, or you can set the __max_page_number to a lager value to proceed.")
            break

        soup = BeautifulSoup(html_doc, "lxml")

        feed_item_tags = soup.find_all(class_="m_feed_item")

        for tag in feed_item_tags:
            try:
                date = tag.div.find_all(class_="m_feed_from")[0].span.string
                question = list(tag.div.find_all(class_="m_feed_txt")[0].strings)[2].strip()
            except IndexError:
                try:
                    date = tag.find_all(class_="m_feed_from")[0].span.string
                    question = list(tag.find_all(class_="m_feed_txt")[0].strings)[2].strip()
                except Exception:
                    print("Error processing tag:")
                    print(tag)
            try:
                answer = tag.div.next_sibling.next_sibling.next_sibling.next_sibling.find_all(class_="m_feed_txt")[0].string.strip()
            except Exception:
                answer = ""

            qa_list.append((date, question, answer))
            qa_item_count += 1

        page_no += 1

    return pd.DataFrame(qa_list, columns=["Date", "Question", "Answer"])


def grab_from_sh_replied(stock_code):
    """
    Grab replied Q&A items from the Shanghai stock exchange investor relations website (http://sns.sseinfo.com).
    This is mapped to the "最新答复" section of sns.sseinfo.com.
    :param stock_code: the stock code in string
    :return: A pandas DataFrame object containing date, question and answer.
    *The sseinfo.com website doesn't have year information of the Q&A date.
    """
    url_string = r"http://sns.sseinfo.com/ajax/userfeeds.do?typeCode=company&type=11&pageSize=10&uid={}&page={}"
    return __grab_from_sh(url_string, stock_code)


def grab_from_sh_unreplied(stock_code):
    """
    Grab unreplied Q&A items from the Shanghai stock exchange investor relations website (http://sns.sseinfo.com).
    This is mapped to the "最新提问" section of sns.sseinfo.com.
    :param stock_code: the stock code in string
    :return: A pandas DataFrame object containing date, question and answer.
    *The sseinfo.com website doesn't have year information of the Q&A date.
    """
    url_string = r"http://sns.sseinfo.com/ajax/userfeeds.do?typeCode=company&type=10&pageSize=10&uid={}&page={}"
    return __grab_from_sh(url_string, stock_code)


def set_max_page_number(page_no):
    global __max_page_number
    __max_page_number = page_no
