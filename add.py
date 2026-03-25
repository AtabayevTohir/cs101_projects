import requests

def get_user_info():
    keyword = input("Enter keyword to search advice: ").lower()

    if keyword.strip() == "":
        raise ValueError("Keyword cannot be empty")

    try:
        min_length = int(input("Minimum advice length: "))
    except:
        raise ValueError("Length must be a number")

    return keyword, min_length


def get_data(url):
    headers = {
        "Accept": "application/json"
    }

    try:
        response = requests.get(url, headers=headers, timeout=5)
    except requests.exceptions.RequestException:
        raise ConnectionError("Internet problem")

    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError(f"API error: {response.status_code}")


def process_data(data, min_length):
    if "message" in data:
        return []

    filtered = []

    for slip in data["slips"]:
        text = slip["advice"]
        if len(text) >= min_length:
            filtered.append({
                "id": slip["id"],
                "text": text,
                "length": len(text)
            })

    return filtered


def display_results(advice_list, keyword):
    output = f"{'ADVICES ABOUT ' + keyword.upper():^50}\n"

    count = 1
    for advice in advice_list:
        output += f"\n{count}. {advice['text']}"
        output += f"\n   (Length: {advice['length']})\n"
        count += 1

    return output


def save_info(info):
    with open("advices.txt", "w") as f:
        f.write(info)


def main():
    try:
        keyword, min_length = get_user_info()
        url = f"https://api.adviceslip.com/advice/search/{keyword}"

        raw_data = get_data(url)
        processed = process_data(raw_data, min_length)

        if len(processed) == 0:
            return f"No advice found about '{keyword}'."

        # data processing: sort by length
        processed.sort(key=lambda x: x["length"])

        result = display_results(processed, keyword)
        save_info(result)

        print(result)
        return "Done ✅ Check advices.txt"

    except Exception as error:
        return str(error)


print(main())
