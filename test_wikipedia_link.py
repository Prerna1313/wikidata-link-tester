import requests

def get_wikipedia_link_from_qid(qid, language='en'):
    url = f"https://www.wikidata.org/wiki/Special:EntityData/{qid}.json"
    response = requests.get(url)
    if response.status_code != 200:
        return f"Failed to fetch data for QID {qid}"

    data = response.json()
    try:
        sitelinks = data['entities'][qid]['sitelinks']
        if f"{language}wiki" in sitelinks:
            return sitelinks[f"{language}wiki"]['url']
        else:
            return f"No {language} Wikipedia link found for QID {qid}"
    except KeyError:
        return f"Invalid response for QID {qid}"

# Example test
qids_to_test = ["Q42", "Q937", "Q7259"]  # Douglas Adams, Albert Einstein, Harry Potter

for qid in qids_to_test:
    print(f"{qid}: {get_wikipedia_link_from_qid(qid)}")

