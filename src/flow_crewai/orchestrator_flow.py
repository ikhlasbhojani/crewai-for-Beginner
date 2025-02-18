from crewai.flow.flow import Flow, start, listen, or_, router, and_

class OrchestratorFlow(Flow):

    @start()
    def IN(self):
        # Starting point of the flow.
        print("IN")
        return "initial input"

    @listen("IN")
    def orchestrator(self, inp):
        print("give some instructions")
        # Return some instructions (or simply pass along the data)
        return "instructions"

    @listen(and_(orchestrator))
    def LLM1(self, instructions):
        print("LLM1")
        return "LLM1 result"
    
    @listen(and_(orchestrator))
    def LLM2(self, instructions):
        print("LLM2")
        return "LLM2 result"
    
    @listen(and_(orchestrator))
    def LLM3(self, instructions):
        print("LLM3")
        return "LLM3 result"

    @listen(and_("LLM1", "LLM2", "LLM3"))
    def synthesizer(self, results):
        print("aggregate results", results)
        # Combine the results as needed
        return "aggregated results"

    @listen("synthesizer")
    def OUT(self, aggregated):
        print("OUT", aggregated)
        return None  # Terminal node, so we return None

def main():
    flow = OrchestratorFlow()
    flow.kickoff()
    flow.plot()
