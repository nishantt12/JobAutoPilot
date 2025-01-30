import json

from openai import OpenAI

# 1. Get tailored resume, CV and QA
# 2. Create Automated PDF
# 3. Autofill form with Google extension
# 4. Automatically click apply
# 5. Crawl Linkedin, RemoteOk, WllFound and automatically apply

# Soft Skills
#
# Repetations
#
# Date Formatting: ATS and recruiters prefer specific date formatting for your work experience. Please use the following formats: “MM/YY or MM/YYYY or Month YYYY” (e.g. 03/19, 03/2019, Mar 2019 or March 2019).
#
# Remove passionate word


def gen(job_description, base_resume):
    client = OpenAI(
        api_key="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"
    )

    prompt = f"""
      You are a resume optimization assistant. Your task is to modify the following resume to align with the provided job description. Ensure the following updates are made:

1. **Job Title**: Update the title to reflect the position mentioned in the job description.
2. **Summary**: Modify the summary to highlight relevant skills, experiences, and qualifications that align with the job.
3. **Skills**: Update the skills section to match the specific skills mentioned in the job description and which are not present in base_resume
4. **Current Work Experience**: Modify the bullet points under work experience to emphasize relevant achievements, responsibilities, and projects related to the role.

add this detail in work experience also: Experience in managing Kafka, NATS, or other messaging queues, as well as in building event-driven architectures"

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

    with open('backend/base_resume.json', 'r') as file:
        base_resume = json.load(file)

    # Example job description
    job_description = """
Who we are is what we do.

Deel and our family of growing companies are made up of global teams dedicated to helping businesses hire anyone, anywhere, easily. 

The team comprises over three thousand self-driven individuals spanning over 100 countries, and our unified yet diverse culture keeps us continually learning and innovating the platform and products for customers.

Companies should be able to hire the best talent anywhere in the world, so we are building the best platform to make that a reality. Our market-leading technology, expertise, and global team are crucial to the platform’s success. We deliver the best products and features in our space, enabling millions of jobs worldwide and connecting the global workforce with the best companies and opportunities.

Why should you be part of our success story?

A 30-mile hiring radius should no longer dictate how companies hire because exceptional talent lives everywhere. Deel sees a world without hiring borders and endless talent that pairs perfect candidates with great companies.

We offer global teams all the tools they need to hire, onboard, manage, pay, and scale at full speed. We aim to foster a diverse global economy by building a generational platform that seamlessly connects companies with talent worldwide.

After our successful Series D in 2021, we raised another $50M in 2023, doubling our valuation to $12B. There’s never been a more exciting time to join Deel — the international payroll and compliance market leader.

Deel is actively hiring Back-End Engineering professionals across multiple levels, including Mid-level, Senior-level, and Tech Lead roles. The role level will be determined based on candidates' experience (ranging from 4 to 14 years), expertise in relevant skills, and performance during the interview process.

Get Ready To:

Collaborate in a Cross-Functional Team: Work closely with Frontend Engineers, Product Teams, Designers, and QA professionals to create seamless experiences.

Participate in Product Planning: From discovery to deployment, we value your input throughout all stages of the Software Development Lifecycle 

Develop and Enhance Features: Collaborate to develop robust new features, APIs, and continuously improve our industry-leading products. Help find and fix bugs at "Deel Speed."

Provide an Exceptional, Customer-Centric Experience: Ensure top-tier products and services through quality engineering and attentive, customer-focused development.

What you’ll bring to the Team:

Expertise in Backend Development: Strong proficiency in Node.js, TypeScript/JavaScript best practices, along with experience in at least one other server-side language.

Database Mastery: You're a SQL guru, particularly with PostgreSQL, handling query optimization, data migrations, and database modeling.

Solid Grasp of OOP and Design Patterns: Strong understanding of object-oriented programming principles and design patterns, with experience in building and extending classes

Scalability Focus: Experience in designing systems for scalability, ensuring they manage rapid growth and increasing demands efficiently.

High-Volume Performance: Proven expertise in optimizing systems for large transaction volumes, handling concurrency, idempotency, and performance under load.

API Development: Skilled in building APIs, including input validation, JWT tokens, and ensuring security & scalability through queue-based systems.

Experience: at least 4 years of experience as a Software Engineer.

You're the Engineer We're Looking for if You:

Excel in Application Development: You thrive in designing, coding, testing, and maintaining applications using the tech stack mentioned above.

Thrive in Remote Collaboration: Excel in a remote-first environment with proactive communication and strong asynchronous collaboration skills to ensure alignment and effective teamwork. You’ve successfully worked in distributed teams 

Blending Autonomy and Collaboration: You take ownership of projects while excelling in team environments, driving shared success.

Communicate Complex Ideas Easily: You can clearly explain technical concepts to both technical and non-technical stakeholders.

Solve Problems with Optimism: You’re passionate about solving customer problems with your coding superpowers, and approach challenges with Default Optimism whilst maintaining a balanced perspective

Business-Focused Development: You take a business-focused approach to software development, with a keen eye on delivering high-value outcomes for our clients.

Genuine Care: You embody our core value of Genuine Care, understanding how your work impacts our customers.

Extra brownie points if you:

Have SaaS experience: experience with SaaS products running 24/7 on major cloud vendors.

Familiar with Serverless Architecture: experience with serverless architecture on AWS.

Understand FinTech: knowledge of the Fintech Industry and its unique challenge
    """

    # Call the function
    optimized_resume = gen(job_description, base_resume)

    # Print the optimized resume
    print("Optimized Resume:")
    print(optimized_resume)


if __name__ == "__main__":
    main()
