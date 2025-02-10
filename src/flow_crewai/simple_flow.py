from crewai.flow.flow import Flow , start, listen
import time

class SimpleFlow(Flow):
    @start()
    def function1(self):
        print("step1 from function1")
        time.sleep(5)

    @listen(function1)
    def function2(self):
        print("step2 from function2")
        time.sleep(5)


    @listen("function2")
    def function3(self):
        print("step3 from function3")


def kickoff():
    obj = SimpleFlow()
    obj.kickoff()
    obj.plot()

   