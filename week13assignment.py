import requests

def get_user_info():
    keyword = input("Enter keyword to search advice(life,time and others) : ")
    if keyword.strip() == "":
        raise ValueError("Keyword ")
    try:
        max_amount = int(input("Maximum number of advices to show: "))
    except:
        raise ValueError("Enter a number")
    if max_amount <= 0:
        raise OverflowError("Amount should be greater than 0")
    return keyword, max_amount

def get_data(keyword):
    url = "https://api.adviceslip.com/advice/search/" + keyword
    try:
        response = requests.get(url)
        data = response.json()
        if "slips" not in data:
            return []
        return data["slips"]
    except:
        raise ConnectionError("might be API issue")

def process_of_data(advices_list, max_amount):
    processed = []
    for item in advices_list:
        text = item["advice"]
        word_count = len(text.split())
        if word_count > 5:
            processed.append({
                "text": text,
                "words": word_count})
    result = processed[:max_amount]
    return result

def save_info_to_file(advices_list, keyword):
    with open("advices.txt", "w") as file:
        file.write(f"        ADVICES ABOUT {keyword.upper()}\n")
        file.write("--------------------------------------------------" + "\n")
        count = 1
        for advice in advices_list:
            file.write(f"\n{count}. {advice['text']}\n")
            file.write(f"   (Words: {advice['words']})\n")
            count += 1
        file.write(f"\nTotal saved: {len(advices_list)}")

def main():
    try:
        keyword, max_amount = get_user_info()
        data = get_data(keyword)
    except Exception as error:
        return str(error)

    if len(data) == 0:
        return "No advice was found for this word pls choose other word"

    processed_data = process_of_data(data, max_amount)

    if len(processed_data) == 0:
        return "Advice found, but none passed the filter."

    save_info_to_file(processed_data, keyword)
    return "Done! File named 'advices.txt' created."

print(main())