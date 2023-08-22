# 에시는 통과했지만 테스트 코드에서 실패 + 런타임 에러
def solution(m, musicinfos):
    answer = ''
    titles = []
    sheets = []
    for music in musicinfos:
        start,end,title,sheet = music.split(',')
        play = int(end.split(':')[1]) - int(start.split(':')[1])
        titles.append(title)
        if len(sheet) >= play: 
            sheet = sheet[:play]
            sheets.append(sheet)
        else:
            sheetlt = len(sheet)-1
            sheet = sheet*(play//sheetlt) + sheet[:play%sheetlt]
            sheets.append(sheet)

    for i in range(len(titles)):
        if m in sheets[i]:
            a = sheets[i].index(m)
            if sheets[i][a+len(m)] == '#':
                continue
        return titles[i]
    

# 이것도 역시 테스트케이스 절반만 통과
def convert(sheet):
    sheet = sheet.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    return sheet

def solution2(m, musicinfos):
    answer = "(None)"
    sheets = []
    m = convert(m)
    max_play = 0
    
    for music in musicinfos:
        start,end,title,sheet = music.split(',')
        start_hour,start_min = map(int,start.split(":"))
        end_hour,end_min = map(int,end.split(":"))
        play = (end_hour-start_hour)*60 + (end_min-start_min)

        sheet = convert(sheet)
        sheetlt = len(sheet)
        sheet = sheet*(play//sheetlt) + sheet[:play%sheetlt]
        sheets.append(sheet)
        
        if m in sheet:
            if play > max_play or (play == max_play and music < answer):
                answer = title
                max_play = play 
    return answer


# 여기저기 참고해서 결국 해낸 코드
def convert3(sheet):
    sheet = sheet.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    return sheet

def solution3(m, musicinfos):
    answer = []

    m = convert(m)
    
    for music in musicinfos:
        start,end,title,sheet = music.split(',')
        start_hour,start_min = map(int,start.split(":"))
        end_hour,end_min = map(int,end.split(":"))
        play = (end_hour-start_hour)*60 + (end_min-start_min)

        sheet = convert(sheet)
        sheet = sheet*(play//len(sheet)) + sheet[:play%len(sheet)]
        
        if m in sheet:
            answer.append((play,title))
    
    if len(answer) > 0:
        answer = sorted(answer,key=lambda x:-x[0])
        return answer[0][1]
    return "(None)"
        