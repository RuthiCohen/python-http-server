from datetime import datetime

def lower_word(word):
    return word.lower()

def str_2_date(date):
    return datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')

def date_2_str(date):
    return date.strftime('%Y-%m-%dT%H:%M:%S')