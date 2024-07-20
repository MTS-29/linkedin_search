# import requests
#
# api_key = 'm2ZEwwNcWhydb2QaAHGTtA'
# headers = {'Authorization': 'Bearer ' + api_key}
# api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
# params = {
#     'linkedin_profile_url': 'https://www.linkedin.com/in/mohammad-taqui-siddiqui-567147197/',
#     'extra': 'include',
#     'github_profile_id': 'include',
#     'facebook_profile_id': 'include',
#     'twitter_profile_id': 'include',
#     'personal_contact_number': 'include',
#     'personal_email': 'include',
#     'inferred_salary': 'include',
#     'skills': 'include',
#     'use_cache': 'if-present',
#     'fallback_to_cache': 'on-error',
# }
# response = requests.get(api_endpoint,
#                         params=params,
#                         headers=headers)
#
# print(response._content)
import requests

response = requests.get("https://gist.githubusercontent.com/mtaqui-prologis/f9f21e7bf4c09720939a18e8297a27c2/raw/f669eb8276fd67835ea0828f8786e661b13d99ff/llm_practice.json")
print(response.json()['full_name'])