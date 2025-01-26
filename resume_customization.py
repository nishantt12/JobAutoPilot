import openai

def customize_resume(job_description, base_resume):
    openai.api_key = "your-openai-api-key"
    prompt = f"""
    You are a resume optimization assistant. Modify the following resume to fit this job description:

    Job Description: {job_description}

    Resume: {base_resume}
    """
    response = openai.Completion.create(
        model="gpt-4",
        prompt=prompt,
        max_tokens=500
    )
    return response['choices'][0]['text']

# Example
job_description = job_details['description']
base_resume = "Your generic resume content here..."
customized_resume = customize_resume(job_description, base_resume)
print(customized_resume)

import requests
from bs4 import BeautifulSoup


def fetch_job_details(job_url):
    response = requests.get(job_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.find('h1').text if soup.find('h1') else "N/A"
    description = soup.find('div', {'class': 'job-description'}).text if soup.find('div', {
        'class': 'job-description'}) else "N/A"
    return {'title': title, 'description': description}


# Example
job_url = "https://remoteok.com/remote-jobs/remote-software-development-engineer-ii-tala-911561"
job_details = fetch_job_details(job_url)
print(job_details)
