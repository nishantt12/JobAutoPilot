import json

from openai import OpenAI


def gen(job_description, base_resume):
    client = OpenAI(
        api_key="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"
    )

    prompt = f"""
      You are a resume optimization assistant. Your task is to modify the following resume to align with the provided job description. Ensure the following updates are made:

1. **Job Title**: Update the title to reflect the position mentioned in the job description.
2. **Summary**: Modify the summary to highlight relevant skills, experiences, and qualifications that align with the job.
3. **Skills**: Update the skills section to match the specific skills mentioned in the job description.
4. **Current Work Experience**: Modify the bullet points under work experience to emphasize relevant achievements, responsibilities, and projects related to the role.

Ensure that the resume is optimized for ATS (Applicant Tracking System) and includes relevant keywords from the job description.

      Job Description: {job_description}

      Resume: {base_resume}
      """

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {"role": "system", "content": "You are a resume optimization assistant."},
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print(completion.choices[0].message.content)


def main():
    # Load the base resume from the JSON file
    with open('base_resume.json', 'r') as file:
        base_resume = json.load(file)

    # Example job description
    job_description = """
Wing Assistant is hiring a
Remote Software Engineer LLMs and Python
Wing is hiring elite talent for M32 Labs, an innovative venture-backed company based in Silicon Valley dedicated to building cutting-edge AI-powered products for business clients worldwide.

At M32, we're not just another tech company- we’re creating world-class AI solutions that redefine industries. If you’re looking for a challenging and high-impact engineering role, this is it.

What it'll be like working at M32: Move fast and break things: This is a company with 0 bureaucracy, and maximum impact. We are building world-class products, hiring a world-class team, and putting large resources behind the products you're building. We are looking for engineers who are willing to go above and beyond. Deadlines will be tight, expectations will be high. If you're looking for a standard 9-5 job, this is not the place for you. Autonomy & Creativity: We value decision-makers and innovators. You’ll have the control to make both technical and product decisions, and our goal is to let you lead entire product builds. Exponential Career Growth: Exceptional performance will be rewarded far beyond normal. If you excel at M32, expect your compensation to double within a year and your role to grow rapidly. Small, Elite Teams: You’ll work in tight-knit teams of 1–3 exceptional engineers to build full products from scratch. Every week will feel like a hackathon! High Impact: Your work will directly influence thousands of users, with immediate deployment and feedback. You’ll never work on insignificant internal tools or tiny features. You will work directly with C-level executives. Fast track to leadership. Are you ambitious AND hard working? We reward that here, promoting top performers to elevated positions quickly, at a faster rate than industry standards.

Requirements: Basics

Graduated from a university. Preference will be given to graduates of highly competitive institutions or candidates with comparable achievements. Exceptional talent from other backgrounds will also be considered.
A high degree of self-motivation, ambition, and the ability to thrive in fast-paced, high-expectation environments.
Comfortable with ambiguity and rapidly changing priorities, and able to deliver results under tight deadlines.
Strong foundation in computer science fundamentals, including algorithms, data structures, databases, and software design.
Demonstrated ability to solve complex technical problems, whether through academic or personal projects, past startups, hackathons, competitive programming, or professional experience.
Proven Development Experience:

Comfortable working with Ubuntu CLI, server setups, and AWS.
Experience building backend systems with Python server frameworks like FastAPI, Streamlit, or Flask.
Comfortabe deploying code to web environments and API endpoints
Comfortable working with websockets, including building real-time applications
Comfortable working in environments where Python may be used in conjunction with PHP and/or JavaScript backends
Expertise in AI Development:

Mastery of Python and AI libraries like LangChain, Phidata, CrewAI, etc.
Experience applying LLMs to solve problems (e.g., GPT models, Anthropic models, open-source alternatives).
Ability to evaluate and optimize open-source models, understanding their benefits and drawbacks.
Experience working with vector databases
Integration & API Experience:

Extensive experience working with APIs and external integrations.
Experience with Composio is a strong plus.
Preferred Skills:

Familiarity with Cursor AI or similar tools for rapid development.
Experience working in a remote-first setting.
Excellent verbal and written communication in English.
Strong degree of critical thinking & creativity.
Proficiency with Node JS is a plus.
Prior experience building full-scale web applications.
Experience in the LAMP stack (Linux, Apache, MySQL, PHP).
Strong proficiency and comfortable working with vanilla PHP and MySQL.
Responsibilities:

Architect, build, and deploy AI applications, leveraging integrations, tools, vector databases, and agents.
Work independently to lead the development of entire products, from prototype to deployment.
Evaluate and integrate the latest AI models to deliver cutting-edge solutions.
Collaborate with cross-functional teams (product, design) to rapidly iterate on ideas.
Take ownership of deployments, ensuring products are delivered on time and meet high standards.
Review user feedback, product data, problems shared by management and be able to think critically about solutions.
Come up with ideas with product team & management.
Working Location: This will be a remote role.
    """

    # Call the function
    optimized_resume = gen(job_description, base_resume)

    # Print the optimized resume
    print("Optimized Resume:")
    print(optimized_resume)


if __name__ == "__main__":
    main()
