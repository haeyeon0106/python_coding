import re
def split_files(files):
    head,num,tail = re.match(r'([a-zA-Z\-\. ]+)([0-9]{1,5})(.*)',files).groups()
    return head.lower(),int(num)

def solution(files):
    answer = []
    sorted_files = sorted(files,key=lambda files:split_files(files))
    return sorted_files