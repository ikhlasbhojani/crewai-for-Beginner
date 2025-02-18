from crewai.flow.flow import Flow, listen, start

class SimpleFlow(Flow):
    @start()
    def IN(self):
        topic = "Ai"
        print("Step 1 Input:" , topic)
        return topic

    @listen(IN)
    def LLMCall1(self, topic):
        print(f"Step 2 LLM Call: {topic} for searching news")
        return topic + " news"

    @listen(LLMCall1)
    def LLMCall2(self, topic_news):
        print(f"Step 3 LLM Call2: {topic_news} for searching artical")
        self.state['topic_news_artical'] = topic_news + " artical"

    @listen(LLMCall2)
    def LLMCall3(self):
        print(f"Step 4 LLM Call3: {self.state['topic_news_artical']} for searching summary")
        self.state['topic_news_artical_summary'] = self.state['topic_news_artical'] + " summary"
    
    @listen(LLMCall3)
    def OUT(self):
        print("Step 5 Output")


def main():
    flow = SimpleFlow()
    flow.kickoff()
    flow.plot("simple_flow")
