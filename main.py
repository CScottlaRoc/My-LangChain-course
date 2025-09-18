from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
load_dotenv()


def main():
    print("Hello from langchain-course!")
    information = """
RIO DE JANEIRO (AP) — When two police officers tore little Chico from the arms of Elizete Carmona, they said it was for his own good. After all, 71-year-old women aren’t meant to live with endangered tufted capuchin monkeys.

But the case has upset many in Brazil, and thousands of people have signed an online petition calling on Sao Paulo state environmental officials to return Chico to the only home he’s known for the past 37 years.

It’s illegal to keep wild animals as pets in Brazil, especially those classified as endangered on the International Union for the Conservation of Nature’s Red List of threatened species, as the tufted capuchin monkey has been.

But the Carmona family contends Chico is completely domesticated and might not survive the stress of separation.

When the officers came to their house in the city of San Carlos on Saturday, Chico grabbed onto Carmona and hugged her tight, one of the woman’s sons, Everaldo Furlan, told the Globo television network.


    """
    summary_template = """ 
    given the information {information} about a subject I want you to create:
    1. A short summary 
    2. two interesting facts about that topic
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model="gpt-5")
    # llm = ChatOllama(temperature=0, model="gemma3:270m")
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})
    print(response.content)
if __name__ == "__main__":


    main()
