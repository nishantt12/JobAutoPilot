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

    with open('android/base_resume.json', 'r') as file:
        base_resume = json.load(file)

    # Example job description
    job_description = """
Company Description:
Trust Payments is an MFSA-regulated in Malta; and an FCA-regulated company in the UK. We provide a range of payments and commerce solutions, with market-leading technology and data insights.

We offer innovative payment methods and cutting-edge technologies, with a truly global presence. Our global offices cater to the most demanding business sectors, including retail, travel, hospitality, forex, and financial services.


Driving value for our clients and demonstrating genuine care for their success, is a core value of ours. We also believe in striving to build a better, more sustainable tomorrow and believe in conducting our business ethically, driving social and environmental change.

We have a passionate, collaborative, and diverse culture that recognizes that every employee contributes to our business success.

Find out more at www.trustpayments.com.  

Trust Payments has an exciting opportunity for a Senior Android Developer (Tech Lead) to join their team.

Location: Remote - India - Bangalore

Salary: Competitive + Benefits

Job Type: Full-Time/ Permanent

How will you make an impact in this role?
The Role:

Notable leadership experience and can mentor and teach your team in a positive, proactive, Agile manner.
Architect, design, and develop scalable and maintainable Android applications that meet business requirements and technical specifications for SDK/PoS for Fintech products using Android.
Drive the technical direction and roadmap for Android development, ensuring alignment with company goals and industry best practices.
API integrations in SDK/PoS with backend services
Develop automated unit tests with tools such Appium and espresso.
Advocate for sound design principles and patterns, consistently producing clean and testable code. Value the delivery of incremental improvements.
A passion to improve processes, tools, methodologies & overall quality of the product.
Work closely with developers, product team, QA & BAs to define & develop the best in-class solutions.
Define & implement processes & best practices related to development.
Raising any security compliance issues for SDK /PoS product to the development manager.
Work with the development manager & project teams to develop & maintain the applications in line with defined scripting standards.
An understanding of the software product development lifecycle & test processes
 

What We Expect of You, Day To Day:

Design, build, and maintain Android SDK/PoS and Apps.
Work with engineers, product managers, designers, and stakeholders across the company to bring new features and products.
Maintain & improve the Android frameworks, suggesting improvements where appropriate.
Support the development team by answering questions and solving complex problems.
Ensure developers are following best practices, along with producing clean and secure code.
Write automated unit tests.
Investigate any defects reported by stakeholders / end users & support the team to find the root cause & get the right fixes.
Humble to embrace better ideas from others, eager to make things better, open to challenges and possibilities.
Troubleshoot and resolve complex technical issues related to Android development, both independently and collaboratively with the team.
Understand business requirements & processes to define solutions with continuous review of scope of all requirements following the agile methodology.
Provide estimations on deliverable features to the delivery manager.
Lead by example, demonstrating a strong work ethic, a passion for continuous learning, and a commitment to delivering high-quality software solutions on time and within budget.
Can put yourself in the shoes of your users and be a steward of crafting great developer and consumer experiences
Bright, highly self-motivated and driven with a professional and positive approach.
Ability to multi-task and stay organised in a dynamic work environment.
 

Qualifications: 

Experience with the Android, Java, NDK, C++ and developing complex Android applications. Appreciate the art of API design.
Experience of deploying apps on Google Play store.
Experience with JSON concepts and REST APIs
Experience with design patterns such as MVVM or MVC, Kotlin and Android frameworks.
Conduct code reviews, provide constructive feedback, and enforce coding standards to maintain code quality and ensure adherence to development best practices.
Proactive and enthusiastic quick learner.
Experience across the entire SDLC.
Passionate about software development, with a general thirst for technology & interest in new tools & methodologies.
Proactive and enthusiastic quick learner with the ability to work as part of a team.
Ability to adapt and to drive innovation in an evolving technical environment.
Experienced using version control tools e.g. Git.
Experienced in working with CI/CD pipeline environments.
Ability to solve problems quickly and completely.
Bachelor’s Degree in Computer Science, Computer Engineering and/or relevant work experience.
Desirable Experience:

Experience in working with Common Web application architectures such as n-tier, micro-services, etc.
Experience of working with Point Of Sale devices.
Experience with Docker.
Experience with Unit testing, UI Testing beneficial.
Experience with performance and memory tuning with tools.
Experienced in CI tools (Jenkins, Gitlab Pipelines).
Understanding of MVC of MVVM design patterns desirable.
Additional Information:
Trust Payments is an Equal Opportunities Employer

We are a growing business with an aspiration to create a truly inclusive working environment, where each employee can reach their full potential.  We celebrate the differences that exist within our teams. We encourage our people to bring their own opinions and thoughts to work, to be authentic and help us to innovate. We do this by embracing people as individuals, and appreciating that what works for one person, doesn’t work for everyone. We are committed to equal employment opportunity for all, regardless of race, heritage, religion, gender, national origin, sexual orientation, age, citizenship, marital status, disability, gender identity or any other protected characteristic.
    """

    # Call the function
    optimized_resume = gen(job_description, base_resume)

    # Print the optimized resume
    print("Optimized Resume:")
    print(optimized_resume)


if __name__ == "__main__":
    main()
