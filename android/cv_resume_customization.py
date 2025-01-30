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

#    ---
#
# ### **Additional Questions to Answer**
# Provide **concise and structured responses** to the following:
#
# #### **1. Can you describe the highest level of decision-making you’ve been involved in as a Software Engineer?**
# - Explain **architectural decisions, technology stack selection, scalability strategies**, or major system-level choices.
# - Mention experience in **microservices, cloud infrastructure, security policies, or system integrations**.
#
# #### **2. Have you ever been a part of building a backend system from scratch and scaling it?**
# - If yes, describe **the system, its tech stack, scalability challenges, and how they were addressed**.
# - Highlight **database design, API development, cloud infrastructure, and DevOps practices used**.
#
# ---

base_cv = """Nishant Tanwar
Senior Android Developer
nishantt21@gmail.com
www.linkedin.com/in/nishantt12

To:
The Chan Zuckerberg Initiative Team

Dear CZI Team,

I am excited to apply for the Senior Engineer position at the Chan Zuckerberg Initiative. With over 10 years of experience in software development and a current role at Tala, I am eager to contribute to your mission of building a more inclusive, just, and healthy future for everyone.

At Tala, I played a crucial role in developing a scalable financial system serving over 20 million users. I led the implementation of dynamic features that enhanced user engagement by 20% and integrated a Server-Driven UI framework with Jetpack Compose, reducing the app size by 25%. My expertise in technologies such as Kubernetes, Google Cloud Platform, AWS, Android, Kotlin, Java, and Microservices aligns well with the technical needs of CZI’s Central Tech team.

I am particularly drawn to CZI’s focus on enhancing infrastructure and security to support impactful initiatives. I am enthusiastic about the opportunity to analyze and improve the efficiency, stability, and security of CZI's engineering, and to contribute to building shared technology solutions for multiple teams. My experience in developing robust and scalable systems, combined with my passion for optimizing operations and implementing best practices, positions me well to drive significant impact at CZI.

Thank you for considering my application. I look forward to the opportunity to discuss how my skills and experiences align with your needs.

Best regards,
Nishant Tanwar"""

def gen(job_description):


    client = OpenAI(
        api_key="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"
    )

    prompt = f"""
          You are a cover letter optimization assistant. Your task is to create a cover letter to align with the provided job description. Ensure the following updates are made:

    Ensure that the CV is optimized for ATS (Applicant Tracking System) and includes relevant keywords from the job description.

          Job Description: {job_description}

          CV: {base_cv}
          """

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {"role": "system", "content": "You are a cover letter optimization assistant."},
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print(completion.choices[0].message.content)



def main():
    # Load the base resume from the JSON file

    # Example job description
    job_description = """
Are you passionate about building great products? Do you want to redefine the way travellers explore the world? Keen to be part of this growth journey with a bunch of amazing people? Then Pelago is the place for you!

We are looking for ambitious and motivated talents who are excited about staying on the cutting edge of Technology and always keen on innovating new ways to drive growth and taking our startup to new heights.

WHO ARE WE? 
Pelago is a travel experiences platform created by Singapore Airlines Group. Think of us as a travel magazine that you can book - highly curated, visually inspiring, with the trust and quality of Singapore Airlines. We connect you with global, local cultures and ideas so you can expand your life.

We are a team of diverse, passionate, empowered, inclusive, authentic and open individuals who share the same values and strive towards a common goal!

WHAT CAN WE OFFER YOU?  
- A unique opportunity to take end-to-end ownership of your workstream to deliver real value to users. 
- Platforms to solve real user problems concerning travel planning & booking with innovative products/services.
- An amazing peer group to work with, and the ability to learn from the similarly great minds around you. 
- An opportunity to be an integral part of shaping the company’s growth and culture with a diverse, fun, and dynamic environment with teammates from different parts of the world.
- Competitive compensation and benefits - including work flexibility, insurance, remote working and more!

WHAT WILL YOU DO?
- Write code as part of a diverse and multi-skilled development team
- Design and architect innovative, modern architectures
- Champion and focus on software qualities such as testability, security, scalability, operability etc
- Work with state of the art technologies to solve genuine, real-world problems
- Champion good agile practices that provide a foundation for iterative product development
- Build strong relationships with product managers, designers and business team 
- Enjoy working in a diverse, dynamic, collaborative, transparent, environment where everyone's ideas and opinions are equally valued
- Demonstrate and communicate a passion for implementing highly scalable and maintainable backend services
- Share technical solutions and product ideas through design review, pair programming, code review and technological discussions

WHAT EXPERTISE YOU NEED TO HAVE?
- 4+ years experience in building production-grade, performant frontend apps with a modern JS frameworks React/React-Native using the latest ECMAScript standards (ES6 / ES7) and/or TypeScript
- Working with CSS preprocessors like SASS, SCSS, or LESS
- Experience working with Agile, Lean and Continuous Delivery approaches, such as Continuous Integration, TDD
- Working closely and proactively with the backend team, building scalable apis and designing data structures to ensure consistency and availability
- Strong people skills that contribute to an open and collaborative environment
- Experience in communicating ideas and decisions to a variety of team members
- Working closely and proactively with product managers and designers to deliver a high-quality user experiences
- Experience or knowledge of working with GraphQL API’s (good to have)
- Experience working in the travel industry or with B2C consumer platforms (good to have)
- Experience deploy/ ship production app to AppStore / PlayStore (good to have)

Below are the technologies we primarily use. However, we'll always choose the best tool for the job (maybe you can suggest one?), so don't consider this list either exhaustive or immutable: 

Languages / Frameworks
JavaScript, Typescript, ReactJs, React-Native (Swift, Kotlin, Java), Apollo GraphQL
    """

    # Call the function
    optimized_cv = gen(job_description)

    # Print the optimized
    print("Optimized CV:")
    print(optimized_cv)


if __name__ == "__main__":
    main()
