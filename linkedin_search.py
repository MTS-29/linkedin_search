from dotenv import load_dotenv
from typing import Tuple

from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI

from Output_parsers import summary_parser, Summary
from third_parties.linkedIn import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent


def ice_break_with(name: str) -> Tuple[Summary, str]:
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username)

    summary_template = """
    given the Linkedin information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    \n{format_instructions}
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        }
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = summary_prompt_template | llm | summary_parser
    information = scrape_linkedin_profile(
        linkedin_profile_url="https://gist.githubusercontent.com/mtaqui-prologis/f9f21e7bf4c09720939a18e8297a27c2/raw/f669eb8276fd67835ea0828f8786e661b13d99ff/llm_practice.json")
    res = chain.invoke(input={"information": linkedin_data})

    return res, linkedin_data.get("profile_pic_url")


if __name__ == "__main__":
    load_dotenv()

    print("Ice Breaker Enter")
    ice_break_with(name="Mohammad Taqui Siddiqui Nisum")
