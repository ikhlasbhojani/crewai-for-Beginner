from  crewai.flow.flow import Flow, listen, start, router, or_

class RoutingFlow(Flow):
    @start()
    def IN(self):
        print("Step 1 Input")
        self.state['topic'] = "AI"
        print(f"Step 1 Input {self.state['topic']}")

    @router("IN")
    def LLM_call_router(self):
        print(f"Step 2 Routing {self.state['topic']}")
        if self.state['topic'] == "AI":
            return "ai_route"
        elif self.state['topic'] == "AI news":
            return "ai_news_route"
        elif self.state['topic'] == "AI artical":
            return "ai_artical_route"
    

    @listen("ai_route")
    def LLMCall1(self):
        print(f"Step 2 LLM Call1 {self.state['topic']}")
        return self.state['topic'] + " news"

    @listen("ai_news_route")
    def LLMCall2(self):
        print(f"Step 3 LLM Call2 {self.state['topic']}")
        return self.state['topic'] + " artical"

    @listen("ai_artical_route")
    def LLMCall3(self):
        print(f"Step 4 LLM Call3 {self.state['topic']}")
        return self.state['topic'] + " summary"
    
    @listen(or_("LLMCall1", "LLMCall2", "LLMCall3"))
    def output(self):
        print(f"Step 5 Output {self.state['topic']}")

def main():
    flow = RoutingFlow()
    flow.kickoff()
    flow.plot("routing_flow")
