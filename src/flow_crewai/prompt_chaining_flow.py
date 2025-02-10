from crewai.flow.flow import Flow , listen, start
from litellm import completion
from dotenv import load_dotenv, find_dotenv

_:bool = load_dotenv(find_dotenv())




class PromptChainingFlow(Flow):

    @start()
    def function1(self):
        response = completion(
            model="gemini/gemini-1.5-flash",
            messages=[
                {"role": "user", "content": "generate any random city name from pakistan only?"}
            ]
        )
        city_name =response.choices[0].message.content
        return city_name

    @listen("function1")
    def function2(self, city_name):
        response = completion(
            model="gemini/gemini-1.5-flash",
            messages=[
                {"role": "user", "content": f"write some fun fact about {city_name} city output must be in the markdown format?"}
            ]
        )
        fun_fact =response.choices[0].message.content
        self.state['fun_fact'] = fun_fact


    @listen("function2")
    def function3(self):
        with open("fun_fact.md", "w") as f:
            f.write(self.state['fun_fact'])


def run_prompt_chaining_flow():
    obj = PromptChainingFlow()
    obj.kickoff()
    obj.plot()