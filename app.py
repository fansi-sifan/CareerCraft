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
         Organize it in a table with job title, company, descriptions, and skills required.
         Give a title "People with Similar Background" in markdown."""}
    ]
    # Generate response
  # Generate response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.9,
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
        keep it around 200 words, and organize it in markdown."""}
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
        Recommend 5 job titles, try to be creative and think outside of the box. Please provide a table with the following columns:
        - potential job titles that align with the candidate career goal
        - a brief job descriptions
        - a score that evaluates how likely the candidate can get the job, 0-10)
        - skills the candidate need to improve on
        - skills the candidate matches the job descri   ption
        - potential companies, with links to their career page, and explain why this company is recommended
        - resources: training courses, certifications, or industry opinion leaders. provide actual links when available."""}
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
         Please create three examples of people with similar job profiles that have achieved the career goal.
         List their past positions, companies, and explain each career moves they had.
         Organize it in Markdown"""}
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
        
        sections = {
            "Your Job Skills and Similar Job Profiles": (gr.Markdown(), gr.Markdown()),
            "Career Plan Summary": gr.Markdown(),
            "Potential Jobs to Consider": gr.Markdown(),
            "Networking Recommendations": gr.Markdown()
        }
        
        for title, content in sections.items():
            with gr.Row(scale=1):
                gr.Markdown(f"## {title}")
            with gr.Row(scale=1):
                if isinstance(content, tuple):
                    for item in content:
                        item
                else:
                    content
        
        btn.click(fn=summarize_resume, inputs=resume, outputs=sections["Your Job Skills and Similar Job Profiles"][0])
        btn.click(fn=career_profiles, inputs=resume, outputs=sections["Your Job Skills and Similar Job Profiles"][1])
        btn.click(fn=industry_insight, inputs=[resume, goal], outputs=sections["Career Plan Summary"])
        btn.click(fn=job_recommendations, inputs=[resume, goal], outputs=sections["Potential Jobs to Consider"])
        btn.click(fn=networking_connections, inputs=[resume, goal], outputs=sections["Networking Recommendations"])

demo.launch()