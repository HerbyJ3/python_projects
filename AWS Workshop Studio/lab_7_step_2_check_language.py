import json

# A defined list of languages supported by Amazon Translate
languages = ["af","sq","am","ar","az","bn","bs","bg","zh","zh-TW","hr","cs","da","fa-AF","nl","en","et","fi","fr","fr-CA","ka","de","el","ha","he","hi","hu","id","it","ja","ko","lv","ms","no","fa","ps","pl","pt","ro","ru","sr","sk","sl","so","es","sw","sv","tl","ta","th","tr","uk","ur","vi"]

# This uses a json string as an input
json_string = """
{
    "Input":[
        {
        "Text":"I am learning to code in AWS",
        "SourceLanguageCode":"en",
        "TargetLanguageCode":"fr"
        }
    ]
}
"""

json_input = json.loads(json_string)

# Extracts the SourceLanguageCode and TargetLanguageCode from the JSON
SourceLanguageCode = json_input['Input'][0]['SourceLanguageCode']
TargetLanguageCode = json_input['Input'][0]['TargetLanguageCode']

# Uses an if-else statement to check that the SourceLanguageCode is in the languages list.
if SourceLanguageCode in languages:
    print("The SourceLanguageCode is valid - proceeding")
else:
    print("The SourceLanguageCode is not valid - stopping")
