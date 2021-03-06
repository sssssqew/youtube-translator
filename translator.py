# pip 업그레이드하기 =>  /usr/bin/python3 -m pip install --upgrade pip
#  구글 번역 API 다운로드 하기 => pip3 install google_trans_new
# 구글 번역 라이브러리는 Python >=3.6 에서 동작함

import os
from google_trans_new import google_translator

directory_to_save_captions = '/home/sylee/dev/utility/youtube-translator/captions' # 자막을 저장할 폴더 위치 => PC마다 변경해줘야 함

# 자막 파일들을 담을 폴더 생성하기
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
 
createFolder(directory_to_save_captions)


filename = 'captions.srt' # 유튜브 영상에서 다운받은 자막파일 이름
src_lang = 'ko'
tgt_lang_array = ['en', 'zh-cn', 'zh-tw', 'hi', 'ru',
                             'ja', 'de', 'th', 'id', 'ms', 'vi', 'tl',
                             'fi', 'fr', 'pl',  'pt', 'es', 'tr', 'it',
                             'uk', 'da', 'no', 'nl', 'sv', 'he'
                             ]

translator = google_translator()  


def translate_and_save_into_file(filename, tgt_lang):
  #  파일 전체 읽어서 lines 배열에 저장하기
  f = open(filename, "r")
  lines = f.readlines()

  # 라인마다 순회하면서 한글이 있는 줄만 번역한 다음 lines 배열에 업데이트하기
  for i, line in enumerate(lines):
    if (i-2) % 4 == 0:
      # print(lines[i])
      translate_text = translator.translate(lines[i],lang_src=src_lang, lang_tgt=tgt_lang)  
      print(translate_text)
      lines[i] = translate_text + "\n" # 원래 다운로드한 자막파일에 자막마다 한줄 띄워쓰기가 있어서 반드시 "\n"  있어야 함

  # 변경된 lines 배열을 다시 파일에 쓰기
  f = open("{}/captions_{}.srt".format(directory_to_save_captions, tgt_lang), "w")
  f.writelines(lines)
  f.close()

# 번역할 언어 갯수만큼 순회하면서 번역하고 파일 저장함
for i in range(len(tgt_lang_array)):
  translate_and_save_into_file(filename, tgt_lang_array[i])
  print("---------------------------------------------------------------")


############### 변경할 언어 코드 ################
# 영어 : en
# 중국어(간체): zh-cn
# 중국어(번체) : zh-tw
# 힌두어 :  hi
# 러시아어: ru
# 일본어 : 	ja
# 독일어: de
# 태국어: th
# 인도네시아어 : id
# 말레이시아어: ms
# 베트남어 : vi
# 필리핀어 : tl
# 핀란드어 : fi
# 프랑스어: fr
# 폴란드어: pl
# 포르투칼어: pt
# 스페인어: es
# 터키어: tr
# 이탈리아어: it
# 우크라이나어: uk
# 덴마크어 : 	da
# 노르웨이어: no
# 네덜란드어: nl
# 스웨던어: sv
# 히브리어: he
############################################



  