# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
import argparse
import json
from statistics import mean
from typing import List


def compute_stats(data: List[dict]) -> dict:
    num_samples = len(data)
    step_counts = [len(d.get("steps", [])) for d in data]
    avg_steps = mean(step_counts) if step_counts else 0
    question_lengths = [len(d.get("question", "").split()) for d in data]
    avg_question_len = mean(question_lengths) if question_lengths else 0

    step_word_lengths = []
    for d in data:
        for step in d.get("steps", []):
            step_word_lengths.append(len(step.split()))
    avg_step_len = mean(step_word_lengths) if step_word_lengths else 0

    return {
        "num_samples": num_samples,
        "avg_steps": avg_steps,
        "avg_question_length": avg_question_len,
        "avg_step_length": avg_step_len,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Show basic statistics for a dataset JSON file")
    parser.add_argument("path", help="Path to dataset JSON file")
    args = parser.parse_args()

    data = json.load(open(args.path))
    stats = compute_stats(data)

    print(f"Samples: {stats['num_samples']}")
    print(f"Average steps per sample: {stats['avg_steps']:.2f}")
    print(f"Average question length (words): {stats['avg_question_length']:.2f}")
    print(f"Average step length (words): {stats['avg_step_length']:.2f}")


if __name__ == "__main__":
    main()
