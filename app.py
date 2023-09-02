import openai
import gradio as gr


def summarize_resume(experience):
    messages=[
        {"role": "system", "content": f"""Extract the hard skills and soft skills from {experience}
          Please organize it in bullet points, with subtitles in markdown."""}
    ]

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

def career_profiles(experience):
    messages=[
        {"role": "system", "content": f"""Extract the hard skills and soft skills from {experience}. 
         Give me three typical profiles of people who have similar experience with this candidate, 
         but are 5- 10 years ahead of the user in the career, in a more senior position. 
         Organize it in a table with job title, company, descriptions, and skills required."""}
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
        {"role": "system", "content": f"""You are a career coach. 
         I want you start providing advice for user with this past work experience: {experience} and career goal: {goal}. 
        Give a career plan, analyze the strengths and weakness, as well as the industry or job position insights. 
        keep it around 200 words"""}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.5
    )
    return response['choices'][0]['message']['content'].strip()

def job_recommendations(experience, goal):
    messages=[
        {"role": "system", "content": f"""You are a career coach.
        I want you start providing advice for user with this past work experience: {experience} and career goal: {goal}. 
         Try to be creative and think outside of the box. Please provide a table with the following columns: 
        - potential job titles that align with the candidate career goal
        - a brief job descriptions
        - a score (a score of evaluating the matching level at a salce of 10)
        - Reason(explain the reasoning of the score, lay out strength and weakness)
        - skills the candidate need to improve on
        - the companies the candidate can work for, include company information below:
            - Company Name: the name of the company.
            - Relevance: explain why this company is recommended
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

def networking_connections(experience, goal):
    messages=[
        {"role": "system", "content": f"""You are a career coach. 
         I want you start providing advice for user with this past work experience: {experience} and career goal: {goal}. 
         Please suggest three people with similar career paths that the user could connect with to potentially get to their career goals.
         List their names, job titles, past positions, companies, and try to explain each career move."""}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0
    )
    return response['choices'][0]['message']['content'].strip()



with gr.Blocks() as demo:
    gr.Markdown("# CareerCraft")
    with gr.Column():
        with gr.Row(scale=1):
            resume = gr.Textbox(label='Resume', placeholder="What is your experience? Feel free to copy paste your entire cv or linkedin profile", lines=6)
            goal = gr.Textbox(label='Career Goal', placeholder="What is your career goal? Tell me about your ideal job title, industry, or salary expectation", lines=2)
        btn = gr.Button("Analyze my career path!")
        with gr.Row(scale=1):
            gr.Markdown("## Your Job Skills and similar Job Profiles")
        with gr.Row(scale=1):
            skills = gr.Markdown()
            profiles = gr.Markdown()
        with gr.Row(scale=1):
            gr.Markdown("## Industry Insight")
            industry = gr.Markdown()
        with gr.Row(scale=1):
            gr.Markdown("## Potential Jobs to Consider")
        with gr.Row(scale=1):
            jobs = gr.Markdown()
        with gr.Row(scale=1):
            gr.Markdown("## Networking Recommendations")
        with gr.Row(scale=1):
            connections = gr.Markdown()
        btn.click(fn=summarize_resume, inputs=resume, outputs=skills)
        btn.click(fn=summarize_resume, inputs=resume, outputs=profiles)
        btn.click(fn=industry_insight, inputs=[resume, goal], outputs=industry)
        btn.click(fn=job_recommendations, inputs=[resume, goal], outputs=jobs)
        btn.click(fn=networking_connections, inputs=[resume, goal], outputs=connections)

demo.launch()