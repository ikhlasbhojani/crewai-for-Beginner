from crewai.flow.flow import Flow, start, listen, or_

class MatchFlow(Flow):

    @start()
    def process_banana(self):
        result = "banana"
        return result

    @start()
    def process_grapes(self):
        result = "grapes"
        print(f"Route 2 processed: {result}")
        return result

    @start()
    def process_apple(self):
        result = "apple"
        print(f"Route 3 processed: {result}")
        return result


    @listen(or_(process_banana, process_grapes, process_apple))
    def match_results(self,result):
        input_value = "apple"
        if result == input_value:
            print(f"Match Found: {result}")
            return result
        else:
            print(f"No match for: {result}")
            return None

    @listen("match_results")
    def show_output(self, matched_result):
        if matched_result:
            print(f"Final Output: {matched_result}")
        else:
            print("No valid output found!")

def main():
    flow = MatchFlow()
    flow.kickoff()
    flow.plot()

if __name__ == "__main__":
    main()
