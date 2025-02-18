from crewai.flow.flow import Flow, start, listen
import random

class EvaluatorFlow(Flow):
    @start()
    def IN(self):
        print("IN")
        return "initial input"
    
    @listen(IN)
    def generate(self):
        print("generate")
        fruit = random.choice(["apple", "banana", "cherry"])
        print("generate produced:", fruit)
        return fruit
    

    @listen("generate")
    def evaluate(self, fruit):
        print("evaluate: Checking fruit:", fruit)
        if fruit == "banana":
            print("evaluate: Valid fruit received:", fruit)
            return fruit
        else:
            print("evaluate: Invalid fruit, generating again...")
            new_fruit = self.generate()
            return self.evaluate(new_fruit)
            
    
    @listen("evaluate")
    def OUT(self, fruit):
        print("OUT: Final output:", fruit)
        return fruit

def main():
    flow = EvaluatorFlow()
    flow.kickoff()
    flow.plot()

if __name__ == "__main__":
    main()
