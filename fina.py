import requests

# -----------------------------
# get user input
# -----------------------------
def get_user_info():
    keyword = input("Enter keyword to search advice: ")

    if keyword.strip() == "":
        raise ValueError("Keyword cannot be empty")

    try:
        max_amount = int(input("Maximum number of advices to save: "))
    except:
        raise ValueError("Amount must be a number")

    if max_amount <= 0:
        raise OverflowError("Amount must be greater than 0")

    return keyword, max_amount


# -----------------------------
# get data from api
# -----------------------------
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


# -----------------------------
# process data
# -----------------------------
def process_data(advice_list, max_amount):
    processed = []

    for item in advice_list:
        text = item["advice"]
        word_count = len(text.split())

        if word_count > 5:
            processed.append({
                "text": text,
                "words": word_count
            })

    # limit to max amount (if not enough, takes all)
    return processed[:max_amount]


# -----------------------------
# save to file
# -----------------------------
def save_info(advice_list, keyword):
    with open("advices.txt", "w") as file:
        file.write(f"ADVICES ABOUT {keyword.upper()}\n")
        file.write("-" * 50 + "\n")

        count = 1
        for advice in advice_list:
            file.write(f"\n{count}. {advice['text']}\n")
            file.write(f"   (Words: {advice['words']})\n")
            count += 1

        file.write(f"\nTotal saved: {len(advice_list)}\n")


# -----------------------------
# main program
# -----------------------------
def main():
    try:
        keyword, max_amount = get_user_info()
        raw_data = get_data(keyword)
    except Exception as error:
        return str(error)

    if len(raw_data) == 0:
        return "No advice found. File not created."

    processed = process_data(raw_data, max_amount)

    if len(processed) == 0:
        return "Advice found, but none passed the filter."

    save_info(processed, keyword)
    return "Done ✅ File 'advices.txt' created."


print(main())
