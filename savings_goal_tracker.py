#!/usr/bin/env python3
from typing import Dict, List
import random

class SavingsGoal:
    def __init__(self, goal_name: str, target_amount: float, monthly_contribution: float):
        self.goal_name = goal_name
        self.target_amount = target_amount
        self.monthly_contribution = monthly_contribution
        self.balance = 0.0
        self.history: List[float] = []

    def deposit(self, amount: float = None):
        if amount is None:
            amount = self.monthly_contribution
        self.balance += amount
        self.history.append(self.balance)

    def months_to_goal(self) -> int:
        if self.monthly_contribution <= 0:
            return -1
        remaining = self.target_amount - self.balance
        return max(0, int((remaining + self.monthly_contribution - 1) // self.monthly_contribution))

    def is_goal_reached(self) -> bool:
        return self.balance >= self.target_amount

    def summary(self) -> Dict[str, float]:
        return {
            "Goal": self.goal_name,
            "Target": self.target_amount,
            "Balance": round(self.balance, 2),
            "Remaining": round(max(0, self.target_amount - self.balance), 2),
            "Months to Goal": self.months_to_goal()
        }

def demo():
    vacation = SavingsGoal("Vacation Fund", 2000, 250)
    for month in range(1, 10):
        vacation.deposit()
        print(f"Month {month}:", vacation.summary())
    print("Goal Reached?", vacation.is_goal_reached())

if __name__ == "__main__":
    demo()
