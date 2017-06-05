import urllib.request
import re
from bs4 import BeautifulSoup  # BS processes unicode much better
import pandas as pd
import datetime


def __convert_chinese_date(date_string):
    "Converts chinese date text to python datetime object"
    return datetime.datetime(year=int(date_string[:4]), month=int(date_string[5:7]), day=int(date_string[8:10]))


def __process_page(url):

    soup = BeautifulSoup(urllib.request.urlopen(url), "lxml")
    question_tags = soup.find_all(class_="ask")
    question_items = [None] * len(question_tags)  # Pre-allocate memory space so we don't have to call append so often
    idx = 0
    for tag in question_tags:
        question_items[idx] = tag["href"]
        idx += 1
    base_url = url[:url.rfind("/") + 1]

    qa_list = [None] * len(question_tags)  # Again, pre-allocate memory for the list
    idx = 0
    for itm in question_items:
        sub_question_url = base_url + itm
        sub_soup = BeautifulSoup(urllib.request.urlopen(sub_question_url), "lxml")
        date_tags = sub_soup.find_all(class_="date")
        question_date = __convert_chinese_date(date_tags[0].string)
        msg_contents = sub_soup.find_all(class_="msgCnt")
        question = list(msg_contents[0].div.strings)[-1].strip()
        #
        # Couple of things to note for the answer block:
        # 1) No sub <div>.
        # 2) <br> inserted as hard line-break - this is interpreted as separate string items. Apparently, the company's IR uses a
        # different system.
        #
        if len(msg_contents) > 1:
            answer_block_text_list = list(msg_contents[1].strings)
            if len(answer_block_text_list) >= 4:
                answer = "".join(answer_block_text_list[4:]).strip()
                if len(answer) > 0:
                    answer = answer[1:]  # Do some prettify of the result...
                    answer = answer.strip()
        else:
            answer = ""

        qa_list[idx] = (question_date, question, answer)
        idx += 1

    return qa_list


def __grab_from_sz(url_string, stock_code):
    market_code = "S"
    page_no = 1

    soup = BeautifulSoup(urllib.request.urlopen(url_string.format(stock_code, market_code, page_no)), "lxml")
    pages_td = soup.find_all(class_="PagesBox").pop().table.tbody.tr.next_sibling.td  # Locate the pages box
    pages_match = re.findall("\(\d+\)", str(pages_td))  # Find all the page number quotes

    # Find the maximum page number
    max_page_num = 0
    for page_num in map(lambda s: s.lstrip("(").rstrip(")"), pages_match):
        if int(page_num) >= max_page_num:
            max_page_num = int(page_num)

    qa_list = []
    for page_idx in range(1, max_page_num + 1):
        print("Processing page {} of {}...".format(page_idx, max_page_num))
        qa_list += __process_page(url_string.format(stock_code, market_code, page_idx))

    return pd.DataFrame(qa_list, columns=["Date", "Question", "Answer"])


def grab_from_sz_replied(stock_code):
    """
     Grab replied Q&A data from the Shenzhen stock exchange investor relations website (http://irm.cninfo.com.cn).
     This is mapped to the "最新答复" section of irm.cninfo.com.
     :param stock_code: the stock code in string
     :return: A pandas DataFrame object containing date, question and answer.
     """
    url_string = r"http://irm.cninfo.com.cn/ircs/interaction/lastRepliesforSzseSsgs.do?condition.type=1&condition.stockcode={}&condition.stocktype={}&pageNo={}"
    return __grab_from_sz(url_string, stock_code)


def grab_from_sz_all(stock_code):
    """
     Grab all Q&A data from the Shenzhen stock exchange investor relations website (http://irm.cninfo.com.cn).
     This is mapped to the "最新提问" section of irm.cninfo.com.
     :param stock_code: the stock code in string
     :return: A pandas DataFrame object containing date, question and answer.
     """
    url_string = r"http://irm.cninfo.com.cn/ircs/interaction/lastQuestionforSzseSsgs.do?condition.type=2&condition.stockcode={}&condition.stocktype={}&pageNo={}"
    return __grab_from_sz(url_string, stock_code)