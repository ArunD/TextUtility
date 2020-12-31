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
    

    if utility_type == "textstats/":
        opdir = "/textStatsData/"
        parserop = TextParser()
    elif utility_type == "removechar/":
        opdir = "/removeCharData/"
        remove_char = params['remove_char']
        parserop = RemoveCharParser()
    else:
        opdir = "/specialCharData/"
        parserop = SpecialCharParser()

    try:
        os.mkdir(FILE_DIR+'/user_'+id +opdir)
    except Exception as err:
        print('Mkdir Error : {0}'.format(err))

    print(parserop)
    if 'file_name' in params:
        document = params['file_name']
        uploaded_path = os.path.join(FILE_DIR,'user_'+id +'/rawData/' + document)

        #textStats_path = os.path.join(FILE_DIR,'user_'+id +'/textStatsData/' + document)
        textStats_path = os.path.join(FILE_DIR,'user_'+id +opdir + document)
        datatype = 'file'
        textDict = parserop.parse(datatype,uploaded_path,remove_char)
    else :
        text_upload = params['text_upload']
        fname = params['fname']
        datatype = 'notfile'
        textStats_path = os.path.join(FILE_DIR,'user_'+id +opdir + fname + '.txt')
        textDict = parserop.parse(datatype,text_upload,remove_char)
    
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
    else :
        print(textDict['specialChar'],file=wf)
        textDict['status'] = 200

    wf.close

    return JsonResponse(data=textDict)







    

