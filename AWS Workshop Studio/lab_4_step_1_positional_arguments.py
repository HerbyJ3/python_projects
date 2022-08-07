import boto3


def translate_text(text, source_language_code, target_language_code):
    client = boto3.client('translate')
    response = client.translate_text(
        Text=text,  # we remove the hard coded value
        SourceLanguageCode=source_language_code, # we used the positional argument instead
        TargetLanguageCode=target_language_code
)
    print(response["TranslatedText"])            

def main():
    translate_text('I am learning to code in AWS ', 'en', 'ht')  # we provide the value for the arguments when we call the function in the correct positional order.
    translate_text('How to be a cloud engineer in Haiti ', 'en', 'ht')

if __name__=="__main__":
    main()