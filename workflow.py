# @ Author: Bertan Berker
# @ language: Python
# This file contains the workflow for the agentic system that is used to generate a renovation image

from agent import *

# This functions is the main workflow for the agentic system
# :param user_prompt: The prompt from the user
# :return: The generated image
def start_workflow(user_prompt):

    # 1. Process the user_prompt for keywords related to design style like
    # Room_type, Price, Color, Style
    # 2. Create an SQL query to fetch the top 5 images that match these keywords
    # 3. Use the image description of these 5 images to come up with a complete description
    # to create a renovation image prompt
    # 4. Finally generate a new image

    requirements = analyze_requirements(user_prompt)
    sql_commands = generate_sql_commands(requirements)
    image_descriptions = run_sql_commands(sql_commands)
    description = generate_description(image_descriptions, user_prompt)
    image_url = generate_image(description) 
    
    return image_url