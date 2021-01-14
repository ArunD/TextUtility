from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
import random
from TextUtility.settings import FILE_DIR
from app_utility.parser.wordCount import TextParser
from app_utility.parser.specialChar import SpecialCharParser
from app_utility.parser.removeChar import RemoveCharParser
from app_utility.parser.lexerHtml import LexerOp


# Create your views here.
@csrf_exempt
def perform_utility(request,utility_type):
    #print(request)
    textDict = {}
    remove_char = []
    params = json.loads(request.body)
    #print(params)
    id = params['id']
    id = str(id)
    
    #extn = params['extn']
    extn = '.txt'
    fname = params['fname']
    if utility_type == "textstats/":
        opdir = "/textStatsData/"
        parserop = TextParser()
    elif utility_type == "removechar/":
        opdir = "/removeCharData/"
        remove_char = params['remove_char']
        parserop = RemoveCharParser(remove_char)
    elif utility_type == "specialchar/":
        opdir = "/specialCharData/"
        parserop = SpecialCharParser()
    elif utility_type == "lexer/":
        opdir = "/lexerOpData/"
        language = params['language']
        parserop = LexerOp(language)
        extn = '.html'

    try:
        os.mkdir(FILE_DIR+'/user_'+id +opdir)
    except Exception as err:
        print('Mkdir Error : {0}'.format(err))

    #print(parserop)
    if 'file_name' in params:
        document = params['file_name']
        uploaded_path = os.path.join(FILE_DIR,'user_'+id +'/rawData/' + document)
        datatype = 'file'
        textDict = parserop.parse(datatype,uploaded_path)
    else :
        text_upload = params['text_upload']
        fname = params['fname']
        datatype = 'notfile'
        textDict = parserop.parse(datatype,text_upload)
    
    
    textStats_path = os.path.join(FILE_DIR,'user_'+id +opdir + fname + extn)
    #print(uploaded_path)
    
    wf = open(textStats_path,'w')

    if utility_type == "textstats/":
        for k,v in textDict.items():
            if k == 'nl':
                print('Total no of lines(including Blank) : '+str(v),file=wf)
            if k == 'l':
                print('Total no of lines : '+str(v),file=wf)
            if k == 'wc':
                print('Total no of words : '+str(v),file=wf)
            if k == 'tu':
                print('************************************************************',file=wf)
                print('Word : Count',file=wf)
                for val in v:
                    print(val[0] +' : ' + str(val[1]),file=wf)
    elif utility_type == "removechar/":
        print(textDict['removeChar'],file=wf)
    elif utility_type == "specialchar/":
        print(textDict['specialChar'],file=wf)
    elif utility_type == "lexer/":
        print(textDict['lexerOp'],file=wf)
        
    textDict['status'] = 200
    wf.close

    return JsonResponse(data=textDict)







    

