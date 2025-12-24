#!/usr/bin/env python
import sys
import warnings
from datetime import datetime

from vizzini_chat.crew import VizziniChat

import argparse

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally via the command line, using config from your YAML files.
# Do not add unnecessary logic to this file.

def run():
    """
    Run the crew kickoff flow (full customer journey scenario).
    """
    try:
        VizziniChat().crew().kickoff()
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

def train(n_iterations, filename):
    """
    Train the crew for a given number of iterations. Stores results in report file.
    """
    try:
        VizziniChat().crew().train(n_iterations=n_iterations, filename=filename)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay(task_id):
    """
    Replay the crew execution from a specific task.
    """
    try:
        VizziniChat().crew().replay(task_id=task_id)
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test(n_iterations, eval_llm):
    """
    Test the crew execution, returning the results.
    """
    try:
        VizziniChat().crew().test(n_iterations=n_iterations, eval_llm=eval_llm)
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


def _help():
    print("""
Usage: python main.py [run|train|replay|test] [args...]

Where:
  run
      Run the default customer journey (kickoff) with sample input.
  train N filename
      Train the crew for N iterations, storing output in 'filename'.
  replay TASK_ID
      Replay the crew from a specific task ID.
  test N EVAL_LLM
      Test the crew for N iterations and evaluation LLM (model name).
""")
    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] in {"-h", "--help"}:
        _help()
    cmd = sys.argv[1]
    if cmd == "run":
        run()
    elif cmd == "train":
        if len(sys.argv) < 4:
            print("train requires N_ITERATIONS and FILENAME arguments.")
            _help()
        try:
            n_iterations = int(sys.argv[2])
        except ValueError:
            print("N_ITERATIONS must be an integer.")
            sys.exit(1)
        filename = sys.argv[3]
        train(n_iterations, filename)
    elif cmd == "replay":
        if len(sys.argv) < 3:
            print("replay requires TASK_ID argument.")
            _help()
        task_id = sys.argv[2]
        replay(task_id)
    elif cmd == "test":
        if len(sys.argv) < 4:
            print("test requires N_ITERATIONS and EVAL_LLM arguments.")
            _help()
        try:
            n_iterations = int(sys.argv[2])
        except ValueError:
            print("N_ITERATIONS must be an integer.")
            sys.exit(1)
        eval_llm = sys.argv[3]
        test(n_iterations, eval_llm)
    else:
        print(f"Unknown command: {cmd}")
        _help()
