import openai


def summarize_resume(experience):
    messages=[
        {"role": "system", "content": f"Extract the hard skills and soft skills from {experience} Please organize it in bullet points in markdown. Also give me three typical profiles of people who have similar experience with this job candidate, but are 10 years ahead of the user in the career, in a more senior position. Organize it in a table with job title, company, descriptions, and skills required. Give the table a title"}
    ]
    # Generate response
  # Generate response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0,
        # stream=True
        # Add additional parameters here, such as prompt_id, file, or codify
  )

  # Return response
    return response['choices'][0]['message']['content'].strip()

def industry_insight(experience, goal):
    messages=[
        {"role": "system", "content": f"""You are a career coach. I want you start providing advice for user with this past work experience: {experience} and career goal: {goal}. 
        Please provide an overview of the industry insight, the job market for the recommended jobs. (keep it around 500 words)"""}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0
    )
    return response['choices'][0]['message']['content'].strip()

def job_recommendations(experience, goal):
    messages=[
        {"role": "system", "content": f"""You are a career coach. I want you start providing advice for user with this past work experience: {experience} and career goal: {goal}. 
         Try to be creative and think outside of the box.
        Please provide a table with the following columns: 
        - potential job titles that align with the candidate career goal
        - a brief job descriptions
        - a score (a score of evaluating the matching level at a salce of 10)
        - Reason(explain the reasoning of the score, lay out strength and weakness)
        - skills the candidate need to improve on
        - resources they can use (organize it as a nice table):
            - Information to get: Twitter account, Newsletter or website, please provide actual links when available. 
            - What are the training courses or certifications can be recommended, provide actual links when available."""}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.5
    )
    return response['choices'][0]['message']['content'].strip()

def company_recommendations(experience, goal):
    messages=[
        {"role": "system", "content": f"""You are a career coach. I want you start providing advice for user with this past work experience: {experience} and career goal: {goal}. 
        Please make another table using the same list of job titles, add the companies the candidate can work for, include company information below:
            - Company Name: the name of the company.
            - Location: the location of the company.
            - Industry: the industry the company belongs to.
            - Relevance: explain why this company is recommended."""}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0
    )
    return response['choices'][0]['message']['content'].strip()

def networking_connections(experience, goal):
    messages=[
        {"role": "system", "content": f"""You are a career coach. I want you start providing advice for user with this past work experience: {experience} and career goal: {goal}. 
        Please recommend three people with similar career paths that the user could connect with to potentially get her to her career goals. List their names, job titles, past positions, companie."""}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0
    )
    return response['choices'][0]['message']['content'].strip()



import gradio as gr

with gr.Blocks() as demo:
    gr.Markdown("# CareerCraft")
    with gr.Column():
        with gr.Row(scale=1):
            resume = gr.Textbox(label='Resume', placeholder="What is your experience? Feel free to copy paste your entire cv or linkedin profile", lines=6)
            goal = gr.Textbox(label='Career Goal', placeholder="What is your career goal? Tell me about your ideal job title, industry, or salary expectation", lines=2)
        btn = gr.Button("Analyze my career path!")
        with gr.Row(scale=1):
            gr.Markdown("## Your Job Skills and Industry Insights")
        with gr.Row(scale=1):
            skills = gr.Markdown(label="Skills", lines=10)
            industry = gr.Markdown(label="Industry Insights", lines=10)
        with gr.Row(scale=1):
            gr.Markdown("## Potential Jobs to Consider")
        with gr.Row(scale=1):
            jobs = gr.Markdown(label="Job Recommendations", lines=10)
        with gr.Row(scale=1):
            gr.Markdown("## Company and Networking Recommendations")
        with gr.Row(scale=1):
            companies = gr.Markdown(label="Company Recommendations", lines=10)
            connections = gr.Markdown(label="Networking Connections", lines=10)
        btn.click(fn=summarize_resume, inputs=resume, outputs=skills)
        btn.click(fn=industry_insight, inputs=[resume, goal], outputs=industry)
        btn.click(fn=job_recommendations, inputs=[resume, goal], outputs=jobs)
        btn.click(fn=company_recommendations, inputs=[resume, goal], outputs=companies)
        btn.click(fn=networking_connections, inputs=[resume, goal], outputs=connections)

demo.launch()