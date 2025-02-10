from crewai.flow.flow import Flow , listen, start, router
import time
import random

class RouterFlow(Flow):
    @start()
    def function1(self):
        topic = random.choice(["tech", "health", "other"])
        return topic

    @router("function1")
    def function2(self, topic):
        if topic == "tech":
            return "tech"
        elif topic == "health":
            return "health"
        else:
            return "other"

    @listen("tech")
    def function3(self, topic):
        print("step3 from function3 ", topic)


    @listen("health")
    def function4(self, topic):
        print("step4 from function4 ", topic)


    @listen("other")
    def function5(self, topic):
        print("step5 from function5 ", topic)


def main():
    flow = RouterFlow()
    flow.kickoff()
    flow.plot()
