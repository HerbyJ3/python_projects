import boto3

def translate_text(**kwargs): 
    client = boto3.client('translate')
    response = client.translate_text(**kwargs)
    print(response) 

### Change below this line only ###
text = input("Provide the text you want translating: ")
source_language_code = input("Provide the two letter source language code: ")
target_language_code = input("Provide the two letter target language code: ")

#kwargs={
#    "Text":"I am learning to code in AWS",
#    "SourceLanguageCode":"en",
#    "TargetLanguageCode":"ht"
#    }

def main():
    translate_text(
        Text = text,
        SourceLanguageCode = source_language_code,
        TargetLanguageCode = target_language_code
    )  

if __name__=="__main__":
    main()
