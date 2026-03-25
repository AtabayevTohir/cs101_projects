import requests

# -----------------------------
# get user input
# -----------------------------
def get_user_info():
    keyword = input("Enter keyword to search advice: ")

    if keyword.strip() == "":
        raise ValueError("Keyword cannot be empty")

    return keyword


# -----------------------------
# get data from api
# -----------------------------
def get_data(keyword):
    url = "https://api.adviceslip.com/advice/search/" + keyword

    try:
        response = requests.get(url, headers={"Cache-Control": "no-cache"})
        data = response.json()

        if "slips" not in data:
            return []

        return data["slips"]

    except:
        raise ConnectionError("Internet problem or API issue")


# -----------------------------
# process data
# -----------------------------
def process_data(advice_list):
    processed = []

    for item in advice_list:
        text = item["advice"]
        word_count = len(text.split())

        # filtering logic
        if word_count > 5:
            processed.append({
                "text": text,
                "words": word_count
            })

    return processed


# -----------------------------
# display results
# -----------------------------
def display_results(advice_list, keyword):
    output = f"\n{'ADVICES ABOUT ' + keyword.upper():^50}\n"

    count = 1
    for advice in advice_list:
        output += f"\n{count}. {advice['text']}"
        output += f"\n   (Words: {advice['words']})\n"
        count += 1

    return output


# -----------------------------
# main program
# -----------------------------
def main():
    try:
        keyword = get_user_info()
        raw_data = get_data(keyword)
    except Exception as error:
        return str(error)

    if len(raw_data) == 0:
        return "No advice found."

    processed = process_data(raw_data)

    if len(processed) == 0:
        return "Advice found, but none passed the filter."

    result = display_results(processed, keyword)
    print(result)
    return "Done ✅"


print(main())
