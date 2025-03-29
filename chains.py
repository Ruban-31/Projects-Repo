from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv
import os
load_dotenv()


if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))

class Chain():
    def __init__(self):
        self.llm = ChatGroq(temperature=0 , api_key=os.getenv("GROQ_API_KEY") , model_name="llama-3.3-70b-versatile")  



    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
    You are Ruban Sivan Perumal, a Business Intelligence Intern at Future Generali India Life Insurance. 
    You have experience working in the Analytics and Automation department to automate and develop dashboards using Power BI, and maintain databases in Google Cloud Platform Big Query.
    Your job is to write a cold email to the hiring team or person incharge of hiring regarding the job mentioned above, describing how you can fit in this job role.
    Focus on being **brief and to the point** while explaining your relevant experience.
    Keep the email **short** (around 150-200 words).
    Do not provide a preamble.
    
    ### EMAIL (NO PREAMBLE):
    """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description": str(job), "link_list": links})
        return res.content

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))