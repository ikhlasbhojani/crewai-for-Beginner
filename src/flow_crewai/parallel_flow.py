from crewai.flow.flow import Flow, start, listen, and_, or_

class MatchFlow(Flow):

    @start()
    def IN(self):
        return "start"

    @listen("IN")
    def LLM1(self):
        result = "banana"
        print(result)
        return result

    @listen("IN")
    def LLM2(self):
        result = "grapes"
        print(result)
        return result

    @listen("IN")
    def LLM3(self):
        result = "apple"
        print(result)
        return result


    @listen(or_(LLM1, LLM2, LLM3))
    def aggregate_results(self,result):
        print(result)
        return result

    @listen(aggregate_results)
    def OUT(self, result):
        print(result)

def main():
    flow = MatchFlow()
    flow.kickoff()
    flow.plot()


