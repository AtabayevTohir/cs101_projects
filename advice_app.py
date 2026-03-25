import requests

# -----------------------------
# get data from api
# -----------------------------
def get_advice(keyword):
    url = "https://api.adviceslip.com/advice/search/" + keyword

    try:
        response = requests.get(url, headers={"Cache-Control": "no-cache"})
        data = response.json()

        if "slips" not in data:
            return []

        return data["slips"]

    except:
        print("Error connecting to the API")
        return []


# -----------------------------
# process data
# -----------------------------
def process_advice(advice_list):
    filtered = []

    for item in advice_list:
        text = item["advice"]
        if len(text.split()) > 5:
            filtered.append(text)

    return filtered


# -----------------------------
# display result
# -----------------------------
def show_results(advice_list):
    print("\nResults:")
    print("----------------")

    for i in range(len(advice_list)):
        print(str(i + 1) + ".", advice_list[i])

    print("\nTotal advice shown:", len(advice_list))


# -----------------------------
# main program
# -----------------------------
def main():
    print("Advice Finder App")

    keyword = input("Enter a keyword to search advice: ")

    advice_data = get_advice(keyword)

    if len(advice_data) == 0:
        print("No advice found.")
        return

    processed = process_advice(advice_data)

    if len(processed) == 0:
        print("Advice found, but none passed the filter.")
        return

    show_results(processed)


main()
