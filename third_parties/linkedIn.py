import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url : str, mock : bool = True):
    """TODO"""
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/mtaqui-prologis/f9f21e7bf4c09720939a18e8297a27c2/raw/f669eb8276fd67835ea0828f8786e661b13d99ff/llm_practice.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )
    else:
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        response = requests.get(
            api_endpoint,
            params={"url": linkedin_profile_url},
            headers=header_dic,
            timeout=10,
        )

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data


if __name__ == "__main__":
    print(scrape_linkedin_profile(linkedin_profile_url="https://gist.githubusercontent.com/mtaqui-prologis/f9f21e7bf4c09720939a18e8297a27c2/raw/f669eb8276fd67835ea0828f8786e661b13d99ff/llm_practice.json"))