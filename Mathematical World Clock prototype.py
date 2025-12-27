# Mathematical World Clock Prototype
# Author: Captain Leif (Jarvondis Project)
# Purpose: A lineage-safe chronometer using pure math, not atoms

import math

class MathematicalWorldClock:
    def __init__(self, drift_per_day=1e-9):
        """
        Initialize the clock.
        :param drift_per_day: simulated drift in seconds per day (default: 1 nanosecond)
        """
        self.baseline_second = 1.0   # unity second
        self.drift_per_day = drift_per_day
        self.current_time = 0.0
        self.error_log = []

    def tick_day(self, day):
        """
        Simulate one day of clock operation with drift and auto-correction.
        """
        # Apply drift
        drifted_second = self.baseline_second + self.drift_per_day

        # Auto-correction: normalize back to unity
        corrected_second = drifted_second / drifted_second * self.baseline_second

        # Track cumulative error
        error = drifted_second - corrected_second
        self.error_log.append((day, error))

        # Advance time
        self.current_time += corrected_second * 86400  # seconds in a day

    def run_simulation(self, days=3650):
        """
        Run the simulation for a given number of days.
        """
        for day in range(1, days + 1):
            self.tick_day(day)

    def report(self):
        """
        Print summary of cumulative error.
        """
        total_error = sum(error for _, error in self.error_log)
        print("Simulation complete.")
        print(f"Days simulated: {len(self.error_log)}")
        print(f"Cumulative error: {total_error:.12f} seconds")
        print(f"Equivalent in microseconds: {total_error * 1e6:.6f} µs")

# Run a 10-year test (3650 days)
if __name__ == "__main__":
    clock = MathematicalWorldClock(drift_per_day=1e-9)
    clock.run_simulation(days=3650)
    clock.report()
