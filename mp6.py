import datetime

def get_thought():
    """Prompts the user to enter a thought type and description, and returns them as a dictionary.
       Returns None if the user enters 'q' to quit."""
    while True:
        try:
            thought_type = input("Enter thought type (or 'q' to quit): ")
            if thought_type.lower() == 'q':
                return None

            thought_description = input("Enter thought description: ")
            return {"type": thought_type, "description": thought_description, "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        except Exception as e:
            print(f"An error occurred: {e}")


class ThoughtTracker:
    """A class to track and analyze OCD intrusive thoughts."""

    def __init__(self):
        """Initializes the ThoughtTracker with empty lists for thoughts and thought counts."""
        self.thoughts = []
        self.thought_counts = {}

    def add_thought(self, thought_type, thought_description):
        """Adds a new thought to the tracker, including a timestamp."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.thoughts.append({"type": thought_type, "description": thought_description, "timestamp": timestamp})

        if thought_type not in self.thought_counts:
            self.thought_counts[thought_type] = 0
        self.thought_counts[thought_type] += 1

    def get_summary(self):
        """Returns a summary of thought counts by type."""
        return self.thought_counts

    def get_thoughts_by_date(self, start_date_str, end_date_str):
        """Returns thoughts within a specified date range.  Handles invalid date formats."""
        try:
            start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
            end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")
        except ValueError:
            return "Invalid date format. Please use YYYY-MM-DD."

        filtered_thoughts = []
        for thought in self.thoughts:
            thought_date = datetime.datetime.strptime(thought['timestamp'][:10], "%Y-%m-%d")
            if start_date <= thought_date <= end_date:
                filtered_thoughts.append(thought)
        return filtered_thoughts

    def export_for_analysis(self, filename="thought_data.txt"):
      """Exports the thought data to a text file for analysis by a psychologist or app."""
      try:
        with open(filename, 'w') as f:
          for thought in self.thoughts:
            f.write(f"Type: {thought['type']}, Description: {thought['description']}, Timestamp: {thought['timestamp']}\n")
        print(f"Data exported to {filename}")
      except Exception as e:
        print(f"Error exporting data: {e}")




if __name__ == "__main__":
    tracker = ThoughtTracker()

    while True:
        action = input("Choose action: (a)dd, (s)ummary, (f)ilter, (e)xport, (q)uit: ")

        if action.lower() == 'q':
            break
        elif action.lower() == 'a':
            new_thought = get_thought()
            if new_thought:
                tracker.add_thought(new_thought['type'], new_thought['description'])
        elif action.lower() == 's':
            summary = tracker.get_summary()
            print("Thought Summary:")
            for thought_type, count in summary.items():
                print(f"- {thought_type}: {count}")
        elif action.lower() == 'f':
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            filtered_thoughts = tracker.get_thoughts_by_date(start_date, end_date)

            if isinstance(filtered_thoughts, str):
                print(filtered_thoughts)  # Print error message if invalid dates
            elif filtered_thoughts:
                print("Filtered Thoughts:")
                for thought in filtered_thoughts:
                    print(thought)
            else:
                print("No thoughts found in that date range.")

        elif action.lower() == 'e':
            tracker.export_for_analysis() # Could prompt user for a file name here if you want.
        else:
            print("Invalid action. Please try again.")