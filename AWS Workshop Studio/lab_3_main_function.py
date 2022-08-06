import boto3
client = boto3.client('translate')

def translate_text():
    response = client.translate_text(
        Text='I am learning to code in AWS',
    SourceLanguageCode='en',# We are using a two letter language code from the documentation (en = English)
    TargetLanguageCode='ht' # We are using a two letter language code from the documentation (ht = Haitian Creole)
)
    print(response)# this code is inside the function and will print the contents of the variable 'response'
def main():
    translate_text()

if __name__=="__main__":
    main()