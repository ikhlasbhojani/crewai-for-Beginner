
from crewai.flow.flow import Flow, start, listen, router, or_
from litellm import completion
from dotenv import load_dotenv, find_dotenv

_:bool = load_dotenv(find_dotenv()) 

class AutonomousAgentFlow(Flow):

    @start()
    def initial_prompt(self):
        response = completion(
            model="gemini/gemini-1.5-flash",
            messages=[{"role": "user", "content": "Generate a creative idea for an AI article."}]
        )
        idea = response["choices"][0]["message"]["content"].strip()
        self.state["idea"] = idea
        # Set a flag for further branching; for example, if the idea includes the word "technology"
        self.state["is_tech"] = "technology" in idea.lower()
        print("Initial Idea:")
        print(idea)
        return idea

    @router(initial_prompt)
    def choose_flow(self):
        # Route the flow based on the idea category.
        if self.state.get("is_tech"):
            return "tech_flow"
        else:
            return "general_flow"

    @listen("tech_flow")
    def tech_content(self, idea):
        response = completion(
            model="gemini/gemini-1.5-flash",
            messages=[{"role": "user", "content": f"Develop a detailed outline for an AI article focused on technology: {idea}"}]
        )
        outline = response["choices"][0]["message"]["content"].strip()
        return outline

    @listen("general_flow")
    def general_content(self, idea):
        response = completion(
            model="gemini/gemini-1.5-flash",
            messages=[{"role": "user", "content": f"Develop a detailed outline for an AI article: {idea}"}]
        )
        outline = response["choices"][0]["message"]["content"].strip()
        return outline

    @listen(or_(tech_content, general_content))
    def final_optimization(self, outline):
        response = completion(
            model="gemini/gemini-1.5-flash",
            messages=[{"role": "user", "content": f"Improve and polish this article outline: {outline}"}]
        )
        final_outline = response["choices"][0]["message"]["content"].strip()
        print("Final Optimized Outline:")
        print(final_outline)
        return final_outline

def main():
    flow = AutonomousAgentFlow()
    flow.kickoff()
    flow.plot()
