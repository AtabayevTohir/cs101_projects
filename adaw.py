import requests         
import json
# Takes information from the user: interactive part
def get_user_info():
    surah = int(input("Enter Surah Number: "))
    if not 0<surah<115:
        raise OverflowError(f"Invalid number: Surah must be between 1 and 114")
    url = f"https://api.alquran.cloud/v1/surah/{surah}/en.asad"
    response = requests.get(url)
    max_ayah_number = json.loads(response.text)["data"]["numberOfAyahs"]
    ayah = int(input("Enter Ayah Number: "))
    if not 0<ayah<max_ayah_number+1:
        raise OverflowError(f"Invalid number: Ayah must be between 1 and {max_ayah_number}")
    return surah, ayah
# Gets data from the given url
def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError(f"Invalid API key: {response.status_code}")
# Takes the raw data and returns the most important information
def process_data(data):
    surah_number = data['data']['surah']['number']
    text = data['data']['text']
    serial_number = data['data']['number'] # “You are number 12”
    data_surah = data['data']['surah']
    index_of_en_name = list(data_surah.keys())[2]
    name_of_surah = data_surah[index_of_en_name]
    ayah_number = data['data']['numberInSurah']
    return [surah_number, text, serial_number, name_of_surah, ayah_number]
def display_results(list_of_data):
    formatted_info = f'''{'INFORMATION'.center(50, '-')}
Surah number: {list_of_data[0]}
Ayah number:  {list_of_data[4]}
Surah name:   {list_of_data[3]}

{'AYAH'.center(50, '-')}
{list_of_data[1]}

{'ADDITIONAL INFO'.center(50, '-')}
Ayah's position in Qur'an: {list_of_data[2]}'''
    return formatted_info
def save_info(info):
    with open('info.txt', 'w') as f:
        f.write(info)
# Main function which takes suitable data from various functions and gives appropriate arguments to other functions
def main():
    try:
        surah, ayah = get_user_info()
    except OverflowError as error:
        return error
    except Exception as error:
        return f"You entered invalid number: {error}"
    url = f"https://api.alquran.cloud/v1/ayah/{surah}:{ayah}/en.asad"
    try:
        data = get_data(url)
    except Exception as error:
        return error
    try:
        processed_data = process_data(data)
    except Exception as error:
        return error
    try:
        formatted_text = display_results(processed_data)
    except Exception as error:
        return error
    try:
        save_info(formatted_text)
    except Exception as error:
        return error
    return "Done ✅\nYou can check the info.txt file"
print(main())